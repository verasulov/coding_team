from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, BOOLEAN, INTEGER
from sqlalchemy import Column, ForeignKey
from src.helper import Base
from src.models.FoodCategory import FoodCategory


class Food(Base):
    __tablename__ = 'foods'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    category_id = Column(BIGINT, ForeignKey(FoodCategory.id), nullable=False)
    name = Column(VARCHAR, nullable=False)
    description = Column(VARCHAR, nullable=False)
    price = Column(INTEGER, nullable=False)
    is_special = Column(BOOLEAN, server_default='false', nullable=False)
    is_vegan = Column(BOOLEAN, server_default='false', nullable=False)
    is_publish = Column(BOOLEAN, server_default='false', nullable=False)
