"""
Food & Restaurants Topic Content

This file contains all content related to the Food & Restaurants topic.
No Django models should be imported here.

The seed_data management command will import this file
and populate the database.
"""

FOOD = {
    "topic": {
        "title": "Food & Restaurants",
        "description": "Learn English for ordering food, making reservations, asking about menu items, and dining confidently.",
        "category": "Daily Life",
        "difficulty": "A2",
        "grammar_focus": "Countable & Uncountable Nouns",
        "vocabulary_focus": "Food & Dining",
        "estimated_turns": 40,
        "icon": "🍽️",
        "display_order": 2,
        "is_active": True,
    },

    # "learning_objectives": [
    #     "Order food confidently",
    #     "Ask about menu items",
    #     "Pay the bill politely",
    # ],

    "scenarios": [
        {
            "title": "Ordering Food",
            "description": "Order a complete meal in a restaurant.",
            "ai_role": "Waiter",
            "user_role": "Customer",
            "opening_prompt": "Good evening! Welcome to our restaurant. May I take your order?",
            "learning_objective": "Order food politely and naturally.",
            "difficulty": "A2",
            "grammar_focus": "Countable & Uncountable Nouns",
            "vocabulary_focus": "Restaurant",
            "max_turns": 40,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Making a Reservation",
            "description": "Reserve a table at a restaurant.",
            "ai_role": "Restaurant Host",
            "user_role": "Customer",
            "opening_prompt": "Hello! Thank you for calling Green Garden Restaurant. How may I help you?",
            "learning_objective": "Make a restaurant reservation.",
            "difficulty": "A2",
            "grammar_focus": "Countable & Uncountable Nouns",
            "vocabulary_focus": "Reservation",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Asking About the Menu",
            "description": "Ask questions about dishes before ordering.",
            "ai_role": "Waiter",
            "user_role": "Customer",
            "opening_prompt": "Here is today's menu. Please let me know if you have any questions.",
            "learning_objective": "Understand menu items and ingredients.",
            "difficulty": "A2",
            "grammar_focus": "Countable & Uncountable Nouns",
            "vocabulary_focus": "Menu",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Paying the Bill",
            "description": "Ask for the bill and complete payment.",
            "ai_role": "Cashier",
            "user_role": "Customer",
            "opening_prompt": "I hope you enjoyed your meal. Would you like the bill now?",
            "learning_objective": "Pay for a meal politely.",
            "difficulty": "A2",
            "grammar_focus": "Countable & Uncountable Nouns",
            "vocabulary_focus": "Payment",
            "max_turns": 25,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Returning Incorrect Food",
            "description": "Politely report that you received the wrong order.",
            "ai_role": "Waiter",
            "user_role": "Customer",
            "opening_prompt": "Is everything alright with your meal?",
            "learning_objective": "Handle a restaurant problem politely.",
            "difficulty": "B1",
            "grammar_focus": "Countable & Uncountable Nouns",
            "vocabulary_focus": "Complaints",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
    ],

    "vocabulary": [
    {
      "word": "menu",
      "definition": "A list of food and drinks available in a restaurant.",
      "difficulty": "A1"
    },
    {
      "word": "reservation",
      "definition": "An arrangement to keep a table for a customer.",
      "difficulty": "A2"
    },
    {
      "word": "appetizer",
      "definition": "A small dish served before the main course.",
      "difficulty": "A2"
    },
    {
      "word": "main course",
      "definition": "The primary dish of a meal.",
      "difficulty": "A2"
    },
    {
      "word": "dessert",
      "definition": "A sweet dish served at the end of a meal.",
      "difficulty": "A1"
    },
    {
      "word": "beverage",
      "definition": "A drink.",
      "difficulty": "A2"
    },
    {
      "word": "ingredients",
      "definition": "The foods used to prepare a dish.",
      "difficulty": "A2"
    },
    {
      "word": "spicy",
      "definition": "Having a strong hot flavor.",
      "difficulty": "A1"
    },
    {
      "word": "bill",
      "definition": "The amount of money you must pay after a meal.",
      "difficulty": "A1"
    },
    {
      "word": "tip",
      "definition": "Extra money given for good service.",
      "difficulty": "A2"
    },
    {
      "word": "waiter",
      "definition": "A person who serves food in a restaurant.",
      "difficulty": "A1"
    },
    {
      "word": "customer",
      "definition": "A person buying food or services.",
      "difficulty": "A1"
    },
    {
      "word": "order",
      "definition": "A request for food or drinks.",
      "difficulty": "A1"
    },
    {
      "word": "chef",
      "definition": "A professional cook.",
      "difficulty": "A1"
    },
    {
      "word": "receipt",
      "definition": "A document showing payment.",
      "difficulty": "A2"
    },
    {
      "word": "fork",
      "definition": "A utensil with prongs used for eating.",
      "difficulty": "A1"
    },
    {
      "word": "knife",
      "definition": "A utensil used for cutting food.",
      "difficulty": "A1"
    },
    {
      "word": "plate",
      "definition": "A flat dish used for serving food.",
      "difficulty": "A1"
    },
    {
      "word": "table",
      "definition": "Furniture where people eat meals.",
      "difficulty": "A1"
    },
    {
      "word": "vegetarian",
      "definition": "A person who does not eat meat, or food suitable for them.",
      "difficulty": "A2"
    },
    {
      "word": "restaurant",
      "definition": "A place where people pay to eat meals.",
      "difficulty": "A1"
    },
    {
      "word": "host",
      "definition": "A person who welcomes guests at a restaurant.",
      "difficulty": "A2"
    },
    {
      "word": "cashier",
      "definition": "A person who receives payments.",
      "difficulty": "A2"
    },
    {
      "word": "meal",
      "definition": "Food eaten at one time.",
      "difficulty": "A1"
    },
    {
      "word": "breakfast",
      "definition": "The first meal of the day.",
      "difficulty": "A1"
    },
    {
      "word": "lunch",
      "definition": "The meal eaten in the middle of the day.",
      "difficulty": "A1"
    },
    {
      "word": "dinner",
      "definition": "The main meal of the evening.",
      "difficulty": "A1"
    },
    {
      "word": "drink",
      "definition": "A liquid for drinking.",
      "difficulty": "A1"
    },
    {
      "word": "water",
      "definition": "A clear liquid people drink.",
      "difficulty": "A1"
    },
    {
      "word": "juice",
      "definition": "A drink made from fruit.",
      "difficulty": "A1"
    },
    {
      "word": "coffee",
      "definition": "A hot drink made from roasted beans.",
      "difficulty": "A1"
    },
    {
      "word": "tea",
      "definition": "A hot drink made by steeping tea leaves.",
      "difficulty": "A1"
    },
    {
      "word": "bread",
      "definition": "A baked food made from flour.",
      "difficulty": "A1"
    },
    {
      "word": "salad",
      "definition": "A dish of mixed vegetables.",
      "difficulty": "A1"
    },
    {
      "word": "soup",
      "definition": "A liquid food served warm or cold.",
      "difficulty": "A1"
    },
    {
      "word": "rice",
      "definition": "Small grains cooked and eaten as food.",
      "difficulty": "A1"
    },
    {
      "word": "chicken",
      "definition": "Meat from a chicken.",
      "difficulty": "A1"
    },
    {
      "word": "fish",
      "definition": "An animal from water often eaten as food.",
      "difficulty": "A1"
    },
    {
      "word": "beef",
      "definition": "Meat from a cow.",
      "difficulty": "A2"
    },
    {
      "word": "pasta",
      "definition": "Food made from wheat dough.",
      "difficulty": "A1"
    },
    {
      "word": "pizza",
      "definition": "A baked flatbread topped with cheese and other ingredients.",
      "difficulty": "A1"
    },
    {
      "word": "burger",
      "definition": "A sandwich with a cooked meat or vegetable patty.",
      "difficulty": "A1"
    },
    {
      "word": "sandwich",
      "definition": "Two pieces of bread with filling.",
      "difficulty": "A1"
    },
    {
      "word": "fries",
      "definition": "Thin pieces of fried potato.",
      "difficulty": "A1"
    },
    {
      "word": "cheese",
      "definition": "A food made from milk.",
      "difficulty": "A1"
    },
    {
      "word": "egg",
      "definition": "An oval food produced by birds.",
      "difficulty": "A1"
    },
    {
      "word": "fruit",
      "definition": "The sweet edible part of a plant.",
      "difficulty": "A1"
    },
    {
      "word": "vegetable",
      "definition": "An edible plant or part of a plant.",
      "difficulty": "A1"
    },
    {
      "word": "fresh",
      "definition": "Recently prepared or picked.",
      "difficulty": "A1"
    },
    {
      "word": "delicious",
      "definition": "Having a very pleasant taste.",
      "difficulty": "A2"
    },
    {
      "word": "sweet",
      "definition": "Having a sugary taste.",
      "difficulty": "A1"
    },
    {
      "word": "salty",
      "definition": "Having the taste of salt.",
      "difficulty": "A1"
    },
    {
      "word": "bitter",
      "definition": "Having a sharp, unpleasant taste.",
      "difficulty": "A2"
    },
    {
      "word": "sour",
      "definition": "Having an acidic taste.",
      "difficulty": "A2"
    },
    {
      "word": "hot",
      "definition": "Having a high temperature.",
      "difficulty": "A1"
    },
    {
      "word": "cold",
      "definition": "Having a low temperature.",
      "difficulty": "A1"
    },
    {
      "word": "serve",
      "definition": "To bring food or drinks to a customer.",
      "difficulty": "A2"
    },
    {
      "word": "recommend",
      "definition": "To suggest something as a good choice.",
      "difficulty": "A2"
    },
    {
      "word": "special",
      "definition": "A dish featured by the restaurant.",
      "difficulty": "A2"
    },
    {
      "word": "available",
      "definition": "Ready to be ordered or used.",
      "difficulty": "A2"
    },
    {
      "word": "allergy",
      "definition": "A medical reaction to certain foods.",
      "difficulty": "A2"
    },
    {
      "word": "gluten",
      "definition": "A protein found in wheat and similar grains.",
      "difficulty": "A2"
    },
    {
      "word": "vegan",
      "definition": "A person who eats no animal products, or food suitable for them.",
      "difficulty": "A2"
    },
    {
      "word": "portion",
      "definition": "An amount of food served to one person.",
      "difficulty": "A2"
    },
    {
      "word": "napkin",
      "definition": "A cloth or paper used while eating.",
      "difficulty": "A1"
    },
    {
      "word": "spoon",
      "definition": "A utensil with a rounded bowl for eating.",
      "difficulty": "A1"
    },
    {
      "word": "glass",
      "definition": "A drinking container.",
      "difficulty": "A1"
    },
    {
      "word": "bowl",
      "definition": "A round dish used for serving food.",
      "difficulty": "A1"
    },
    {
      "word": "payment",
      "definition": "The act of giving money for goods or services.",
      "difficulty": "A2"
    },
    {
      "word": "cash",
      "definition": "Money in the form of coins or banknotes.",
      "difficulty": "A1"
    },
    {
      "word": "credit card",
      "definition": "A card used to pay for purchases.",
      "difficulty": "A2"
    },
    {
      "word": "change",
      "definition": "Money returned after paying more than the cost.",
      "difficulty": "A2"
    },
    {
      "word": "complaint",
      "definition": "A statement that something is not satisfactory.",
      "difficulty": "B1"
    },
    {
      "word": "incorrect",
      "definition": "Not right or not what was requested.",
      "difficulty": "A2"
    },
    {
      "word": "replace",
      "definition": "To provide a new item instead of the wrong one.",
      "difficulty": "A2"
    },
    {
      "word": "apologize",
      "definition": "To say you are sorry.",
      "difficulty": "A2"
    },
    {
      "word": "reservation number",
      "definition": "A number used to identify a booking.",
      "difficulty": "A2"
    },
    {
      "word": "available table",
      "definition": "A table that is free for customers.",
      "difficulty": "A2"
    },
    {
      "word": "party",
      "definition": "The group of people dining together.",
      "difficulty": "A2"
    },
    {
      "word": "dine in",
      "definition": "To eat at the restaurant.",
      "difficulty": "A2"
    },
    {
      "word": "takeaway",
      "definition": "Food prepared to be eaten elsewhere.",
      "difficulty": "A2"
    },
    {
      "word": "service",
      "definition": "The assistance provided to customers in a restaurant.",
      "difficulty": "A2"
    },
    {
      "word": "booking",
      "definition": "An arrangement made in advance for a table.",
      "difficulty": "A2"
    },
    {
      "word": "flavor",
      "definition": "The particular taste of a food.",
      "difficulty": "A2"
    },
    {
      "word": "cuisine",
      "definition": "A style of cooking from a particular place.",
      "difficulty": "B1"
    },
    {
      "word": "dish",
      "definition": "A prepared type of food served as part of a meal.",
      "difficulty": "A1"
    }
  ]
}