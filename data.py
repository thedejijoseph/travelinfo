
# cause why not
states_in_nigeria = [
    'Abia',
    'Adamawa',
    'Akwa Ibom',
    'Anambra',
    'Bauchi',
    'Bayelsa',
    'Benue',
    'Borno',
    'Cross River',
    'Delta',
    'Ebonyi',
    'Enugu',
    'Edo',
    'Ekiti',
    'Gombe',
    'Imo',
    'Jigawa',
    'Kaduna',
    'Kano',
    'Katsina',
    'Kebbi',
    'Kogi',
    'Kwara',
    'Lagos',
    'Nasarawa',
    'Niger',
    'Ogun',
    'Ondo',
    'Osun',
    'Oyo',
    'Plateau',
    'Rivers',
    'Sokoto',
    'Taraba',
    'Yobe',
    'Zamfara',
    'FCT'
]


states = [
    {
        'name': 'Lagos',
        'state_id': 'lagos',
        'terminals': [
            'trm_oshodi'
        ]
    },
    {
        'name': 'Ondo State',
        'state_id': 'ondo',
        'terminals': [
            'trm_ondo_garage'
        ]
    }
]

terminals = [
    {
        'terminal_id': 'trm_oshodi',
        'name': 'Oshodi Bus Park',
        'type': 'road',
        'state': 'lagos',
        'location': 'Oshodi Bus Stop',
        'description': 'You can get transport from anywhere in Lagos to Oshodi',
        'dest_terminals': [
            'trm_ondo_garage'
        ]
    },
    {
        'terminal_id': 'trm_ondo_garage',
        'name': 'Ondo Garage',
        'type': 'road',
        'state': 'ondo',
        'location': 'Ondo road, Akure',
        'description': '',
        'dest_terminals': [
            'trm_oshodi'
        ]
    }
]
