"""
Travel Topic Content

This file contains all content related to the Travel topic.
No Django models should be imported here.

The seed_data management command will import this file
and populate the database.
"""

TRAVEL = {
    "topic": {
        "title": "Travel",
        "description": "Learn English for common travel situations including airports, hotels, transportation, and asking for directions.",
        "category": "Daily Life",
        "difficulty": "A2",
        "grammar_focus": "Past Simple",
        "vocabulary_focus": "Travel & Transportation",
        "estimated_turns": 40,
        "icon": "✈️",
        "display_order": 1,
        "is_active": True,
    },

    # "learning_objectives": [
    #     "Describe travel experiences",
    #     "Ask for directions",
    #     "Book accommodation",
    # ],

    "scenarios": [
        {
            "title": "Airport Check-in",
            "description": "Check in for an international flight.",
            "ai_role": "Airline Staff",
            "user_role": "Traveler",
            "opening_prompt": "Good morning! Welcome to Sky Airlines. May I see your passport and ticket?",
            "learning_objective": "Complete the airport check-in process.",
            "difficulty": "A2",
            "grammar_focus": "Past Simple",
            "vocabulary_focus": "Airport",
            "max_turns": 40,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Hotel Check-in",
            "description": "Check into a hotel after arriving at your destination.",
            "ai_role": "Hotel Receptionist",
            "user_role": "Tourist",
            "opening_prompt": "Welcome to Sunrise Hotel! Do you have a reservation?",
            "learning_objective": "Successfully check into a hotel.",
            "difficulty": "A2",
            "grammar_focus": "Past Simple",
            "vocabulary_focus": "Hotel",
            "max_turns": 40,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Asking for Directions",
            "description": "Ask a local person for directions to a tourist attraction.",
            "ai_role": "Local Resident",
            "user_role": "Tourist",
            "opening_prompt": "Hello! Can I help you find somewhere?",
            "learning_objective": "Ask for and understand directions.",
            "difficulty": "A2",
            "grammar_focus": "Past Simple",
            "vocabulary_focus": "Directions",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Taxi Ride",
            "description": "Take a taxi to your destination.",
            "ai_role": "Taxi Driver",
            "user_role": "Passenger",
            "opening_prompt": "Hello! Where would you like to go today?",
            "learning_objective": "Explain your destination clearly.",
            "difficulty": "A2",
            "grammar_focus": "Past Simple",
            "vocabulary_focus": "Transportation",
            "max_turns": 30,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Lost Passport",
            "description": "Report a lost passport at the police station.",
            "ai_role": "Police Officer",
            "user_role": "Tourist",
            "opening_prompt": "Good afternoon. How can I help you today?",
            "learning_objective": "Explain a travel emergency.",
            "difficulty": "B1",
            "grammar_focus": "Past Simple",
            "vocabulary_focus": "Emergency Travel",
            "max_turns": 40,
            "is_system": True,
            "is_public": True,
        },
    ],

    "vocabulary": [
    {
      "word": "passport",
      "definition": "An official document used for international travel.",
      "difficulty": "A2"
    },
    {
      "word": "boarding pass",
      "definition": "A document that allows you to board an airplane.",
      "difficulty": "A2"
    },
    {
      "word": "reservation",
      "definition": "An arrangement to keep a room or seat for someone.",
      "difficulty": "A2"
    },
    {
      "word": "luggage",
      "definition": "Bags and suitcases used while traveling.",
      "difficulty": "A2"
    },
    {
      "word": "departure",
      "definition": "The act of leaving a place.",
      "difficulty": "A2"
    },
    {
      "word": "arrival",
      "definition": "The act of reaching a destination.",
      "difficulty": "A2"
    },
    {
      "word": "destination",
      "definition": "The place someone is traveling to.",
      "difficulty": "A2"
    },
    {
      "word": "customs",
      "definition": "The government department that checks goods entering a country.",
      "difficulty": "B1"
    },
    {
      "word": "itinerary",
      "definition": "A planned route or travel schedule.",
      "difficulty": "B1"
    },
    {
      "word": "gate",
      "definition": "The airport area where passengers board a plane.",
      "difficulty": "A2"
    },
    {
      "word": "check-in",
      "definition": "The process of registering before a flight or hotel stay.",
      "difficulty": "A2"
    },
    {
      "word": "tourist",
      "definition": "A person traveling for pleasure.",
      "difficulty": "A2"
    },
    {
      "word": "hotel",
      "definition": "A place where travelers stay overnight.",
      "difficulty": "A1"
    },
    {
      "word": "taxi",
      "definition": "A vehicle that transports passengers for payment.",
      "difficulty": "A1"
    },
    {
      "word": "map",
      "definition": "A drawing that shows roads, places, and directions.",
      "difficulty": "A1"
    },
    {
      "word": "tour",
      "definition": "A planned visit to places of interest.",
      "difficulty": "A2"
    },
    {
      "word": "flight",
      "definition": "A journey by airplane.",
      "difficulty": "A1"
    },
    {
      "word": "visa",
      "definition": "Official permission to enter another country.",
      "difficulty": "B1"
    },
    {
      "word": "terminal",
      "definition": "The airport building where passengers arrive and depart.",
      "difficulty": "A2"
    },
    {
      "word": "baggage",
      "definition": "Suitcases and bags carried while traveling.",
      "difficulty": "A2"
    },
    {
      "word": "airport",
      "definition": "A place where airplanes take off and land.",
      "difficulty": "A1"
    },
    {
      "word": "airline",
      "definition": "A company that operates flights.",
      "difficulty": "A2"
    },
    {
      "word": "ticket",
      "definition": "A document giving permission to travel.",
      "difficulty": "A1"
    },
    {
      "word": "airplane",
      "definition": "A vehicle that flies through the air.",
      "difficulty": "A1"
    },
    {
      "word": "pilot",
      "definition": "A person who flies an airplane.",
      "difficulty": "A2"
    },
    {
      "word": "crew",
      "definition": "The people working on an aircraft.",
      "difficulty": "A2"
    },
    {
      "word": "security",
      "definition": "Safety checks before boarding a flight.",
      "difficulty": "A2"
    },
    {
      "word": "immigration",
      "definition": "Passport control when entering or leaving a country.",
      "difficulty": "B1"
    },
    {
      "word": "carry-on",
      "definition": "A small bag taken onto an airplane.",
      "difficulty": "A2"
    },
    {
      "word": "checked baggage",
      "definition": "Luggage stored in the aircraft cargo hold.",
      "difficulty": "A2"
    },
    {
      "word": "window seat",
      "definition": "A seat next to the airplane window.",
      "difficulty": "A2"
    },
    {
      "word": "aisle seat",
      "definition": "A seat next to the aisle.",
      "difficulty": "A2"
    },
    {
      "word": "boarding",
      "definition": "The process of getting onto an aircraft.",
      "difficulty": "A2"
    },
    {
      "word": "delay",
      "definition": "A situation where travel happens later than planned.",
      "difficulty": "A2"
    },
    {
      "word": "schedule",
      "definition": "A planned timetable.",
      "difficulty": "A2"
    },
    {
      "word": "journey",
      "definition": "The act of traveling from one place to another.",
      "difficulty": "A2"
    },
    {
      "word": "trip",
      "definition": "A journey to a place and back.",
      "difficulty": "A1"
    },
    {
      "word": "travel",
      "definition": "The activity of going from one place to another.",
      "difficulty": "A1"
    },
    {
      "word": "traveler",
      "definition": "A person who travels.",
      "difficulty": "A2"
    },
    {
      "word": "vacation",
      "definition": "Time spent away from work for travel or relaxation.",
      "difficulty": "A1"
    },
    {
      "word": "holiday",
      "definition": "A period of travel or leisure.",
      "difficulty": "A1"
    },
    {
      "word": "receptionist",
      "definition": "A person who welcomes guests at a hotel.",
      "difficulty": "A2"
    },
    {
      "word": "reception",
      "definition": "The hotel front desk.",
      "difficulty": "A2"
    },
    {
      "word": "guest",
      "definition": "A person staying at a hotel.",
      "difficulty": "A1"
    },
    {
      "word": "room",
      "definition": "A space in a hotel where guests stay.",
      "difficulty": "A1"
    },
    {
      "word": "room key",
      "definition": "A key or card used to enter a hotel room.",
      "difficulty": "A2"
    },
    {
      "word": "key card",
      "definition": "An electronic card that unlocks a hotel room.",
      "difficulty": "A2"
    },
    {
      "word": "single room",
      "definition": "A room for one person.",
      "difficulty": "A2"
    },
    {
      "word": "double room",
      "definition": "A room for two people.",
      "difficulty": "A2"
    },
    {
      "word": "suite",
      "definition": "A large hotel room with extra space.",
      "difficulty": "B1"
    },
    {
      "word": "elevator",
      "definition": "A machine that carries people between floors.",
      "difficulty": "A1"
    },
    {
      "word": "lobby",
      "definition": "The main entrance area of a hotel.",
      "difficulty": "A2"
    },
    {
      "word": "directions",
      "definition": "Instructions for reaching a place.",
      "difficulty": "A1"
    },
    {
      "word": "street",
      "definition": "A public road in a town or city.",
      "difficulty": "A1"
    },
    {
      "word": "intersection",
      "definition": "A place where two roads meet.",
      "difficulty": "A2"
    },
    {
      "word": "traffic light",
      "definition": "A signal that controls road traffic.",
      "difficulty": "A1"
    },
    {
      "word": "turn left",
      "definition": "To move toward the left at a corner.",
      "difficulty": "A1"
    },
    {
      "word": "turn right",
      "definition": "To move toward the right at a corner.",
      "difficulty": "A1"
    },
    {
      "word": "straight ahead",
      "definition": "Continue without turning.",
      "difficulty": "A1"
    },
    {
      "word": "corner",
      "definition": "The point where two streets meet.",
      "difficulty": "A1"
    },
    {
      "word": "nearby",
      "definition": "Not far away.",
      "difficulty": "A1"
    },
    {
      "word": "landmark",
      "definition": "A well-known place used for navigation.",
      "difficulty": "A2"
    },
    {
      "word": "local resident",
      "definition": "A person who lives in the area.",
      "difficulty": "A2"
    },
    {
      "word": "transportation",
      "definition": "The system of moving people or goods.",
      "difficulty": "A2"
    },
    {
      "word": "bus",
      "definition": "A large road vehicle for passengers.",
      "difficulty": "A1"
    },
    {
      "word": "train",
      "definition": "A series of connected railway vehicles.",
      "difficulty": "A1"
    },
    {
      "word": "subway",
      "definition": "An underground railway system.",
      "difficulty": "A2"
    },
    {
      "word": "station",
      "definition": "A place where trains or buses stop.",
      "difficulty": "A1"
    },
    {
      "word": "platform",
      "definition": "The area where passengers wait for a train.",
      "difficulty": "A2"
    },
    {
      "word": "fare",
      "definition": "The money paid for transportation.",
      "difficulty": "A2"
    },
    {
      "word": "driver",
      "definition": "A person who operates a vehicle.",
      "difficulty": "A1"
    },
    {
      "word": "passenger",
      "definition": "A person traveling in a vehicle.",
      "difficulty": "A1"
    },
    {
      "word": "route",
      "definition": "The path followed to reach a destination.",
      "difficulty": "A2"
    },
    {
      "word": "traffic",
      "definition": "Vehicles moving on roads.",
      "difficulty": "A1"
    },
    {
      "word": "police officer",
      "definition": "A person responsible for enforcing the law.",
      "difficulty": "A2"
    },
    {
      "word": "police station",
      "definition": "A building where police officers work.",
      "difficulty": "A2"
    },
    {
      "word": "lost",
      "definition": "Unable to find something.",
      "difficulty": "A1"
    },
    {
      "word": "report",
      "definition": "To officially tell someone about an incident.",
      "difficulty": "A2"
    },
    {
      "word": "theft",
      "definition": "The crime of stealing.",
      "difficulty": "B1"
    },
    {
      "word": "emergency",
      "definition": "A serious situation needing immediate help.",
      "difficulty": "A2"
    },
    {
      "word": "identity",
      "definition": "Information that shows who a person is.",
      "difficulty": "B1"
    },
    {
      "word": "embassy",
      "definition": "A country's official office in another country.",
      "difficulty": "B1"
    },
    {
      "word": "consulate",
      "definition": "An office that helps citizens abroad.",
      "difficulty": "B1"
    },
    {
      "word": "travel insurance",
      "definition": "Insurance that covers travel-related problems.",
      "difficulty": "B1"
    },
    {
      "word": "confirmation",
      "definition": "Proof that a booking has been accepted.",
      "difficulty": "A2"
    },
    {
      "word": "booking",
      "definition": "An arrangement made in advance for travel or accommodation.",
      "difficulty": "A2"
    },
    {
      "word": "guide",
      "definition": "A person or book that helps travelers.",
      "difficulty": "A2"
    },
    {
      "word": "sightseeing",
      "definition": "Visiting interesting places as a tourist.",
      "difficulty": "A2"
    },
    {
      "word": "attraction",
      "definition": "A place that tourists like to visit.",
      "difficulty": "A2"
    },
    {
      "word": "currency",
      "definition": "The money used in a country.",
      "difficulty": "B1"
    },
    {
      "word": "exchange rate",
      "definition": "The value of one currency compared with another.",
      "difficulty": "B1"
    },
    {
      "word": "border",
      "definition": "The line separating two countries.",
      "difficulty": "B1"
    },
    {
      "word": "country",
      "definition": "A nation with its own government.",
      "difficulty": "A1"
    },
    {
      "word": "city",
      "definition": "A large town where many people live.",
      "difficulty": "A1"
    }
  ]
}


"""
{
    "word": "passport",
    "definition": "An official travel document.",
    "part_of_speech": "noun",
    "difficulty": "A2",
    "pronunciation": "/ˈpɑːspɔːrt/",
    "examples": [
        "Don't forget your passport.",
        "I renewed my passport."
    ]
}"""