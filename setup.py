
import os
import random

from faker import Faker
from dotenv import load_dotenv

import motor.motor_asyncio

fake = Faker()

transport_modes = ['road', 'air', 'rail']
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
terminals = {}


def create_state(state):
    return {
        'name': state,
        'state_id': state.replace(' ', '_').lower(),
        'terminals': []
    }

def create_terminal(state_id):
    return {
        'terminal_id': fake.uuid4(),
        'type': random.choice(transport_modes),
        'state': state_id,
        'name': ' '.join(fake.words()).title(),
        'location': fake.street_name(),
        'description': fake.text()[:60],
        'dest_terminals': []
    }

# first, instantiate a list of states and their ids
states = [create_state(state) for state in states_in_nigeria]

# next, add 1 to 3 terminals per state
for state in states:
    terminal_count = random.randrange(1, 4)
    for count in range(terminal_count):
        new_terminal = create_terminal(state['state_id'])
        state['terminals'].append(new_terminal)
        terminals[new_terminal['terminal_id']] = new_terminal

# then, add 1 or 2 dest_terminals to each terminal
for state in states:
    # first, ignore terminals in the same state
    terminal_pool = [terminal for terminal in terminals.values() if terminal['state'] != state['state_id']]
    for source_terminal in state['terminals']:
        # then, ignore terminals that are not of the same type
        terminal_pool = [terminal for terminal in terminal_pool if terminal['type'] == source_terminal['type']]
        if len(terminal_pool) > 1:
            # select 1 or 2 terminals from slimmed down pool
            target_terminals = random.choices(terminal_pool, k=random.randrange(1,2))
            # extend the dest_terminals list with the terminal_ids of selected terminals
            source_terminal['dest_terminals'].extend([terminal['terminal_id'] for terminal in target_terminals])
        elif len(terminal_pool) == 1:
            dest_terminal = terminal_pool[0]
            source_terminal['dest_terminals'].append(dest_terminal['terminal_id'])
        else:
            pass

# dummy data is set up
# setup method to interact with database

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)

async def write_to_db():
    db = client['travelinfo-staging']

    states_collection = db['states']
    result = await states_collection.insert_many(states)
    print(f'inserted {len(result.inserted_ids)} states into db')

    terminals_collections = db['terminals']
    result = await terminals_collections.insert_many(terminals.values())
    print(f'inserted {len(result.inserted_ids)} terminals into db')

# as well as clearing database
async def flush_db():
    db = client['travelinfo-staging']
    db.drop_collection("states")
    db.drop_collection("terminals")
    print("dropped db collections successfully")
