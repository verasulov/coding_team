from src.lib.filter_builder import filter_builder, option_builder
from src.helper import get_session, object_as_dict
from src.models.Food import Food
from src.models.ToppingFood import ToppingFood
from src.models.Topping import Topping
from src.models.FoodCategory import FoodCategory
from sqlalchemy import func, literal_column


def get_publish_food_by_category(query_filter: list or dict) -> list:
    result = []
    with get_session() as session:
        query_toppings = session.query(Topping.name).select_from(ToppingFood) \
            .join(Topping, Topping.id == ToppingFood.topping_id, isouter=True) \
            .filter(ToppingFood.food_id == Food.id)
        query_food = session.query(Food.category_id,
                                   Food.name,
                                   Food.description,
                                   Food.price,
                                   Food.is_vegan,
                                   Food.is_special,
                                   func.array(query_toppings.scalar_subquery()).label('toppings'))\
            .filter(Food.is_publish == True)
        if len(query_filter) > 0:
            query_food = query_food.filter(*filter_builder(Food, query_filter))
        query = session.query(FoodCategory.id,
                              FoodCategory.name,
                              func.json_agg(literal_column('food_extend')).label('foods'))\
            .select_from(query_food.subquery('food_extend'))\
            .join(FoodCategory, FoodCategory.id == literal_column('category_id'), isouter=True)\
            .group_by(FoodCategory.id, FoodCategory.name)
        rows = query.all()
        for row in rows:
            (cf_id, name, foods) = row
            result.append({
                'id': cf_id,
                'name': name,
                'foods': foods
            })
    return result
