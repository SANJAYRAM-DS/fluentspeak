"""
Daily Conversation Topic Content

This file contains all content related to the Daily Conversation topic.
No Django models should be imported here.

The seed_data management command will import this file
and populate the database.
"""

DAILY = {
    "topic": {
        "title": "Daily Conversation",
        "description": "Practice everyday English used in common situations such as meeting people, talking about routines, hobbies, weather, and daily activities.",
        "category": "Daily Life",
        "difficulty": "A1",
        "grammar_focus": "Present Simple",
        "vocabulary_focus": "Everyday Communication",
        "estimated_turns": 35,
        "icon": "💬",
        "display_order": 5,
        "is_active": True,
    },

    # "learning_objectives": [
    #     "Introduce yourself naturally",
    #     "Talk about your daily routine",
    #     "Keep a simple everyday conversation going",
    # ],

    "scenarios": [
        {
            "title": "Meeting Someone New",
            "description": "Introduce yourself and ask basic personal questions.",
            "ai_role": "New Friend",
            "user_role": "Student",
            "opening_prompt": "Hi! My name is Emma. Nice to meet you. What's your name?",
            "learning_objective": "Introduce yourself confidently.",
            "difficulty": "A1",
            "grammar_focus": "Present Simple",
            "vocabulary_focus": "Greetings",
            "max_turns": 30,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Talking About Your Daily Routine",
            "description": "Describe your typical weekday and daily habits.",
            "ai_role": "English Teacher",
            "user_role": "Student",
            "opening_prompt": "Tell me about your daily routine. What do you usually do in the morning?",
            "learning_objective": "Describe everyday activities.",
            "difficulty": "A1",
            "grammar_focus": "Present Simple",
            "vocabulary_focus": "Daily Routine",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Talking About Hobbies",
            "description": "Discuss your hobbies and interests.",
            "ai_role": "Friend",
            "user_role": "Student",
            "opening_prompt": "What do you like doing in your free time?",
            "learning_objective": "Talk about hobbies and interests.",
            "difficulty": "A1",
            "grammar_focus": "Present Simple",
            "vocabulary_focus": "Hobbies",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Talking About the Weather",
            "description": "Discuss today's weather and your preferences.",
            "ai_role": "Neighbor",
            "user_role": "Resident",
            "opening_prompt": "Nice weather today, isn't it?",
            "learning_objective": "Talk naturally about weather.",
            "difficulty": "A1",
            "grammar_focus": "Present Simple",
            "vocabulary_focus": "Weather",
            "max_turns": 30,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Weekend Plans",
            "description": "Talk about your plans for the weekend.",
            "ai_role": "Friend",
            "user_role": "Student",
            "opening_prompt": "Do you have any plans for this weekend?",
            "learning_objective": "Discuss future plans in simple English.",
            "difficulty": "A2",
            "grammar_focus": "Present Simple",
            "vocabulary_focus": "Weekend Activities",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
    ],

    "vocabulary": [
    {
      "word": "hello",
      "definition": "A greeting used when meeting someone.",
      "difficulty": "A1"
    },
    {
      "word": "good morning",
      "definition": "A greeting used in the morning.",
      "difficulty": "A1"
    },
    {
      "word": "friend",
      "definition": "A person you know and like.",
      "difficulty": "A1"
    },
    {
      "word": "family",
      "definition": "People related to you.",
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
      "definition": "The main meal eaten in the evening.",
      "difficulty": "A1"
    },
    {
      "word": "morning",
      "definition": "The early part of the day.",
      "difficulty": "A1"
    },
    {
      "word": "afternoon",
      "definition": "The period after midday.",
      "difficulty": "A1"
    },
    {
      "word": "evening",
      "definition": "The later part of the day before night.",
      "difficulty": "A1"
    },
    {
      "word": "weather",
      "definition": "The condition of the atmosphere.",
      "difficulty": "A1"
    },
    {
      "word": "sunny",
      "definition": "Bright because of sunshine.",
      "difficulty": "A1"
    },
    {
      "word": "rainy",
      "definition": "Having rain.",
      "difficulty": "A1"
    },
    {
      "word": "weekend",
      "definition": "Saturday and Sunday.",
      "difficulty": "A1"
    },
    {
      "word": "hobby",
      "definition": "An activity you enjoy in your free time.",
      "difficulty": "A1"
    },
    {
      "word": "music",
      "definition": "Sounds organized into songs or melodies.",
      "difficulty": "A1"
    },
    {
      "word": "movie",
      "definition": "A film you watch for entertainment.",
      "difficulty": "A1"
    },
    {
      "word": "exercise",
      "definition": "Physical activity to stay healthy.",
      "difficulty": "A1"
    },
    {
      "word": "work",
      "definition": "The place or activity where you have a job.",
      "difficulty": "A1"
    },
    {
      "word": "study",
      "definition": "To learn about a subject.",
      "difficulty": "A1"
    },
    {
      "word": "name",
      "definition": "The word people use to identify a person.",
      "difficulty": "A1"
    },
    {
      "word": "introduce",
      "definition": "To tell someone your name or present yourself.",
      "difficulty": "A1"
    },
    {
      "word": "meet",
      "definition": "To see and get to know someone for the first time.",
      "difficulty": "A1"
    },
    {
      "word": "routine",
      "definition": "The usual things you do every day.",
      "difficulty": "A1"
    },
    {
      "word": "usually",
      "definition": "In most situations or on most days.",
      "difficulty": "A1"
    },
    {
      "word": "weekday",
      "definition": "A day from Monday to Friday.",
      "difficulty": "A1"
    },
    {
      "word": "habit",
      "definition": "Something you do regularly.",
      "difficulty": "A1"
    },
    {
      "word": "wake up",
      "definition": "To stop sleeping.",
      "difficulty": "A1"
    },
    {
      "word": "free time",
      "definition": "Time when you are not working or studying.",
      "difficulty": "A1"
    },
    {
      "word": "interest",
      "definition": "Something you enjoy or like to learn about.",
      "difficulty": "A1"
    },
    {
      "word": "read",
      "definition": "To look at and understand written words.",
      "difficulty": "A1"
    },
    {
      "word": "today",
      "definition": "The present day.",
      "difficulty": "A1"
    },
    {
      "word": "cloudy",
      "definition": "Covered with clouds.",
      "difficulty": "A1"
    },
    {
      "word": "warm",
      "definition": "Having a comfortably high temperature.",
      "difficulty": "A1"
    },
    {
      "word": "cold",
      "definition": "Having a low temperature.",
      "difficulty": "A1"
    },
    {
      "word": "plan",
      "definition": "Something you intend to do in the future.",
      "difficulty": "A1"
    },
    {
      "word": "Saturday",
      "definition": "The first day of the weekend in many countries.",
      "difficulty": "A1"
    },
    {
      "word": "Sunday",
      "definition": "The second day of the weekend in many countries.",
      "difficulty": "A1"
    },
    {
      "word": "teacher",
      "definition": "A person who helps others learn.",
      "difficulty": "A1"
    },
    {
      "word": "student",
      "definition": "A person who is learning at school or elsewhere.",
      "difficulty": "A1"
    },
    {
      "word": "neighbor",
      "definition": "A person who lives near you.",
      "difficulty": "A1"
    },
    {
      "word": "activity",
      "definition": "Something that you do.",
      "difficulty": "A1"
    },
    {
      "word": "talk",
      "definition": "To speak with someone.",
      "difficulty": "A1"
    },
    {
      "word": "question",
      "definition": "A sentence that asks for information.",
      "difficulty": "A1"
    },
    {
      "word": "answer",
      "definition": "A response to a question.",
      "difficulty": "A1"
    },
    {
      "word": "like",
      "definition": "To enjoy or prefer something.",
      "difficulty": "A1"
    },
    {
      "word": "learn",
      "definition": "To gain knowledge or a new skill.",
      "difficulty": "A1"
    },
    {
      "word": "conversation",
      "definition": "A talk between two or more people.",
      "difficulty": "A1"
    }
  ]
}