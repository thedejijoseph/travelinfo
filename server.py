
from starlette.applications import Starlette
from starlette.routing import Route
from starlette.responses import JSONResponse


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
            'message': f'URL {request.url.path} was not found on this server.'
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



exception_handlers = {
    500: handle_server_errors,
    404: handle_404_errors
}

routes = [
    Route('/', root)
]

app = Starlette(
    debug=False,
    routes=routes,
    exception_handlers=exception_handlers
)
