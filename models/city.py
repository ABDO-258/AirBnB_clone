#!/usr/bin/python3
""" BaseModel that defines all common attributes/methods for other classes"""
from models.base_model import BaseModel


class City(BaseModel):
    """sub class of BaseModel """
    state_id = ""
    name = ""
