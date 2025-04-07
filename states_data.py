# states_data.py
# Data for all 28 states in India, with at least 10 food items per state, including ingredients, calories, and nutritional details

STATE_FOODS = {
    "Andhra Pradesh": [
        ("Pesarattu", "Green Gram, Rice, Green Chillies, Ginger", 200, 8, 30, 5, "Breakfast"),
        ("Gongura Pachadi", "Sorrel Leaves, Red Chillies, Garlic, Tamarind", 150, 2, 10, 10, "Side"),
        ("Prawn Iguru", "Prawns, Onions, Tomatoes, Spices", 250, 20, 5, 15, "Dinner"),
        ("Biryani", "Rice, Chicken, Spices, Saffron", 600, 25, 80, 20, "Lunch"),
        ("Pulihora", "Rice, Tamarind, Peanuts, Spices", 300, 5, 50, 10, "Lunch"),
        ("Gutti Vankaya", "Brinjal, Peanuts, Spices, Coconut", 200, 4, 15, 12, "Side"),
        ("Chepala Pulusu", "Fish, Tamarind, Onions, Spices", 300, 22, 10, 18, "Dinner"),
        ("Ariselu", "Rice Flour, Jaggery, Ghee", 400, 3, 60, 15, "Snack"),
        ("Pappu Charu", "Lentils, Tamarind, Tomatoes, Spices", 150, 6, 20, 3, "Side"),
        ("Kodi Kura", "Chicken, Onions, Tomatoes, Spices", 350, 28, 10, 20, "Dinner"),
        ("Royyala Vepudu", "Prawns, Garlic, Curry Leaves, Red Chillies", 280, 22, 8, 16, "Dinner"),
        ("Bendakaya Pulusu", "Okra, Tamarind, Jaggery, Spices", 180, 3, 25, 6, "Side"),
        ("Miriyala Rasam", "Black Pepper, Tamarind, Garlic, Cumin", 120, 2, 15, 4, "Side"),
        ("Kobbari Annam", "Rice, Coconut, Cashews, Spices", 320, 6, 50, 10, "Lunch"),
        ("Chintakaya Pachadi", "Raw Tamarind, Green Chillies, Spices", 140, 2, 12, 8, "Side"),
        ("Natukodi Pulusu", "Country Chicken, Tamarind, Spices", 380, 30, 12, 22, "Dinner"),
        ("Ulava Charu", "Horse Gram, Garlic, Spices", 160, 7, 22, 3, "Side"),
        ("Ragi Sangati", "Finger Millet, Rice, Water", 220, 5, 40, 2, "Lunch"),
        ("Kakarakaya Fry", "Bitter Gourd, Spices, Oil", 170, 3, 20, 8, "Side"),
        ("Pootharekulu", "Rice Flour, Sugar, Ghee", 350, 4, 55, 12, "Snack"),
        ("Mukkala Pulusu", "Mixed Vegetables, Tamarind, Spices", 190, 4, 28, 6, "Side"),
        ("Pappula Podi", "Roasted Gram, Red Chillies, Spices", 130, 5, 15, 5, "Side"),
        ("Chicken Vepudu", "Chicken, Green Chillies, Curry Leaves", 360, 27, 8, 23, "Dinner"),
        ("Bobbatlu", "Wheat Flour, Lentils, Jaggery", 380, 8, 60, 12, "Snack"),
        ("Dondakaya Fry", "Ivy Gourd, Spices, Peanuts", 160, 3, 18, 7, "Side"),
        ("Sunnundalu", "Urad Dal, Jaggery, Ghee", 420, 10, 60, 15, "Snack"),
        ("Tomato Pappu", "Lentils, Tomatoes, Green Chillies", 170, 7, 23, 4, "Side"),
        ("Pallikaram Dosa", "Rice, Peanuts, Spices", 240, 6, 35, 8, "Breakfast"),
        ("Mutton Iguru", "Mutton, Onions, Spices", 430, 32, 10, 28, "Dinner"),
        ("Kandi Podi", "Toor Dal, Red Chillies, Garlic", 140, 6, 18, 4, "Side")
    ],
    "Arunachal Pradesh": [
        ("Pika Pila", "Rice, Bamboo Shoot, Spices, Ginger", 200, 4, 35, 5, "Lunch"),
        ("Lukter", "Beef, Bamboo Shoot, Chillies, Garlic", 300, 25, 5, 20, "Dinner"),
        ("Apong", "Rice, Fermented Yeast", 150, 2, 30, 0, "Snack"),
        ("Bamboo Shoot Fry", "Bamboo Shoot, Spices, Garlic", 100, 2, 15, 3, "Side"),
        ("Kharzi", "Rice, Chicken, Spices, Herbs", 400, 20, 50, 15, "Lunch"),
        ("Mung Bean Soup", "Mung Beans, Ginger, Garlic, Spices", 150, 8, 20, 2, "Side"),
        ("Pork with Bamboo", "Pork, Bamboo Shoot, Chillies", 350, 22, 5, 25, "Dinner"),
        ("Zan", "Millet, Water, Fermented Yeast", 200, 3, 40, 2, "Snack"),
        ("Fish Stew", "Fish, Herbs, Spices, Ginger", 250, 18, 10, 15, "Dinner"),
        ("Chicken with Herbs", "Chicken, Local Herbs, Spices", 300, 25, 5, 18, "Dinner"),
        ("Oying", "Mixed Vegetables, Bamboo Shoot, Ginger", 130, 3, 18, 4, "Side"),
        ("Ngatok", "Fish, Local Spices, Banana Leaf", 280, 20, 8, 15, "Dinner"),
        ("Pe Hak", "Fermented Soybeans, Chillies, Garlic", 140, 7, 12, 6, "Side"),
        ("Amra", "Pork, Dry Chillies, Smoked Spices", 420, 28, 5, 30, "Dinner"),
        ("Rice Cake", "Sticky Rice, Salt, Spices", 250, 4, 45, 5, "Snack"),
        ("Yom Pat", "Wild Greens, Garlic, Spices", 120, 3, 15, 4, "Side"),
        ("Mithun Curry", "Mithun Meat, Ginger, Chillies", 450, 32, 10, 28, "Dinner"),
        ("Etting", "Fermented Bamboo Shoot, Spices", 90, 2, 10, 3, "Side"),
        ("Chicken Ngathu", "Chicken, King Chilli, Bamboo Shoot", 360, 26, 8, 22, "Dinner"),
        ("Millet Porridge", "Millet, Milk, Jaggery", 300, 6, 50, 8, "Breakfast"),
        ("Smoked Fish Fry", "Fish, Spices, Smoke Flavor", 270, 19, 5, 18, "Dinner"),
        ("Tapyo", "Dried Fish, Chillies, Salt", 110, 8, 2, 6, "Side"),
        ("Pork Anishi", "Pork, Fermented Yam Leaves, Spices", 400, 25, 6, 28, "Dinner"),
        ("Rice Porridge", "Rice, Ginger, Local Herbs", 220, 4, 40, 3, "Breakfast"),
        ("Goat Stew", "Goat Meat, Spices, Bamboo Shoot", 380, 30, 8, 25, "Dinner")
    ],
    "Assam": [
        ("Masor Tenga", "Fish, Tomatoes, Lemon, Spices", 200, 15, 10, 12, "Dinner"),
        ("Aloo Pitika", "Potatoes, Mustard Oil, Onions, Chillies", 150, 3, 25, 5, "Side"),
        ("Pitha", "Rice Flour, Coconut, Jaggery", 300, 4, 50, 8, "Snack"),
        ("Duck Curry", "Duck, Spices, Onions, Garlic", 400, 28, 10, 25, "Dinner"),
        ("Khar", "Raw Papaya, Pulses, Spices", 150, 5, 20, 3, "Side"),
        ("Bamboo Shoot Curry", "Bamboo Shoot, Spices, Ginger", 100, 2, 15, 3, "Side"),
        ("Pork with Bamboo", "Pork, Bamboo Shoot, Chillies", 350, 22, 5, 25, "Dinner"),
        ("Jolpan", "Rice, Curd, Jaggery", 250, 5, 40, 5, "Breakfast"),
        ("Chicken with Banana Flower", "Chicken, Banana Flower, Spices", 300, 20, 10, 15, "Dinner"),
        ("Fish Fry", "Fish, Spices, Mustard Oil", 200, 15, 5, 12, "Dinner"),
        ("Bilahi Maas", "Fish, Tomatoes, Turmeric, Spices", 220, 16, 8, 12, "Dinner"),
        ("Koldil Bhaji", "Banana Flower, Spices, Mustard Oil", 140, 3, 18, 6, "Side"),
        ("Narzi", "Rice, Pork, Local Herbs", 380, 20, 50, 15, "Lunch"),
        ("Ou Tenga", "Elephant Apple, Spices, Lentils", 130, 4, 20, 2, "Side"),
        ("Pani Pitha", "Rice Flour, Water, Jaggery", 280, 4, 45, 8, "Snack"),
        ("Tilor Laru", "Sesame Seeds, Jaggery", 350, 6, 50, 12, "Snack"),
        ("Mati Mahor Dal", "Black Lentils, Spices, Ginger", 160, 7, 22, 3, "Side"),
        ("Kumura Aloo", "Sweet Potato, Mustard Oil, Spices", 180, 3, 30, 5, "Side"),
        ("Bora Saul", "Sticky Rice, Milk, Sugar", 320, 6, 55, 8, "Snack"),
        ("Goat Curry", "Goat Meat, Spices, Onions", 420, 30, 10, 28, "Dinner"),
        ("Lai Xaak", "Mustard Greens, Garlic, Spices", 120, 3, 15, 4, "Side"),
        ("Misa Maas", "Prawns, Spices, Bamboo Shoot", 260, 20, 6, 16, "Dinner"),
        ("Sunga Pitha", "Rice Flour, Coconut, Spices", 300, 5, 50, 8, "Snack"),
        ("Kon Bilahi Chutney", "Roasted Tomato, Chillies, Garlic", 100, 2, 12, 4, "Side"),
        ("Chicken Tenga", "Chicken, Lemon, Spices", 340, 25, 8, 20, "Dinner"),
        ("Posola Bhaji", "Banana Stem, Spices, Oil", 150, 3, 20, 5, "Side"),
        ("Khorisa", "Fermented Bamboo Shoot, Chillies", 90, 2, 10, 3, "Side"),
        ("Duck Roast", "Duck, Spices, Mustard Oil", 450, 30, 5, 32, "Dinner"),
        ("Guti Aloo", "Baby Potatoes, Spices, Oil", 170, 3, 25, 6, "Side"),
        ("Kumol Saul", "Soft Rice, Curd, Spices", 250, 5, 45, 5, "Breakfast")
    ],
    "Bihar": [
        ("Litti Chokha", "Wheat Flour, Brinjal, Tomatoes, Spices", 400, 10, 60, 12, "Lunch"),
        ("Sattu Paratha", "Wheat Flour, Sattu, Spices", 350, 12, 50, 10, "Breakfast"),
        ("Chana Ghugni", "Chickpeas, Onions, Spices", 200, 8, 30, 5, "Snack"),
        ("Bihari Kebab", "Mutton, Spices, Yogurt", 450, 30, 5, 30, "Dinner"),
        ("Dal Puri", "Wheat Flour, Lentils, Spices", 300, 10, 45, 8, "Lunch"),
        ("Thekua", "Wheat Flour, Jaggery, Ghee", 400, 5, 60, 15, "Snack"),
        ("Khichdi", "Rice, Lentils, Spices", 250, 8, 40, 5, "Lunch"),
        ("Fish Curry", "Fish, Mustard, Spices", 300, 20, 10, 15, "Dinner"),
        ("Mutton Curry", "Mutton, Onions, Spices", 400, 28, 10, 25, "Dinner"),
        ("Pua", "Wheat Flour, Milk, Sugar", 350, 6, 50, 12, "Snack")
    ],
    "Chattisgarh": [
        ("Chila", "Rice Flour, Urad Dal, Spices", 200, 6, 30, 5, "Breakfast"),
        ("Fara", "Rice Flour, Lentils, Spices", 250, 8, 40, 5, "Snack"),
        ("Bafauri", "Chana Dal, Spices, Ginger", 150, 6, 20, 3, "Snack"),
        ("Muthia", "Rice Flour, Vegetables, Spices", 200, 4, 30, 5, "Side"),
        ("Dehrori", "Rice Flour, Milk, Sugar", 400, 5, 60, 15, "Snack"),
        ("Aamat", "Bamboo Shoot, Lentils, Spices", 150, 5, 20, 3, "Side"),
        ("Bore Baasi", "Rice, Curd, Spices", 200, 4, 35, 5, "Breakfast"),
        ("Angakar Roti", "Rice Flour, Spices", 250, 5, 40, 5, "Breakfast"),
        ("Petha", "Rice Flour, Jaggery, Ghee", 350, 4, 50, 12, "Snack"),
        ("Red Ant Chutney", "Red Ants, Chillies, Garlic", 50, 2, 5, 2, "Side")
    ],
    "Goa": [
        ("Fish Curry", "Fish, Coconut, Tamarind, Spices", 300, 20, 10, 15, "Dinner"),
        ("Prawn Balchao", "Prawns, Vinegar, Spices", 250, 18, 5, 15, "Dinner"),
        ("Chicken Xacuti", "Chicken, Coconut, Spices", 400, 25, 10, 20, "Dinner"),
        ("Bebinca", "Coconut Milk, Flour, Sugar, Eggs", 500, 8, 70, 20, "Snack"),
        ("Pork Vindaloo", "Pork, Vinegar, Spices", 450, 28, 10, 30, "Dinner"),
        ("Sannas", "Rice, Coconut, Yeast", 200, 4, 35, 5, "Breakfast"),
        ("Goan Pao", "Wheat Flour, Yeast", 150, 5, 25, 2, "Breakfast"),
        ("Sorpotel", "Pork, Liver, Vinegar, Spices", 400, 25, 10, 25, "Dinner"),
        ("Fish Recheado", "Fish, Red Chillies, Spices", 300, 20, 5, 15, "Dinner"),
        ("Prawn Rissóis", "Prawns, Flour, Spices", 250, 15, 20, 10, "Snack")
    ],
    "Gujarat": [
        ("Dhokla", "Gram Flour, Yogurt, Spices", 150, 6, 20, 5, "Breakfast"),
        ("Thepla", "Wheat Flour, Fenugreek, Spices", 200, 6, 30, 5, "Breakfast"),
        ("Undhiyu", "Mixed Vegetables, Spices, Coconut", 300, 8, 40, 10, "Lunch"),
        ("Khandvi", "Gram Flour, Yogurt, Spices", 100, 4, 15, 3, "Snack"),
        ("Fafda", "Gram Flour, Spices, Oil", 200, 5, 25, 8, "Snack"),
        ("Jalebi", "Wheat Flour, Sugar Syrup", 400, 3, 60, 15, "Snack"),
        ("Gujarati Kadhi", "Yogurt, Gram Flour, Spices", 150, 4, 20, 5, "Side"),
        ("Shrikhand", "Yogurt, Sugar, Saffron", 300, 8, 40, 10, "Snack"),
        ("Patra", "Colocasia Leaves, Gram Flour, Spices", 200, 5, 25, 8, "Snack"),
        ("Khichu", "Rice Flour, Spices, Oil", 150, 3, 25, 3, "Snack")
    ],
    "Haryana": [
        ("Bajra Khichdi", "Pearl Millet, Lentils, Spices", 300, 10, 50, 5, "Lunch"),
        ("Kachri Ki Sabzi", "Kachri, Spices, Oil", 150, 2, 20, 5, "Side"),
        ("Hara Cholia", "Green Chickpeas, Spices", 200, 8, 30, 5, "Side"),
        ("Rabri", "Milk, Sugar, Nuts", 400, 10, 50, 15, "Snack"),
        ("Gajar Ka Halwa", "Carrots, Milk, Sugar, Ghee", 500, 8, 60, 20, "Snack"),
        ("Kadhi Pakora", "Yogurt, Gram Flour, Spices", 200, 6, 25, 8, "Lunch"),
        ("Methi Gajar", "Fenugreek, Carrots, Spices", 150, 3, 20, 5, "Side"),
        ("Aloo Paratha", "Wheat Flour, Potatoes, Spices", 350, 8, 50, 10, "Breakfast"),
        ("Lassi", "Yogurt, Sugar, Water", 200, 6, 30, 5, "Snack"),
        ("Churma", "Wheat Flour, Jaggery, Ghee", 400, 6, 60, 15, "Snack")
    ],
    "Himachal Pradesh": [
        ("Dham", "Rice, Lentils, Yogurt, Spices", 400, 10, 60, 10, "Lunch"),
        ("Siddu", "Wheat Flour, Yeast, Spices", 300, 8, 50, 5, "Breakfast"),
        ("Chha Gosht", "Mutton, Yogurt, Spices", 450, 30, 10, 30, "Dinner"),
        ("Babru", "Wheat Flour, Black Gram, Spices", 250, 8, 40, 5, "Breakfast"),
        ("Kullu Trout", "Fish, Spices, Lemon", 300, 20, 5, 15, "Dinner"),
        ("Madra", "Chickpeas, Yogurt, Spices", 200, 8, 30, 5, "Lunch"),
        ("Bhey", "Lotus Stem, Spices, Oil", 150, 3, 20, 5, "Side"),
        ("Aktori", "Buckwheat Flour, Spices", 200, 5, 35, 3, "Breakfast"),
        ("Patande", "Wheat Flour, Milk, Sugar", 350, 6, 50, 12, "Snack"),
        ("Sepu Badi", "Urad Dal, Spices, Yogurt", 200, 8, 25, 5, "Side")
    ],
    "Jharkhand": [
        ("Dhuska", "Rice, Urad Dal, Spices", 200, 6, 30, 5, "Breakfast"),
        ("Rugda", "Mushrooms, Spices, Oil", 150, 5, 15, 5, "Side"),
        ("Chilka Roti", "Rice Flour, Spices", 200, 4, 35, 3, "Breakfast"),
        ("Handia", "Rice, Fermented Herbs", 150, 2, 30, 0, "Snack"),
        ("Litti", "Wheat Flour, Sattu, Spices", 400, 10, 60, 12, "Lunch"),
        ("Pitha", "Rice Flour, Jaggery, Coconut", 300, 4, 50, 8, "Snack"),
        ("Bamboo Shoot Sabzi", "Bamboo Shoot, Spices", 100, 2, 15, 3, "Side"),
        ("Chicken Curry", "Chicken, Spices, Onions", 350, 25, 10, 20, "Dinner"),
        ("Fish Curry", "Fish, Mustard, Spices", 300, 20, 10, 15, "Dinner"),
        ("Thekua", "Wheat Flour, Jaggery, Ghee", 400, 5, 60, 15, "Snack")
    ],
    "Karnataka": [
        ("Bisi Bele Bath", "Rice, Lentils, Vegetables, Spices", 400, 10, 60, 10, "Lunch"),
        ("Ragi Mudde", "Ragi Flour, Water", 150, 4, 30, 2, "Lunch"),
        ("Mysore Pak", "Gram Flour, Sugar, Ghee", 500, 5, 70, 20, "Snack"),
        ("Dosa", "Rice, Urad Dal, Spices", 200, 6, 30, 5, "Breakfast"),
        ("Chicken Sukka", "Chicken, Coconut, Spices", 350, 25, 10, 20, "Dinner"),
        ("Obbattu", "Wheat Flour, Jaggery, Lentils", 400, 8, 60, 12, "Snack"),
        ("Kesari Bath", "Semolina, Sugar, Ghee, Saffron", 450, 6, 70, 15, "Snack"),
        ("Maddur Vada", "Rice Flour, Semolina, Spices", 200, 5, 25, 8, "Snack"),
        ("Kori Gassi", "Chicken, Coconut, Spices", 400, 25, 10, 20, "Dinner"),
        ("Akki Roti", "Rice Flour, Spices, Vegetables", 200, 4, 35, 5, "Breakfast")
    ],
    "Kerala": [
        ("Appam", "Rice, Coconut, Yeast", 200, 4, 35, 5, "Breakfast"),
        ("Fish Molee", "Fish, Coconut Milk, Spices", 300, 20, 10, 15, "Dinner"),
        ("Puttu", "Rice Flour, Coconut", 150, 3, 25, 3, "Breakfast"),
        ("Beef Fry", "Beef, Coconut, Spices", 400, 30, 5, 25, "Dinner"),
        ("Sadya", "Rice, Mixed Vegetables, Spices", 500, 10, 80, 10, "Lunch"),
        ("Kerala Parotta", "Wheat Flour, Oil", 300, 6, 50, 8, "Dinner"),
        ("Prawn Curry", "Prawns, Coconut, Spices", 350, 22, 10, 20, "Dinner"),
        ("Banana Chips", "Banana, Coconut Oil", 200, 2, 30, 8, "Snack"),
        ("Thalassery Biryani", "Rice, Chicken, Spices", 600, 25, 80, 20, "Lunch"),
        ("Jackfruit Payasam", "Jackfruit, Coconut Milk, Jaggery", 400, 5, 60, 12, "Snack")  # Using seasonal jackfruit
    ],
    "Madya Pradesh": [
        ("Poha", "Flattened Rice, Peanuts, Spices", 200, 4, 35, 5, "Breakfast"),
        ("Bhutte Ka Kees", "Corn, Milk, Spices", 250, 5, 40, 8, "Snack"),
        ("Dal Bafla", "Wheat Flour, Lentils, Spices", 400, 10, 60, 10, "Lunch"),
        ("Kusli", "Wheat Flour, Jaggery, Coconut", 350, 6, 50, 12, "Snack"),
        ("Mawa Bati", "Milk Solids, Sugar, Ghee", 500, 8, 60, 20, "Snack"),
        ("Palak Puri", "Wheat Flour, Spinach, Spices", 300, 8, 45, 8, "Breakfast"),
        ("Bhutte Ki Sabzi", "Corn, Spices, Oil", 200, 4, 30, 5, "Side"),
        ("Chicken Korma", "Chicken, Yogurt, Spices", 400, 25, 10, 20, "Dinner"),
        ("Jalebi", "Wheat Flour, Sugar Syrup", 400, 3, 60, 15, "Snack"),
        ("Sabudana Khichdi", "Sago, Peanuts, Spices", 250, 4, 40, 8, "Breakfast")
    ],
    "Maharastra": [
        ("Pav Bhaji", "Mixed Vegetables, Spices, Butter", 400, 8, 60, 12, "Dinner"),
        ("Vada Pav", "Potatoes, Gram Flour, Spices", 300, 6, 45, 10, "Snack"),
        ("Misal Pav", "Sprouts, Spices, Farsan", 350, 10, 50, 10, "Breakfast"),
        ("Puran Poli", "Wheat Flour, Jaggery, Lentils", 400, 8, 60, 12, "Snack"),
        ("Bharli Vangi", "Brinjal, Peanuts, Spices", 200, 4, 25, 8, "Side"),
        ("Kothimbir Vadi", "Gram Flour, Coriander, Spices", 150, 5, 20, 5, "Snack"),
        ("Modak", "Rice Flour, Coconut, Jaggery", 300, 4, 50, 8, "Snack"),
        ("Chicken Kolhapuri", "Chicken, Spices, Coconut", 400, 25, 10, 20, "Dinner"),
        ("Sabudana Vada", "Sago, Peanuts, Spices", 250, 5, 35, 8, "Snack"),
        ("Prawn Masala", "Prawns, Spices, Coconut", 350, 22, 10, 20, "Dinner")
    ],
    "Manipur": [
        ("Eromba", "Vegetables, Fermented Fish, Chillies", 150, 5, 15, 5, "Side"),
        ("Chak-hao Kheer", "Black Rice, Milk, Sugar", 400, 6, 60, 12, "Snack"),
        ("Kangshoi", "Vegetables, Spices, Ginger", 100, 3, 15, 2, "Side"),
        ("Singju", "Vegetables, Fermented Fish, Chillies", 150, 4, 15, 5, "Side"),
        ("Chicken Curry", "Chicken, Spices, Bamboo Shoot", 350, 25, 10, 20, "Dinner"),
        ("Fish Stew", "Fish, Spices, Herbs", 300, 20, 10, 15, "Dinner"),
        ("Pork with Bamboo", "Pork, Bamboo Shoot, Chillies", 400, 25, 5, 30, "Dinner"),
        ("Iromba", "Potatoes, Fermented Fish, Chillies", 150, 4, 20, 5, "Side"),
        ("Ngari", "Fermented Fish, Chillies", 50, 5, 0, 2, "Side"),
        ("Thongba", "Fish, Spices, Ginger", 250, 18, 10, 12, "Dinner")
    ],
    "Meghalaya": [
        ("Jadoh", "Rice, Pork, Spices", 400, 20, 50, 15, "Lunch"),
        ("Dohneiiong", "Pork, Black Sesame, Spices", 450, 25, 5, 30, "Dinner"),
        ("Nakham Bitchi", "Dried Fish, Chillies, Spices", 100, 8, 5, 5, "Side"),
        ("Pumaloi", "Rice Flour, Spices", 200, 4, 35, 3, "Breakfast"),
        ("Tungrymbai", "Fermented Soybeans, Spices", 150, 8, 15, 5, "Side"),
        ("Chicken with Bamboo", "Chicken, Bamboo Shoot, Spices", 350, 22, 10, 20, "Dinner"),
        ("Pork with Bamboo", "Pork, Bamboo Shoot, Chillies", 400, 25, 5, 30, "Dinner"),
        ("Fish Fry", "Fish, Spices, Oil", 300, 20, 5, 15, "Dinner"),
        ("Kyat", "Rice, Fermented Yeast", 150, 2, 30, 0, "Snack"),
        ("Pukhlein", "Rice Flour, Jaggery", 300, 4, 50, 8, "Snack")
    ],
    "Mizoram": [
        ("Bai", "Vegetables, Pork, Spices", 300, 15, 20, 15, "Lunch"),
        ("Vawksa Rep", "Pork, Spices, Ginger", 400, 25, 5, 30, "Dinner"),
        ("Misa Mach Poora", "Prawns, Spices, Banana Leaf", 250, 18, 5, 15, "Dinner"),
        ("Chhum Han", "Vegetables, Spices, Bamboo Shoot", 150, 3, 20, 3, "Side"),
        ("Koat Pitha", "Rice Flour, Banana, Jaggery", 300, 4, 50, 8, "Snack"),
        ("Fish Stew", "Fish, Spices, Herbs", 250, 18, 10, 12, "Dinner"),
        ("Chicken with Bamboo", "Chicken, Bamboo Shoot, Spices", 350, 22, 10, 20, "Dinner"),
        ("Pork with Bamboo", "Pork, Bamboo Shoot, Chillies", 400, 25, 5, 30, "Dinner"),
        ("Sawhchiar", "Rice, Chicken, Spices", 400, 20, 50, 15, "Lunch"),
        ("Mizo Dal", "Lentils, Spices, Ginger", 150, 6, 20, 3, "Side")
    ],
    "Nagaland": [
        ("Pork with Bamboo", "Pork, Bamboo Shoot, Chillies", 400, 25, 5, 30, "Dinner"),
        ("Axone", "Fermented Soybeans, Spices", 150, 8, 15, 5, "Side"),
        ("Smoked Pork", "Pork, Spices, Smoke", 450, 28, 5, 30, "Dinner"),
        ("Fish in Bamboo", "Fish, Spices, Bamboo Shoot", 300, 20, 5, 15, "Dinner"),
        ("Chicken with Anishi", "Chicken, Fermented Yam Leaves, Spices", 350, 22, 10, 20, "Dinner"),
        ("Galho", "Rice, Vegetables, Spices", 200, 4, 35, 5, "Lunch"),
        ("Naga King Chilli Chutney", "King Chilli, Garlic, Spices", 50, 1, 5, 2, "Side"),
        ("Pork with Dry Bamboo", "Pork, Dry Bamboo Shoot, Spices", 400, 25, 5, 30, "Dinner"),
        ("Zutho", "Rice, Fermented Yeast", 150, 2, 30, 0, "Snack"),
        ("Vegetable Stew", "Mixed Vegetables, Spices", 150, 3, 20, 3, "Side")
    ],
    "Odisha": [
        ("Pakhala Bhata", "Fermented Rice, Water, Spices", 200, 4, 35, 3, "Lunch"),
        ("Dalma", "Lentils, Mixed Vegetables, Spices", 250, 8, 40, 5, "Lunch"),
        ("Chhencheda", "Fish, Spices, Tamarind", 300, 20, 10, 15, "Dinner"),
        ("Rasabali", "Milk, Sugar, Spices", 400, 8, 50, 15, "Snack"),
        ("Chhena Poda", "Cheese, Sugar, Cardamom", 450, 10, 60, 15, "Snack"),
        ("Pitha", "Rice Flour, Jaggery, Coconut", 300, 4, 50, 8, "Snack"),
        ("Mutton Jholo", "Mutton, Spices, Onions", 400, 28, 10, 25, "Dinner"),
        ("Crab Curry", "Crab, Spices, Coconut", 350, 22, 10, 20, "Dinner"),
        ("Badi Chura", "Sun-Dried Lentil Dumplings, Spices", 150, 6, 20, 3, "Side"),
        ("Khicede", "Rice, Lentils, Spices", 250, 8, 40, 5, "Lunch")
    ],
    "Punjab": [
        ("Makki Di Roti", "Corn Flour, Spices", 200, 5, 35, 5, "Lunch"),
        ("Sarson Da Saag", "Mustard Greens, Spinach, Spices", 150, 5, 15, 8, "Lunch"),  # Using seasonal mustard greens
        ("Butter Chicken", "Chicken, Butter, Cream, Spices", 500, 30, 20, 30, "Dinner"),
        ("Amritsari Kulcha", "Wheat Flour, Potatoes, Spices", 300, 8, 45, 8, "Breakfast"),
        ("Chole Bhature", "Chickpeas, Wheat Flour, Spices", 450, 12, 60, 15, "Lunch"),
        ("Lassi", "Yogurt, Sugar, Water", 200, 6, 30, 5, "Snack"),
        ("Tandoori Chicken", "Chicken, Yogurt, Spices", 400, 28, 5, 25, "Dinner"),
        ("Pinni", "Wheat Flour, Jaggery, Ghee", 500, 6, 70, 20, "Snack"),
        ("Aloo Paratha", "Wheat Flour, Potatoes, Spices", 350, 8, 50, 10, "Breakfast"),
        ("Gajar Ka Halwa", "Carrots, Milk, Sugar, Ghee", 500, 8, 60, 20, "Snack")  # Using seasonal carrots
    ],
    "Rajasthan": [
        ("Dal Baati Churma", "Wheat Flour, Lentils, Ghee", 500, 12, 70, 15, "Lunch"),
        ("Laal Maas", "Mutton, Red Chillies, Spices", 450, 30, 10, 30, "Dinner"),
        ("Gatte Ki Sabzi", "Gram Flour, Spices, Yogurt", 200, 8, 25, 8, "Lunch"),
        ("Ker Sangri", "Dried Berries, Beans, Spices", 150, 4, 20, 5, "Side"),
        ("Bajre Ki Roti", "Pearl Millet, Spices", 200, 5, 35, 5, "Lunch"),
        ("Mohanthal", "Gram Flour, Sugar, Ghee", 500, 6, 70, 20, "Snack"),
        ("Pyaaz Kachori", "Wheat Flour, Onions, Spices", 300, 6, 45, 10, "Snack"),
        ("Mirchi Bada", "Green Chillies, Gram Flour, Spices", 150, 3, 20, 5, "Snack"),
        ("Rabdi", "Milk, Sugar, Nuts", 400, 8, 50, 15, "Snack"),
        ("Ghevar", "Wheat Flour, Sugar Syrup, Ghee", 450, 6, 60, 20, "Snack")
    ],
    "Sikkim": [
        ("Momo", "Wheat Flour, Pork, Spices", 300, 15, 40, 10, "Snack"),
        ("Thukpa", "Noodles, Vegetables, Spices", 250, 8, 40, 5, "Lunch"),
        ("Gundruk", "Fermented Greens, Spices", 100, 3, 15, 2, "Side"),
        ("Sael Roti", "Rice Flour, Spices, Oil", 200, 4, 35, 5, "Breakfast"),
        ("Phagshapa", "Pork, Radish, Spices", 400, 25, 10, 25, "Dinner"),
        ("Chhurpi Soup", "Chhurpi Cheese, Spices", 150, 6, 15, 5, "Side"),
        ("Chicken Thukpa", "Noodles, Chicken, Spices", 300, 15, 40, 10, "Lunch"),
        ("Sha Phaley", "Wheat Flour, Meat, Spices", 350, 15, 45, 12, "Snack"),
        ("Sinki Soup", "Fermented Radish, Spices", 100, 3, 15, 2, "Side"),
        ("Chang", "Millet, Fermented Yeast", 150, 2, 30, 0, "Snack")
    ],
    "Tamil Nadu": [
        ("Dosa", "Rice, Urad Dal, Fenugreek Seeds, Salt", 200, 6, 30, 5, "Breakfast"),
        ("Idli", "Rice, Urad Dal, Fenugreek Seeds, Salt", 150, 5, 25, 3, "Breakfast"),
        ("Sambar", "Toor Dal, Tamarind, Tomatoes, Drumsticks, Turmeric, Coriander", 150, 6, 20, 3, "Side"),
        ("Rasam", "Tomatoes, Tamarind, Black Pepper, Cumin, Garlic", 100, 2, 15, 2, "Side"),
        ("Pongal", "Rice, Moong Dal, Black Pepper, Cumin, Ghee", 250, 8, 40, 6, "Breakfast"),
        ("Chicken Chettinad", "Chicken, Coconut, Fennel Seeds, Star Anise, Red Chillies", 400, 25, 10, 20, "Dinner"),
        ("Vada", "Urad Dal, Black Pepper, Curry Leaves, Oil", 200, 6, 25, 8, "Snack"),
        ("Mango Pachadi", "Raw Mango, Jaggery, Red Chillies, Mustard Seeds", 150, 2, 30, 3, "Side"),  # Using seasonal mango
        ("Fish Kuzhambu", "Fish, Tamarind, Shallots, Red Chillies, Fenugreek", 300, 20, 10, 15, "Dinner"),
        ("Kothu Parotta", "Wheat Flour, Onions, Tomatoes, Green Chillies, Eggs", 350, 10, 50, 10, "Dinner")
    ],
    "Telangana": [
        ("Hyderabadi Biryani", "Rice, Chicken, Spices, Saffron", 600, 25, 80, 20, "Lunch"),
        ("Pachi Pulusu", "Tamarind, Onions, Spices", 100, 2, 15, 2, "Side"),
        ("Sakinalu", "Rice Flour, Sesame Seeds, Spices", 200, 4, 30, 5, "Snack"),
        ("Garelu", "Urad Dal, Spices, Oil", 200, 6, 25, 8, "Snack"),
        ("Qubani Ka Meetha", "Apricots, Sugar, Nuts", 400, 4, 60, 12, "Snack"),
        ("Pappu Charu", "Lentils, Tamarind, Spices", 150, 6, 20, 3, "Side"),
        ("Chicken 65", "Chicken, Spices, Yogurt", 350, 25, 10, 20, "Dinner"),
        ("Pesarattu", "Green Gram, Rice, Spices", 200, 8, 30, 5, "Breakfast"),
        ("Mutton Curry", "Mutton, Spices, Onions", 400, 28, 10, 25, "Dinner"),
        ("Jonna Rotte", "Sorghum Flour, Spices", 200, 5, 35, 5, "Breakfast")
    ],
    "Tripura": [
        ("Mui Borok", "Vegetables, Bamboo Shoot, Spices", 150, 3, 20, 3, "Side"),
        ("Awan Bangwi", "Rice, Vegetables, Spices", 200, 4, 35, 5, "Lunch"),
        ("Pork with Bamboo", "Pork, Bamboo Shoot, Chillies", 400, 25, 5, 30, "Dinner"),
        ("Fish Stew", "Fish, Spices, Herbs", 300, 20, 10, 15, "Dinner"),
        ("Chicken Curry", "Chicken, Spices, Ginger", 350, 22, 10, 20, "Dinner"),
        ("Chakhwi", "Vegetables, Spices, Bamboo Shoot", 150, 3, 20, 3, "Side"),
        ("Mosdeng Serma", "Vegetables, Chillies, Spices", 100, 2, 15, 2, "Side"),
        ("Berma", "Fermented Fish, Chillies", 50, 5, 0, 2, "Side"),
        ("Wahan", "Pork, Spices, Ginger", 400, 25, 5, 30, "Dinner"),
        ("Gudok", "Vegetables, Spices, Fish", 200, 10, 20, 8, "Lunch")
    ],
    "Uttar Pradesh": [
        ("Aloo Kachori", "Wheat Flour, Potatoes, Spices", 300, 6, 45, 10, "Snack"),
        ("Tunday Kebab", "Mutton, Spices, Yogurt", 450, 30, 5, 30, "Dinner"),
        ("Puri Sabzi", "Wheat Flour, Potatoes, Spices", 350, 8, 50, 10, "Breakfast"),
        ("Kheer", "Rice, Milk, Sugar, Nuts", 400, 8, 60, 12, "Snack"),
        ("Biryani", "Rice, Chicken, Spices", 600, 25, 80, 20, "Lunch"),
        ("Mathura Peda", "Milk Solids, Sugar, Ghee", 500, 8, 60, 20, "Snack"),
        ("Chaat", "Potatoes, Chickpeas, Spices", 200, 5, 30, 5, "Snack"),
        ("Shahi Tukda", "Bread, Milk, Sugar, Nuts", 450, 8, 60, 15, "Snack"),
        ("Mutton Korma", "Mutton, Yogurt, Spices", 400, 28, 10, 25, "Dinner"),
        ("Baingan Bharta", "Brinjal, Spices, Oil", 150, 3, 20, 5, "Side")
    ],
    "Uttarakhand": [
        ("Kafuli", "Spinach, Fenugreek, Spices", 150, 4, 20, 5, "Side"),
        ("Aloo Ke Gutke", "Potatoes, Spices, Oil", 200, 4, 30, 5, "Side"),
        ("Bal Mithai", "Milk Solids, Sugar, Chocolate", 500, 8, 60, 20, "Snack"),
        ("Chainsoo", "Urad Dal, Spices", 200, 8, 25, 5, "Side"),
        ("Kumaoni Raita", "Cucumber, Yogurt, Spices", 100, 3, 15, 3, "Side"),
        ("Jhangora Ki Kheer", "Millet, Milk, Sugar", 400, 6, 60, 12, "Snack"),
        ("Bhatwani", "Black Soybean, Spices", 200, 8, 25, 5, "Side"),
        ("Gahat Ki Dal", "Horse Gram, Spices", 150, 6, 20, 3, "Side"),
        ("Mandua Ki Roti", "Finger Millet, Spices", 200, 5, 35, 5, "Breakfast"),
        ("Pahadi Chicken", "Chicken, Spices, Yogurt", 350, 25, 10, 20, "Dinner")
    ],
    "West Bengal": [
        ("Rasgulla", "Cheese, Sugar Syrup", 400, 8, 60, 12, "Snack"),
        ("Macher Jhol", "Fish, Spices, Mustard", 300, 20, 10, 15, "Dinner"),
        ("Shorshe Ilish", "Hilsa Fish, Mustard, Spices", 350, 22, 10, 20, "Dinner"),
        ("Luchi", "Wheat Flour, Oil", 200, 4, 30, 5, "Breakfast"),
        ("Aloo Posto", "Potatoes, Poppy Seeds, Spices", 200, 4, 30, 5, "Side"),
        ("Cholar Dal", "Chana Dal, Coconut, Spices", 150, 6, 20, 3, "Side"),
        ("Panta Bhat", "Fermented Rice, Spices", 200, 4, 35, 3, "Breakfast"),
        ("Chicken Bharta", "Chicken, Spices, Yogurt", 400, 25, 10, 20, "Dinner"),
        ("Sandesh", "Cheese, Sugar, Cardamom", 400, 8, 60, 12, "Snack"),
        ("Mishti Doi", "Yogurt, Sugar, Milk", 300, 6, 40, 10, "Snack")
    ]
}

# Seasonal fruits and vegetables for each state
STATE_SEASONAL_PRODUCE = {
    "Andhra Pradesh": {
        "Summer": {"Fruits": ["Mango", "Watermelon", "Muskmelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Pear", "Plum"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Custard Apple", "Pomegranate"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Papaya", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Arunachal Pradesh": {
        "Summer": {"Fruits": ["Pineapple", "Mango", "Litchi"], "Vegetables": ["Cucumber", "Bamboo Shoot", "Okra"]},
        "Monsoon": {"Fruits": ["Jackfruit", "Plum", "Peach"], "Vegetables": ["Fern Leaves", "Colocasia", "Corn"]},
        "Autumn": {"Fruits": ["Orange", "Kiwi", "Pomegranate"], "Vegetables": ["Pumpkin", "Brinjal", "Radish"]},
        "Winter": {"Fruits": ["Apple", "Banana", "Grapes"], "Vegetables": ["Cabbage", "Cauliflower", "Mustard Greens"]}
    },
    "Assam": {
        "Summer": {"Fruits": ["Mango", "Litchi", "Pineapple"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jackfruit", "Jamun", "Plum"], "Vegetables": ["Bamboo Shoot", "Colocasia", "Fern Leaves"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Radish"]},
        "Winter": {"Fruits": ["Orange", "Banana", "Papaya"], "Vegetables": ["Cabbage", "Cauliflower", "Peas"]}
    },
    "Bihar": {
        "Summer": {"Fruits": ["Mango", "Litchi", "Watermelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pear"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Banana", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Chattisgarh": {
        "Summer": {"Fruits": ["Mango", "Watermelon", "Muskmelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Jackfruit"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Papaya", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Goa": {
        "Summer": {"Fruits": ["Mango", "Jackfruit", "Cashew Apple"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pineapple"], "Vegetables": ["Colocasia", "Yam", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Custard Apple", "Pomegranate"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Banana", "Papaya", "Orange"], "Vegetables": ["Cabbage", "Cauliflower", "Peas"]}
    },
    "Gujarat": {
        "Summer": {"Fruits": ["Mango", "Watermelon", "Muskmelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pear"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Chikoo", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Haryana": {
        "Summer": {"Fruits": ["Mango", "Watermelon", "Muskmelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pear"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Kinnow", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Himachal Pradesh": {
        "Summer": {"Fruits": ["Mango", "Litchi", "Peach"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Plum", "Pear", "Apple"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Apple", "Pomegranate", "Kiwi"], "Vegetables": ["Pumpkin", "Brinjal", "Radish"]},
        "Winter": {"Fruits": ["Orange", "Kinnow", "Grapes"], "Vegetables": ["Cabbage", "Cauliflower", "Peas"]}
    },
    "Jharkhand": {
        "Summer": {"Fruits": ["Mango", "Litchi", "Watermelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Jackfruit"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Papaya", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Karnataka": {
        "Summer": {"Fruits": ["Mango", "Jackfruit", "Watermelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pineapple"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Custard Apple", "Pomegranate"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Chikoo", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Kerala": {
        "Summer": {"Fruits": ["Mango", "Jackfruit", "Pineapple"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Banana", "Papaya", "Rambutan"], "Vegetables": ["Colocasia", "Yam", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Custard Apple", "Pomegranate"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Banana", "Orange", "Grapes"], "Vegetables": ["Cabbage", "Cauliflower", "Peas"]}
    },
    "Madya Pradesh": {
        "Summer": {"Fruits": ["Mango", "Watermelon", "Muskmelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pear"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Chikoo", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Maharashta": {
        "Summer": {"Fruits": ["Mango", "Watermelon", "Muskmelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pear"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Chikoo", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Manipur": {
        "Summer": {"Fruits": ["Mango", "Pineapple", "Litchi"], "Vegetables": ["Cucumber", "Bamboo Shoot", "Okra"]},
        "Monsoon": {"Fruits": ["Jackfruit", "Plum", "Peach"], "Vegetables": ["Fern Leaves", "Colocasia", "Corn"]},
        "Autumn": {"Fruits": ["Orange", "Pomegranate", "Guava"], "Vegetables": ["Pumpkin", "Brinjal", "Radish"]},
        "Winter": {"Fruits": ["Banana", "Orange", "Grapes"], "Vegetables": ["Cabbage", "Cauliflower", "Mustard Greens"]}
    },
    "Meghalaya": {
        "Summer": {"Fruits": ["Pineapple", "Mango", "Litchi"], "Vegetables": ["Cucumber", "Bamboo Shoot", "Okra"]},
        "Monsoon": {"Fruits": ["Jackfruit", "Plum", "Peach"], "Vegetables": ["Fern Leaves", "Colocasia", "Corn"]},
        "Autumn": {"Fruits": ["Orange", "Pomegranate", "Guava"], "Vegetables": ["Pumpkin", "Brinjal", "Radish"]},
        "Winter": {"Fruits": ["Banana", "Orange", "Grapes"], "Vegetables": ["Cabbage", "Cauliflower", "Mustard Greens"]}
    },
    "Mizoram": {
        "Summer": {"Fruits": ["Pineapple", "Mango", "Litchi"], "Vegetables": ["Cucumber", "Bamboo Shoot", "Okra"]},
        "Monsoon": {"Fruits": ["Jackfruit", "Plum", "Peach"], "Vegetables": ["Fern Leaves", "Colocasia", "Corn"]},
        "Autumn": {"Fruits": ["Orange", "Pomegranate", "Guava"], "Vegetables": ["Pumpkin", "Brinjal", "Radish"]},
        "Winter": {"Fruits": ["Banana", "Orange", "Grapes"], "Vegetables": ["Cabbage", "Cauliflower", "Mustard Greens"]}
    },
    "Nagaland": {
        "Summer": {"Fruits": ["Pineapple", "Mango", "Litchi"], "Vegetables": ["Cucumber", "Bamboo Shoot", "Okra"]},
        "Monsoon": {"Fruits": ["Jackfruit", "Plum", "Peach"], "Vegetables": ["Fern Leaves", "Colocasia", "Corn"]},
        "Autumn": {"Fruits": ["Orange", "Pomegranate", "Guava"], "Vegetables": ["Pumpkin", "Brinjal", "Radish"]},
        "Winter": {"Fruits": ["Banana", "Orange", "Grapes"], "Vegetables": ["Cabbage", "Cauliflower", "Mustard Greens"]}
    },
    "Odisha": {
        "Summer": {"Fruits": ["Mango", "Watermelon", "Jackfruit"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pineapple"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Papaya", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Punjab": {
        "Summer": {"Fruits": ["Mango", "Watermelon", "Muskmelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pear"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Kinnow", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas", "Mustard Greens"]}
    },
    "Rajasthan": {
        "Summer": {"Fruits": ["Mango", "Watermelon", "Muskmelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pear"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Kinnow", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Sikkim": {
        "Summer": {"Fruits": ["Mango", "Litchi", "Peach"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Plum", "Pear", "Apple"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Orange", "Pomegranate", "Kiwi"], "Vegetables": ["Pumpkin", "Brinjal", "Radish"]},
        "Winter": {"Fruits": ["Orange", "Apple", "Grapes"], "Vegetables": ["Cabbage", "Cauliflower", "Peas"]}
    },
    "Tamil Nadu": {
        "Summer": {"Fruits": ["Mango", "Jackfruit", "Watermelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Banana", "Papaya", "Guava"], "Vegetables": ["Colocasia", "Yam", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Custard Apple", "Pomegranate"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Banana", "Orange", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Telangana": {
        "Summer": {"Fruits": ["Mango", "Watermelon", "Muskmelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pear"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Papaya", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Tripura": {
        "Summer": {"Fruits": ["Mango", "Pineapple", "Litchi"], "Vegetables": ["Cucumber", "Bamboo Shoot", "Okra"]},
        "Monsoon": {"Fruits": ["Jackfruit", "Plum", "Peach"], "Vegetables": ["Fern Leaves", "Colocasia", "Corn"]},
        "Autumn": {"Fruits": ["Orange", "Pomegranate", "Guava"], "Vegetables": ["Pumpkin", "Brinjal", "Radish"]},
        "Winter": {"Fruits": ["Banana", "Orange", "Grapes"], "Vegetables": ["Cabbage", "Cauliflower", "Mustard Greens"]}
    },
    "Uttar Pradesh": {
        "Summer": {"Fruits": ["Mango", "Litchi", "Watermelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pear"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Kinnow", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    },
    "Uttarakhand": {
        "Summer": {"Fruits": ["Mango", "Litchi", "Peach"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Plum", "Pear", "Apple"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Apple", "Pomegranate", "Kiwi"], "Vegetables": ["Pumpkin", "Brinjal", "Radish"]},
        "Winter": {"Fruits": ["Orange", "Apple", "Grapes"], "Vegetables": ["Cabbage", "Cauliflower", "Peas"]}
    },
    "West Bengal": {
        "Summer": {"Fruits": ["Mango", "Litchi", "Watermelon"], "Vegetables": ["Cucumber", "Bottle Gourd", "Okra"]},
        "Monsoon": {"Fruits": ["Jamun", "Plum", "Pineapple"], "Vegetables": ["Bitter Gourd", "Ridge Gourd", "Corn"]},
        "Autumn": {"Fruits": ["Guava", "Pomegranate", "Custard Apple"], "Vegetables": ["Pumpkin", "Brinjal", "Green Beans"]},
        "Winter": {"Fruits": ["Orange", "Papaya", "Grapes"], "Vegetables": ["Carrot", "Cauliflower", "Peas"]}
    }
}

# List of states for easy access
STATES = list(STATE_FOODS.keys())
