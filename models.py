from sqlalchemy import Column, Integer, String, Float
from db import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    cpu_utilization = Column(Float)
    cost_per_month = Column(Float)