"""
Shopping Topic Content

This file contains all content related to the Shopping topic.
No Django models should be imported here.

The seed_data management command will import this file
and populate the database.
"""

SHOPPING = {
    "topic": {
        "title": "Shopping",
        "description": "Learn English for shopping in stores, supermarkets, and malls. Practice asking about prices, sizes, discounts, and returning items.",
        "category": "Daily Life",
        "difficulty": "A2",
        "grammar_focus": "Comparatives & Questions",
        "vocabulary_focus": "Shopping & Retail",
        "estimated_turns": 40,
        "icon": "🛍️",
        "display_order": 3,
        "is_active": True,
    },

    # "learning_objectives": [
    #     "Ask about prices and products",
    #     "Compare different items",
    #     "Return or exchange purchases politely",
    # ],

    "scenarios": [
        {
            "title": "Buying Clothes",
            "description": "Shop for clothes and ask about sizes and colors.",
            "ai_role": "Store Assistant",
            "user_role": "Customer",
            "opening_prompt": "Hello! Welcome to Fashion World. Can I help you find something?",
            "learning_objective": "Buy clothing confidently.",
            "difficulty": "A2",
            "grammar_focus": "Comparatives & Questions",
            "vocabulary_focus": "Clothing",
            "max_turns": 40,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Asking About Discounts",
            "description": "Ask about offers, discounts, and promotions.",
            "ai_role": "Salesperson",
            "user_role": "Customer",
            "opening_prompt": "Good afternoon! Are you looking for today's special offers?",
            "learning_objective": "Ask about discounts and promotions.",
            "difficulty": "A2",
            "grammar_focus": "Comparatives & Questions",
            "vocabulary_focus": "Discounts",
            "max_turns": 30,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Returning an Item",
            "description": "Return or exchange a purchased product.",
            "ai_role": "Customer Service Representative",
            "user_role": "Customer",
            "opening_prompt": "Hello! How can I help you today?",
            "learning_objective": "Return an item politely.",
            "difficulty": "A2",
            "grammar_focus": "Comparatives & Questions",
            "vocabulary_focus": "Returns",
            "max_turns": 35,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Buying Groceries",
            "description": "Purchase everyday grocery items at a supermarket.",
            "ai_role": "Cashier",
            "user_role": "Shopper",
            "opening_prompt": "Good evening! Did you find everything you needed?",
            "learning_objective": "Buy groceries using everyday English.",
            "difficulty": "A1",
            "grammar_focus": "Comparatives & Questions",
            "vocabulary_focus": "Groceries",
            "max_turns": 30,
            "is_system": True,
            "is_public": True,
        },
        {
            "title": "Shopping for Electronics",
            "description": "Compare electronic products before buying.",
            "ai_role": "Electronics Salesperson",
            "user_role": "Customer",
            "opening_prompt": "Welcome! Are you looking for a phone, laptop, or something else today?",
            "learning_objective": "Compare products and make a purchase.",
            "difficulty": "B1",
            "grammar_focus": "Comparatives & Questions",
            "vocabulary_focus": "Electronics",
            "max_turns": 40,
            "is_system": True,
            "is_public": True,
        },
    ],

    "vocabulary": [
    {
      "word": "discount",
      "definition": "A reduction in the normal price of a product.",
      "difficulty": "A2"
    },
    {
      "word": "cashier",
      "definition": "A person who receives payments in a store.",
      "difficulty": "A1"
    },
    {
      "word": "receipt",
      "definition": "A document showing proof of payment.",
      "difficulty": "A2"
    },
    {
      "word": "refund",
      "definition": "Money returned after giving back a product.",
      "difficulty": "A2"
    },
    {
      "word": "exchange",
      "definition": "Replacing one product with another.",
      "difficulty": "A2"
    },
    {
      "word": "fitting room",
      "definition": "A room where customers try on clothes.",
      "difficulty": "A2"
    },
    {
      "word": "size",
      "definition": "The measurement of clothing or shoes.",
      "difficulty": "A1"
    },
    {
      "word": "price",
      "definition": "The amount of money something costs.",
      "difficulty": "A1"
    },
    {
      "word": "wallet",
      "definition": "A small case for carrying money and cards.",
      "difficulty": "A1"
    },
    {
      "word": "cash",
      "definition": "Money in the form of coins or banknotes.",
      "difficulty": "A1"
    },
    {
      "word": "credit card",
      "definition": "A card used to pay for purchases.",
      "difficulty": "A1"
    },
    {
      "word": "customer",
      "definition": "A person who buys goods or services.",
      "difficulty": "A1"
    },
    {
      "word": "shopping cart",
      "definition": "A cart used to carry products in a store.",
      "difficulty": "A1"
    },
    {
      "word": "brand",
      "definition": "The name of a product or company.",
      "difficulty": "A1"
    },
    {
      "word": "expensive",
      "definition": "Costing a lot of money.",
      "difficulty": "A1"
    },
    {
      "word": "cheap",
      "definition": "Costing little money.",
      "difficulty": "A1"
    },
    {
      "word": "warranty",
      "definition": "A written promise to repair or replace a product.",
      "difficulty": "B1"
    },
    {
      "word": "supermarket",
      "definition": "A large self-service grocery store.",
      "difficulty": "A1"
    },
    {
      "word": "checkout",
      "definition": "The place where customers pay for purchases.",
      "difficulty": "A1"
    },
    {
      "word": "sale",
      "definition": "A period when products are sold at reduced prices.",
      "difficulty": "A1"
    },
    {
      "word": "store",
      "definition": "A place where goods are sold.",
      "difficulty": "A1"
    },
    {
      "word": "shop",
      "definition": "A place where people buy products.",
      "difficulty": "A1"
    },
    {
      "word": "shopping",
      "definition": "The activity of buying goods.",
      "difficulty": "A1"
    },
    {
      "word": "purchase",
      "definition": "Something that has been bought.",
      "difficulty": "A2"
    },
    {
      "word": "product",
      "definition": "An item offered for sale.",
      "difficulty": "A1"
    },
    {
      "word": "item",
      "definition": "A single product or object.",
      "difficulty": "A1"
    },
    {
      "word": "store assistant",
      "definition": "A person who helps customers in a store.",
      "difficulty": "A2"
    },
    {
      "word": "salesperson",
      "definition": "A person who sells products.",
      "difficulty": "A2"
    },
    {
      "word": "customer service",
      "definition": "Help and support provided to customers.",
      "difficulty": "A2"
    },
    {
      "word": "offer",
      "definition": "A special deal or promotion.",
      "difficulty": "A2"
    },
    {
      "word": "promotion",
      "definition": "A special sales campaign or discount.",
      "difficulty": "A2"
    },
    {
      "word": "coupon",
      "definition": "A voucher that gives a discount.",
      "difficulty": "A2"
    },
    {
      "word": "special offer",
      "definition": "A product sold at a reduced price for a limited time.",
      "difficulty": "A2"
    },
    {
      "word": "compare",
      "definition": "To examine differences between products.",
      "difficulty": "A2"
    },
    {
      "word": "quality",
      "definition": "The standard of something compared to others.",
      "difficulty": "A2"
    },
    {
      "word": "value",
      "definition": "The worth of a product for its price.",
      "difficulty": "A2"
    },
    {
      "word": "color",
      "definition": "The appearance of an object such as red or blue.",
      "difficulty": "A1"
    },
    {
      "word": "small",
      "definition": "Having a little size.",
      "difficulty": "A1"
    },
    {
      "word": "medium",
      "definition": "A size between small and large.",
      "difficulty": "A1"
    },
    {
      "word": "large",
      "definition": "Having a big size.",
      "difficulty": "A1"
    },
    {
      "word": "shirt",
      "definition": "A piece of clothing worn on the upper body.",
      "difficulty": "A1"
    },
    {
      "word": "pants",
      "definition": "Clothing that covers each leg separately.",
      "difficulty": "A1"
    },
    {
      "word": "dress",
      "definition": "A one-piece garment usually worn by women or girls.",
      "difficulty": "A1"
    },
    {
      "word": "jacket",
      "definition": "A short coat worn on the upper body.",
      "difficulty": "A1"
    },
    {
      "word": "shoes",
      "definition": "Footwear worn to protect the feet.",
      "difficulty": "A1"
    },
    {
      "word": "try on",
      "definition": "To wear clothing briefly to see if it fits.",
      "difficulty": "A2"
    },
    {
      "word": "fit",
      "definition": "To be the correct size for someone.",
      "difficulty": "A1"
    },
    {
      "word": "groceries",
      "definition": "Food and household items bought regularly.",
      "difficulty": "A1"
    },
    {
      "word": "milk",
      "definition": "A white drink produced by mammals.",
      "difficulty": "A1"
    },
    {
      "word": "bread",
      "definition": "A baked food made from flour.",
      "difficulty": "A1"
    },
    {
      "word": "rice",
      "definition": "A common grain used as food.",
      "difficulty": "A1"
    },
    {
      "word": "vegetables",
      "definition": "Edible plants used for food.",
      "difficulty": "A1"
    },
    {
      "word": "fruit",
      "definition": "The sweet edible part of a plant.",
      "difficulty": "A1"
    },
    {
      "word": "electronics",
      "definition": "Devices that operate using electricity.",
      "difficulty": "A2"
    },
    {
      "word": "phone",
      "definition": "A device used for calling and messaging.",
      "difficulty": "A1"
    },
    {
      "word": "laptop",
      "definition": "A portable personal computer.",
      "difficulty": "A2"
    },
    {
      "word": "battery",
      "definition": "A device that supplies electrical power.",
      "difficulty": "A2"
    },
    {
      "word": "screen",
      "definition": "The display of an electronic device.",
      "difficulty": "A2"
    },
    {
      "word": "model",
      "definition": "A particular version of a product.",
      "difficulty": "A2"
    },
    {
      "word": "feature",
      "definition": "A particular function or characteristic of a product.",
      "difficulty": "A2"
    },
    {
      "word": "available",
      "definition": "Ready to be bought or used.",
      "difficulty": "A2"
    },
    {
      "word": "stock",
      "definition": "Products available for sale.",
      "difficulty": "A2"
    },
    {
      "word": "out of stock",
      "definition": "Temporarily unavailable because all items have been sold.",
      "difficulty": "A2"
    },
    {
      "word": "payment",
      "definition": "The act of paying for goods.",
      "difficulty": "A2"
    },
    {
      "word": "change",
      "definition": "Money returned after paying more than the cost.",
      "difficulty": "A2"
    },
    {
      "word": "return",
      "definition": "To take a purchased item back to the store.",
      "difficulty": "A2"
    },
    {
      "word": "defective",
      "definition": "Having a fault or problem.",
      "difficulty": "B1"
    },
    {
      "word": "damaged",
      "definition": "Broken or harmed.",
      "difficulty": "A2"
    },
    {
      "word": "replacement",
      "definition": "A new item given instead of a faulty one.",
      "difficulty": "A2"
    },
    {
      "word": "policy",
      "definition": "The rules followed by a store.",
      "difficulty": "A2"
    },
    {
      "word": "barcode",
      "definition": "A printed code scanned to identify a product.",
      "difficulty": "A2"
    },
    {
      "word": "bag",
      "definition": "A container used to carry purchases.",
      "difficulty": "A1"
    },
    {
      "word": "mall",
      "definition": "A large building with many shops.",
      "difficulty": "A1"
    },
    {
      "word": "queue",
      "definition": "A line of people waiting.",
      "difficulty": "A2"
    },
    {
      "word": "shelf",
      "definition": "A flat surface where products are displayed.",
      "difficulty": "A2"
    },
    {
      "word": "aisle",
      "definition": "A passage between shelves in a store.",
      "difficulty": "A2"
    },
    {
      "word": "label",
      "definition": "A tag that provides product information.",
      "difficulty": "A2"
    },
    {
      "word": "online shopping",
      "definition": "Buying products over the internet.",
      "difficulty": "A2"
    },
    {
      "word": "delivery",
      "definition": "The service of bringing purchased items to a customer.",
      "difficulty": "A2"
    },
    {
      "word": "package",
      "definition": "A wrapped item ready for delivery.",
      "difficulty": "A2"
    },
    {
      "word": "scan",
      "definition": "To read a barcode electronically.",
      "difficulty": "A2"
    },
    {
      "word": "payment terminal",
      "definition": "A machine used to process card payments.",
      "difficulty": "B1"
    },
    {
      "word": "loyalty card",
      "definition": "A card that rewards frequent customers.",
      "difficulty": "B1"
    },
    {
      "word": "shopping bag",
      "definition": "A bag used to carry purchased items.",
      "difficulty": "A1"
    },
    {
      "word": "department store",
      "definition": "A large store with different sections for products.",
      "difficulty": "A2"
    },
    {
      "word": "retail",
      "definition": "The business of selling products directly to customers.",
      "difficulty": "B1"
    }
  ]
}