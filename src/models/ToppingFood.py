from sqlalchemy.dialects.postgresql import BIGINT
from src.models.Food import Food
from src.models.Topping import Topping
from sqlalchemy import Column, ForeignKey, Index
from src.helper import Base


class ToppingFood(Base):
    __tablename__ = 'topping_food'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    food_id = Column(BIGINT, ForeignKey(Food.id), nullable=False)
    topping_id = Column(BIGINT, ForeignKey(Topping.id), nullable=False)
    __table_args__ = (
        Index('unique_user_role_pare_id', food_id, topping_id, unique=True),
    )
