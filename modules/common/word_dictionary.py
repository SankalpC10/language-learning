level_names = {
    "1": "Starter",
    "2": "Learner",
    "3": "Explorer",
    "4": "Achiever",
    "5": "Champion",
    "6": "Word Guru"
}

# Dictionary with English words as keys and their meanings in various languages
word_dictionary = {
    "1": [
        {"english_word": "apple", "meanings": {"hi": "सेब", "mr": "सफरचंद"}, "image": "https://en.wikipedia.org/w/api.php?action=query&titles=Apple&prop=pageimages&format=json&pithumbsize=500"},
        {"english_word": "book", "meanings": {"hi": "किताब", "mr": "पुस्तक"}, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Gutenberg_Bible%2C_Lenox_Copy%2C_New_York_Public_Library%2C_2009._Pic_01.jpg/500px-Gutenberg_Bible%2C_Lenox_Copy%2C_New_York_Public_Library%2C_2009._Pic_01.jpg"},
        {"english_word": "cat", "meanings": {"hi": "बिल्ली", "mr": "मांजर"},"image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/500px-Cat_August_2010-4.jpg"},
        {"english_word": "dog", "meanings": {"hi": "कुत्ता", "mr": "कुत्रा"}, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Huskiesatrest.jpg/500px-Huskiesatrest.jpg"},
        {"english_word": "egg", "meanings": {"hi": "अंडा", "mr": "अंडे"}, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Adolphe_Millot_oeufs-fixed.jpg/500px-Adolphe_Millot_oeufs-fixed.jpg"},
        {"english_word": "fish", "meanings": {"hi": "मछली", "mr": "मासा"},"image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Balantiocheilos_melanopterus_-_Karlsruhe_Zoo_02_%28cropped%29.jpg/500px-Balantiocheilos_melanopterus_-_Karlsruhe_Zoo_02_%28cropped%29.jpg"},
        {"english_word": "girl", "meanings": {"hi": "लड़की", "mr": "मुलगी"}, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Balantiocheilos_melanopterus_-_Karlsruhe_Zoo_02_%28cropped%29.jpg/500px-Balantiocheilos_melanopterus_-_Karlsruhe_Zoo_02_%28cropped%29.jpg"},
        {"english_word": "hat", "meanings": {"hi": "टोपी", "mr": "टोपी"},"image": "https://cdn.pixabay.com/photo/2013/07/13/10/41/hat-157581_1280.png"},
        {"english_word": "ice", "meanings": {"hi": "बर्फ", "mr": "बर्फ"},"image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Ice_Block%2C_Canal_Park%2C_Duluth_%2832752478892%29.jpg/500px-Ice_Block%2C_Canal_Park%2C_Duluth_%2832752478892%29.jpg"},
        {"english_word": "jug", "meanings": {"hi": "जग", "mr": "जग"},"image": "https://cdn.pixabay.com/photo/2012/05/07/13/53/water-48521_1280.png"},
        {"english_word": "key", "meanings": {"hi": "चाबी", "mr": "चावी"},"image": "https://cdn.pixabay.com/photo/2014/04/03/11/37/key-311986_1280.png"},
        {"english_word": "lamp", "meanings": {"hi": "लैम्प", "mr": "दिवा"},"image": "https://cdn.pixabay.com/photo/2013/07/12/13/53/desk-lamp-147523_1280.png"},
        {"english_word": "man", "meanings": {"hi": "आदमी", "mr": "माणूस"},"image": "https://cdn.pixabay.com/photo/2019/07/26/20/52/man-4365597_1280.png"},
        {"english_word": "nest", "meanings": {"hi": "घोंसला", "mr": "घरटे"},"image": "https://cdn.pixabay.com/photo/2012/05/03/21/54/bird-46635_1280.png"},
        {"english_word": "orange", "meanings": {"hi": "संतरा", "mr": "संत्री"},"image": "https://cdn.pixabay.com/photo/2019/10/13/20/35/orange-4547207_1280.png"},
        # Add more Starter level words as needed
    ],
    "2": [
        {"english_word": "banana", "meanings": {"hi": "केला", "mr": "केळी"}},
        {"english_word": "chair", "meanings": {"hi": "कुर्सी", "mr": "खुर्ची"}},
        {"english_word": "doctor", "meanings": {"hi": "डॉक्टर", "mr": "डॉक्टर"}},
        {"english_word": "elephant", "meanings": {"hi": "हाथी", "mr": "हत्ती"}, "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/African_Bush_Elephant.jpg/500px-African_Bush_Elephant.jpg"},
        {"english_word": "fruit", "meanings": {"hi": "फल", "mr": "फळ"}},
        {"english_word": "goat", "meanings": {"hi": "बकरी", "mr": "शेळी"}},
        {"english_word": "hand", "meanings": {"hi": "हाथ", "mr": "हात"}},
        {"english_word": "ink", "meanings": {"hi": "स्याही", "mr": "शाई"}},
        {"english_word": "jungle", "meanings": {"hi": "जंगल", "mr": "जंगल"}},
        {"english_word": "kite", "meanings": {"hi": "पतंग", "mr": "पतंग"}},
        {"english_word": "lion", "meanings": {"hi": "शेर", "mr": "सिंह"}},
        {"english_word": "moon", "meanings": {"hi": "चाँद", "mr": "चंद्र"}},
        {"english_word": "nose", "meanings": {"hi": "नाक", "mr": "नाक"}},
        {"english_word": "queen", "meanings": {"hi": "रानी", "mr": "राणी"}},
        {"english_word": "road", "meanings": {"hi": "सड़क", "mr": "रस्ता"}},
        # Add more Learner level words as needed
    ],
    "3": [
        {"english_word": "teacher", "meanings": {"hi": "शिक्षक", "mr": "शिक्षक"}},
        {"english_word": "house", "meanings": {"hi": "घर", "mr": "घर"}},
        {"english_word": "river", "meanings": {"hi": "नदी", "mr": "नदी"}},
        {"english_word": "sun", "meanings": {"hi": "सूरज", "mr": "सूर्य"}},
        {"english_word": "table", "meanings": {"hi": "मेज", "mr": "टेबल"}},
        {"english_word": "umbrella", "meanings": {"hi": "छाता", "mr": "छत्री"}},
        {"english_word": "village", "meanings": {"hi": "गांव", "mr": "गाव"}},
        {"english_word": "water", "meanings": {"hi": "पानी", "mr": "पाणी"}},
        {"english_word": "x-ray", "meanings": {"hi": "एक्स-रे", "mr": "एक्स-रे"}},
        {"english_word": "yoga", "meanings": {"hi": "योग", "mr": "योग"}},
        {"english_word": "zebra", "meanings": {"hi": "ज़ेबरा", "mr": "झेब्रा"}},
        # Add more Explorer level words as needed
    ],
    "4": [
        {"english_word": "adventure", "meanings": {"hi": "साहस", "mr": "साहस"}},
        {"english_word": "bicycle", "meanings": {"hi": "साइकिल", "mr": "सायकल"}},
        {"english_word": "cloud", "meanings": {"hi": "बादल", "mr": "ढग"}},
        {"english_word": "diamond", "meanings": {"hi": "हीरा", "mr": "हिरा"}},
        {"english_word": "energy", "meanings": {"hi": "ऊर्जा", "mr": "ऊर्जा"}},
        {"english_word": "family", "meanings": {"hi": "परिवार", "mr": "कुटुंब"}},
        {"english_word": "garden", "meanings": {"hi": "बगीचा", "mr": "बाग"}},
        {"english_word": "honesty", "meanings": {"hi": "ईमानदारी", "mr": "प्रामाणिकता"}},
        {"english_word": "iceberg", "meanings": {"hi": "हिमखंड", "mr": "हिमखंड"}},
        {"english_word": "journey", "meanings": {"hi": "यात्रा", "mr": "प्रवास"}},
        # Add more Achiever level words as needed
    ],
    "5": [
        {"english_word": "affection", "meanings": {"hi": "स्नेह", "mr": "स्नेह"}},
        {"english_word": "bargain", "meanings": {"hi": "सौदा", "mr": "घसाघीस"}},
        {"english_word": "courage", "meanings": {"hi": "साहस", "mr": "धैर्य"}},
        {"english_word": "dignity", "meanings": {"hi": "गरिमा", "mr": "स्वाभिमान"}},
        {"english_word": "equality", "meanings": {"hi": "समानता", "mr": "समानता"}},
        {"english_word": "freedom", "meanings": {"hi": "स्वतंत्रता", "mr": "स्वातंत्र्य"}},
        {"english_word": "glory", "meanings": {"hi": "महिमा", "mr": "महिमा"}},
        {"english_word": "harmony", "meanings": {"hi": "सद्भाव", "mr": "सौहार्द"}},
        {"english_word": "inspire", "meanings": {"hi": "प्रेरित करना", "mr": "प्रेरणा"}},
        {"english_word": "justice", "meanings": {"hi": "न्याय", "mr": "न्याय"}},
        # Add more Champion level words as needed
    ],
    "6": [
        {"english_word": "abundance", "meanings": {"hi": "प्रचुरता", "mr": "समृद्धी"}},
        {"english_word": "benevolent", "meanings": {"hi": "सद्भावनापूर्ण", "mr": "उदार"}},
        {"english_word": "catalyst", "meanings": {"hi": "प्रेरक", "mr": "प्रेरक"}},
        {"english_word": "deliberate", "meanings": {"hi": "जानबूझकर", "mr": "जाणीवपूर्वक"}},
        {"english_word": "exemplary", "meanings": {"hi": "उदाहरणीय", "mr": "आदर्श"}},
        {"english_word": "fortitude", "meanings": {"hi": "धैर्य", "mr": "धैर्य"}},
        {"english_word": "gratitude", "meanings": {"hi": "कृतज्ञता", "mr": "कृतज्ञता"}},
        {"english_word": "humility", "meanings": {"hi": "विनम्रता", "mr": "विनम्रता"}},
        {"english_word": "illuminate", "meanings": {"hi": "प्रकाशित करना", "mr": "प्रकाशित करा"}},
        {"english_word": "journey", "meanings": {"hi": "यात्रा", "mr": "प्रवास"}}
        # Add more Word Guru level words as needed
    ]
}
