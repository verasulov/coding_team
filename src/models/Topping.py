from sqlalchemy.dialects.postgresql import BIGINT, VARCHAR
from sqlalchemy import Column
from src.helper import Base


class Topping(Base):
    __tablename__ = 'toppings'
    id = Column(BIGINT, autoincrement=True, primary_key=True, nullable=False)
    name = Column(VARCHAR, nullable=False)
