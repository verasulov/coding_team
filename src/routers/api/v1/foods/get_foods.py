from src.routers.api.v1.foods.router_path import router_path_v1_foods
from src.controllers.foods.get_publish_food_by_category import get_publish_food_by_category
from bottle import route, response, abort, request
from src.lib.json import json_encode, json_decode


@route(router_path_v1_foods, method='GET')
def router_v1_get_foods():
    response.headers['Content-Type'] = 'application/json'
    params = request.params
    if 'filter' not in params:
        abort(400, 'filter_not_found')

    query_filter = json_decode(params.getunicode('filter'))
    foods = get_publish_food_by_category(query_filter)
    return json_encode(foods)
