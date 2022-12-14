# models/test_model.py

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.session import base


class Test(base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
