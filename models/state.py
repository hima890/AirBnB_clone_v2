#!/usr/bin/python3
"""
class named state that inharits from BaseModel
"""
from models.base_model import BaseModel


class State(BaseModel):
    """A class named state that represents a state

    Attributes:
        name (string): The name of the state
    """
    name = ""
