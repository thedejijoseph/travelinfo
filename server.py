
from setup import DB_URI
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse
from starlette.config import Config

from motor.motor_asyncio import AsyncIOMotorClient


config = Config('.env')
DB_URI = config('DB_URI', cast=str)
DB_NAME = config('DB_NAME', cast=str, default='travelinfo-staging')

DB_CLIENT = AsyncIOMotorClient(DB_URI)
DB = DB_CLIENT[DB_NAME]

STATES = DB['states']
TERMINALS = DB['terminals']


## helper utilities

async def success(message, data=None, status_code=200):
    response = {'success': True, 'message': message}
    if data:
        response['data'] = data
    
    return JSONResponse(response, status_code=status_code)

async def error(message, errors=None, status_code=500):
    response = {'success': False, 'message': message}
    if errors:
        response['errors'] = errors

    return JSONResponse(response, status_code=status_code)

async def handle_404_errors(request, exception):
    response = {
        'success': False,
        'message': 'Error 404: Not Found',
        'errors': [{
            'message': f'URL {request.url.path} was not found on this server'
        }]
    }
    return JSONResponse(response, status_code=404)

async def handle_server_errors(request, exception):
    response = {
        'success': False,
        'message': 'Server error',
        'errors': [{
            'message': str(exception),
            'details': repr(exception)
        }]
    }
    return JSONResponse(response, status_code=500)


## app routes

async def root(request):
    response = await success('API Root')
    return response

async def query(request):
    from_state = request.query_params['from_state']
    to_state = request.query_params['to_state']

    source_state = await STATES.find_one({'state_id': from_state})
    dest_state = await STATES.find_one({'state_id': to_state})

    if not source_state:
        response = await error(
            'Invalid from_state',
            errors=[{'message': f'State with id {from_state} does not exist'}],
            status_code=400)
        return response
    if not dest_state:
        response = await error(
            'Invalid to_state',
            errors=[{'message': f'State with id {to_state} does not exist'}],
            status_code=400)
        return response
    
    # check terminals in source_state
    if not source_state['terminals']:
        response = await error(f'{source_state["name"]} does not have any terminals')
        return response
    
    # get/check terminals in destination state
    if not dest_state['terminals']:
        response = await error(f'{dest_state["name"]} does not have any terminals')
        return response
    
    connections = []
    
    # as simple as simple get..
    # fetch all the terminals in source state
    cursor = TERMINALS.find({'terminal_id': {'$in': source_state['terminals']}})
    all_terminals = await cursor.to_list(length=24)

    for terminal in all_terminals:
        destinations = terminal['dest_terminals']
        for dest in destinations:
            for dest_state_terminal in dest_state['terminals']:
                if dest == dest_state_terminal:
                    connections.append({terminal['terminal_id']: dest_state_terminal})

    if not connections:
        response = error(f'There are no interconnecting terminals between {source_state["name"]} and {dest_state["name"]}')

    response_data = {'from_state': from_state, 'to_state': to_state}
    response = await success('List of connections', data=connections)
    return response

"""
alternative implementation



"""

exception_handlers = {
    500: handle_server_errors,
    404: handle_404_errors
}

routes = [
    Route('/', root),
    Route('/query', query),
]

app = Starlette(
    debug=False,
    routes=routes,
    exception_handlers=exception_handlers
)
