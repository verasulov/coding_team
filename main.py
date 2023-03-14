import bottle
from src.server import middleware_app, config

from src.routers.api.v1.foods.get_foods import router_path_v1_foods

if __name__ == '__main__':
    server_config = config.get('server', {})

    bottle.run(app=middleware_app, **server_config)
