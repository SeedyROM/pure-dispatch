# This file is part of pure-dispatch.
# https://github.com/SeedyROM/pure-dispatch

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2017, Zack Kollar <zackkollar@gmail.com>
'''The module containing our applications entry point.
'''
from aiohttp import web

from pure_dispatch.database import DATABASE_ENGINE


class Application(web.Application):
    '''Extend web.Applications for simplicity.
    '''

    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.collect_routes()

    def collect_routes(self):
        '''Create our routes dynamically with special
        namedtuples from the routes module.
        '''
        from pure_dispatch.application.routes import routes

        for resource in routes:
            self.router.add_resource(resource.path, name=resource.name)
            for route in resource.routes:
                self.router[resource.name].add_route(route.method, route.handler)


if __name__ == '__main__':
    APP = Application()
    web.run_app(APP)
