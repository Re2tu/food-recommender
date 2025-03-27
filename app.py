import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer, util
import random
from datetime import datetime
import torch
from states_data import STATE_FOODS, STATES, STATE_SEASONAL_PRODUCE

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #f7d794, #f3a683);
        font-family: 'Arial', sans-serif;
    }
    .title {
        font-size: 40px;
        color: #d63031;
        text-align: center;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    .subtitle {
        font-size: 20px;
        color: #2d3436;
        text-align: center;
        margin-bottom: 30px;
    }
    .selectbox-label {
        font-size: 18px;
        color: #2d3436;
        margin-bottom: 5px;
    }
    .stButton>button {
        background-color: #e17055;
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #d63031;
    }
    .dataframe {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 10px;
    }
    .dataframe th {
        background-color: #e17055;
        color: white;
        font-size: 16px;
    }
    .dataframe td {
        font-size: 14px;
        color: #2d3436;
    }
    .footer {
        font-size: 14px;
        color: #636e72;
        text-align: center;
        margin-top: 30px;
    }
    .diet-chart-section {
        font-size: 18px;
        color: #d63031;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .seasonal-produce {
        font-size: 16px;
        color: #2d3436;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Determine the current season based on the date
def get_current_season(date):
    month = date.month
    # Indian seasons (approximate)
    if 3 <= month <= 5:  # March to May
        return "Summer"
    elif 6 <= month <= 9:  # June to September
        return "Monsoon"
    elif 10 <= month <= 11:  # October to November
        return "Autumn"
    else:  # December to February
        return "Winter"

# Mock dataset creation for main dishes
def create_mock_data():
    country = "India"
    diet_types = ["Vegetarian", "Non-Vegetarian", "Vegan"]
    seasons = ["All Seasons", "Winter", "Summer", "Monsoon", "Autumn"]

    data = []
    for state in STATES:
        for food, ingredients, calories, protein, carbs, fats, meal_type in STATE_FOODS[state]:
            diet = random.choice(diet_types)
            season = random.choice(seasons)
            data.append([country, state, f"{country}_{state}", food, diet, season, ingredients, calories, protein, carbs, fats, meal_type])

    return pd.DataFrame(data, columns=["country", "state", "locality", "food_item", "diet_type", "best_season", "key_ingredients", "calories", "protein", "carbs", "fats", "meal_type"])

# Check if a food item uses seasonal produce
def uses_seasonal_produce(ingredients, seasonal_fruits, seasonal_vegetables):
    ingredients_list = [ingredient.strip().lower() for ingredient in ingredients.split(",")]
    seasonal_items = [item.lower() for item in seasonal_fruits + seasonal_vegetables]
    return any(ingredient in seasonal_items for ingredient in ingredients_list)

# Get recommendations for main dishes using transformers
def get_transformer_recommendations(locality, df, model, diet_filter=None, health_goal=None, season_filter=None, state=None, top_n=5):
    # Filter data for the selected locality
    locality_df = df[df["locality"] == locality]
    
    if locality_df.empty:
        return pd.DataFrame(columns=["Food Item", "Diet Type", "Best Season", "Key Ingredients", "Calories", "Protein (g)", "Carbs (g)", "Fats (g)", "Meal Type", "Similarity Score"])

    # Apply diet type filter if specified
    if diet_filter and diet_filter != "All":
        locality_df = locality_df[locality_df["diet_type"] == diet_filter]

    # Apply season filter if specified
    if season_filter and season_filter != "All Seasons":
        locality_df = locality_df[(locality_df["best_season"] == season_filter) | (locality_df["best_season"] == "All Seasons")]

    # Apply health goal filter if specified
    if health_goal:
        if health_goal == "Low-Calorie":
            locality_df = locality_df[locality_df["calories"] <= 200]
        elif health_goal == "High-Protein":
            locality_df = locality_df[locality_df["protein"] >= 15]

    if locality_df.empty:
        return pd.DataFrame(columns=["Food Item", "Diet Type", "Best Season", "Key Ingredients", "Calories", "Protein (g)", "Carbs (g)", "Fats (g)", "Meal Type", "Similarity Score"])

    # Get seasonal produce for the selected state and season
    seasonal_produce = STATE_SEASONAL_PRODUCE.get(state, {})
    seasonal_fruits = seasonal_produce.get(season_filter, {}).get("Fruits", [])
    seasonal_vegetables = seasonal_produce.get(season_filter, {}).get("Vegetables", [])

    # Encode the ingredients of foods in the selected locality only
    locality_embeddings = model.encode(locality_df["key_ingredients"].tolist(), convert_to_tensor=True)

    # Compute the average embedding for the locality
    locality_embedding = locality_embeddings.mean(dim=0)

    # Compute cosine similarity between the average locality embedding and the foods in the locality
    scores = util.pytorch_cos_sim(locality_embedding, locality_embeddings)[0]

    # Boost scores for foods that use seasonal produce
    boosted_scores = []
    for idx, score in enumerate(scores):
        ingredients = locality_df.iloc[idx]["key_ingredients"]
        if uses_seasonal_produce(ingredients, seasonal_fruits, seasonal_vegetables):
            boosted_scores.append(score.item() + 0.1)  # Add a small boost for seasonal produce
        else:
            boosted_scores.append(score.item())

    # Convert boosted scores back to tensor for sorting
    boosted_scores = torch.tensor(boosted_scores)

    # Get the indices of the top-scoring foods within the locality
    top_indices = boosted_scores.argsort(descending=True)[:min(top_n, len(boosted_scores))]

    # Prepare recommendations
    top_foods = []
    for idx in top_indices:
        idx = idx.item()
        food_info = locality_df.iloc[idx]
        top_foods.append({
            "Food Item": food_info["food_item"],
            "Diet Type": food_info["diet_type"],
            "Best Season": food_info["best_season"],
            "Key Ingredients": food_info["key_ingredients"],
            "Calories": food_info["calories"],
            "Protein (g)": food_info["protein"],
            "Carbs (g)": food_info["carbs"],
            "Fats (g)": food_info["fats"],
            "Meal Type": food_info["meal_type"],
            "Similarity Score": round(boosted_scores[idx].item(), 2)
        })
    return pd.DataFrame(top_foods)

# Recommend seasonal produce as snacks or sides
def recommend_seasonal_produce(state, season):
    seasonal_produce = STATE_SEASONAL_PRODUCE.get(state, {}).get(season, {})
    fruits = seasonal_produce.get("Fruits", [])
    vegetables = seasonal_produce.get("Vegetables", [])

    recommendations = []
    # Recommend fruits as snacks
    for fruit in fruits:
        recommendations.append({
            "Food Item": f"Fresh {fruit}",
            "Diet Type": "Vegan",
            "Best Season": season,
            "Key Ingredients": fruit,
            "Calories": 50,  # Approximate for most fruits
            "Protein (g)": 1,
            "Carbs (g)": 12,
            "Fats (g)": 0,
            "Meal Type": "Snack"
        })
    # Recommend vegetables as sides
    for vegetable in vegetables:
        recommendations.append({
            "Food Item": f"Steamed {vegetable}",
            "Diet Type": "Vegan",
            "Best Season": season,
            "Key Ingredients": vegetable,
            "Calories": 30,  # Approximate for most steamed vegetables
            "Protein (g)": 2,
            "Carbs (g)": 6,
            "Fats (g)": 0,
            "Meal Type": "Side"
        })
    return pd.DataFrame(recommendations)

# Streamlit app
def main():
    st.markdown('<div class="title">🍴 Locality-Based Diet Chart Recommendation System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Discover delicious and healthy foods from your selected region in India!</div>', unsafe_allow_html=True)

    # Mock data for main dishes
    df = create_mock_data()

    # Load transformer model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Determine current season
    current_date = datetime(2025, 3, 19)  # Current date as per your setup
    current_season = get_current_season(current_date)
    st.markdown(f'<div class="subtitle">Current Season: {current_season}</div>', unsafe_allow_html=True)

    # UI elements with layout
    col1, col2, col3 = st.columns([1, 1, 1])
    col4, col5 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="selectbox-label">Select Country 🌍</div>', unsafe_allow_html=True)
        countries = df["country"].unique()
        selected_country = st.selectbox("", countries, key="country_select")

    with col2:
        st.markdown('<div class="selectbox-label">Select State 🏞️</div>', unsafe_allow_html=True)
        states = df[df["country"] == selected_country]["state"].unique()
        selected_state = st.selectbox("", states, key="state_select")

    with col3:
        st.markdown('<div class="selectbox-label">Select Diet Type 🥗</div>', unsafe_allow_html=True)
        diet_types = ["All", "Vegetarian", "Non-Vegetarian", "Vegan"]
        selected_diet = st.selectbox("", diet_types, key="diet_select")

    with col4:
        st.markdown('<div class="selectbox-label">Select Health Goal 💪</div>', unsafe_allow_html=True)
        health_goals = ["None", "Low-Calorie", "High-Protein"]
        selected_health_goal = st.selectbox("", health_goals, key="health_goal_select")

    with col5:
        st.markdown('<div class="selectbox-label">Select Season 🌦️</div>', unsafe_allow_html=True)
        seasons = ["All Seasons", "Summer", "Monsoon", "Autumn", "Winter"]
        selected_season = st.selectbox("", seasons, index=seasons.index(current_season), key="season_select")

    if st.button("Get Diet Chart"):
        locality = f"{selected_country}_{selected_state}"
        
        # Get main dish recommendations
        recommendations = get_transformer_recommendations(
            locality, df, model, 
            diet_filter=selected_diet, 
            health_goal=selected_health_goal if selected_health_goal != "None" else None,
            season_filter=selected_season,
            state=selected_state,
            top_n=5
        )

        # Get seasonal produce recommendations
        seasonal_recommendations = recommend_seasonal_produce(selected_state, selected_season)

        # Display main diet chart
        st.subheader(f"Your Daily Diet Chart for {selected_state}, {selected_country} 🍽️")
        if not recommendations.empty:
            # Group main dish recommendations by meal type
            meal_types = ["Breakfast", "Lunch", "Dinner", "Snack", "Side"]
            for meal_type in meal_types:
                meal_df = recommendations[recommendations["Meal Type"] == meal_type]
                if not meal_df.empty:
                    st.markdown(f'<div class="diet-chart-section">{meal_type}</div>', unsafe_allow_html=True)
                    st.dataframe(
                        meal_df.drop(columns=["Meal Type"]).style.format({
                            "Similarity Score": "{:.2f}", 
                            "Calories": "{:.0f}", 
                            "Protein (g)": "{:.0f}", 
                            "Carbs (g)": "{:.0f}", 
                            "Fats (g)": "{:.0f}"
                        }), 
                        use_container_width=True
                    )

        # Display seasonal produce recommendations
        if not seasonal_recommendations.empty:
            st.markdown(f'<div class="diet-chart-section">Seasonal Snacks and Sides 🌱</div>', unsafe_allow_html=True)
            for meal_type in ["Snack", "Side"]:
                seasonal_meal_df = seasonal_recommendations[seasonal_recommendations["Meal Type"] == meal_type]
                if not seasonal_meal_df.empty:
                    st.markdown(f'<div class="diet-chart-section">{meal_type}</div>', unsafe_allow_html=True)
                    st.dataframe(
                        seasonal_meal_df.drop(columns=["Meal Type"]).style.format({
                            "Calories": "{:.0f}", 
                            "Protein (g)": "{:.0f}", 
                            "Carbs (g)": "{:.0f}", 
                            "Fats (g)": "{:.0f}"
                        }), 
                        use_container_width=True
                    )

        if recommendations.empty and seasonal_recommendations.empty:
            st.write(f"No recommendations available for {selected_state}, {selected_country} with the selected filters.")

        st.markdown('<div class="footer">These recommendations are based on the similarity of food ingredients in the selected locality, with a boost for dishes using seasonal produce.</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()