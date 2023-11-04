
# Define the room subtypes and their descriptions in a dictionary
ROOM_SUBTYPES = {
    'Standard': {
        'Single': {
            'description': 'This room has one single bed and basic amenities.',
            'price_per_night': 100,  # Add the price per night for this subtype
            'bed_count': 1,  # Add the bed count for this subtype
            'max_adults': 2,
            'max_children': 2
        },
        'Double': {
            'description': 'This room has two double beds and is suitable for families.',
            'price_per_night': 150,  # Add the price per night for this subtype
            'bed_count': 2,  # Add the bed count for this subtype
            'max_adults': 2,
            'max_children': 2
        },
        'Twin': {
            'description': 'This room has two twin beds, ideal for friends or colleagues.',
            'price_per_night': 120,  # Add the price per night for this subtype
            'bed_count': 2,  # Add the bed count for this subtype
            'max_adults': 2,
            'max_children': 2            
        },
    },
    'Deluxe': {
        'King': {
            'description': 'A spacious room with a king-sized bed and luxurious amenities.',
            'price_per_night': 200,  # Add the price per night for this subtype
            'bed_count': 1,  # Add the bed count for this subtype
            'max_adults': 2,
            'max_children': 2
        },
        'Queen': {
            'description': 'This room features a queen-sized bed and additional comforts.',
            'price_per_night': 180,  # Add the price per night for this subtype
            'bed_count': 1,  # Add the bed count for this subtype
            'max_adults': 2,
            'max_children': 2
        },
        'Suite': {
            'description': 'A deluxe suite with a separate living area and premium amenities.',
            'price_per_night': 250,  # Add the price per night for this subtype
            'bed_count': 1,  # Add the bed count for this subtype
            'max_adults': 2,
            'max_children': 2
            
        },
    },
    'Suite': {
        'Junior': {
            'description': 'A junior suite with a comfortable living space and a king-sized bed.',
            'price_per_night': 300,  # Add the price per night for this subtype
            'bed_count': 1,  # Add the bed count for this subtype
            'max_adults': 2,
            'max_children': 2
        },
        'Executive': {
            'description': 'An executive suite with a separate bedroom and workspace.',
            'price_per_night': 350,  # Add the price per night for this subtype
            'bed_count': 1,  # Add the bed count for this subtype
            'max_adults': 2,
            'max_children': 2

        },
        'Presidential': {
            'description': 'The most luxurious suite with multiple rooms and stunning views.',
            'price_per_night': 500,  # Add the price per night for this subtype
            'bed_count': 1,  # Add the bed count for this subtype
            'max_adults': 2,
            'max_children': 2
        },
    },
}



ROOM_FEATURES = {
    'Standard': ['Wi-Fi', 'TV', 'Air Conditioning'],
    'Deluxe': ['Wi-Fi', 'TV', 'Air Conditioning', 'Mini-Bar'],
    'Suite':  ['Wi-Fi', "TV's", 'Air Conditioning', 'Mini-Bar', 'Work Station', 'Terrace-Balcony'],
    # Add more room types and their features as needed
}