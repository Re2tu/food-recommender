# Locality-Based Diet Chart Recommendation System 🍴

This project is a Streamlit-based web application that recommends food items based on locality, season, and dietary preferences. It utilizes the `SentenceTransformer` model for ingredient-based similarity scoring and boosts recommendations using seasonal produce.

## Features
- Recommends meals based on state and locality.
- Filters results by diet type (Vegetarian, Non-Vegetarian, Vegan).
- Supports health goals (Low-Calorie, High-Protein).
- Boosts recommendations with seasonal produce.
- Uses `SentenceTransformer` for intelligent recommendations.

## Installation

1. Clone the repository:

   ```sh
   git clone ([https://github.com/Re2tu/food-recommender.git](https://github.com/Re2tu/food-recommender.git))
   cd food-recommender
   ```
2.Install dependencies
  ```sh  
  pip install -r requirements.txt
```
3.Run the application
```sh
    streamlit run app.py
```

