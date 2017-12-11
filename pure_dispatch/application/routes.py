'''Our application's main routes file.
'''
from aiohttp import web
from collections import namedtuple


NamedResource = namedtuple('NamedResource', 'name path routes')
Route = namedtuple('Route', 'method handler')

async def handle(request):
    name = request.match_info.get('id', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

routes = [
    NamedResource(
        name='user', 
        path='/user/{id}',
        routes=[
            Route(method='GET', handler=handle)
        ],
    )
]