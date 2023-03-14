from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR, BOOLEAN
from sqlalchemy import Column
from src.helper import Base


class FoodCategory(Base):
    __tablename__ = 'food_categories'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    name = Column(VARCHAR, nullable=False)
    is_publish = Column(BOOLEAN, server_default='false', nullable=False)
