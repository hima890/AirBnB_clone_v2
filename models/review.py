#!/usr/bin/python3
"""
class named review that inharits from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review

    Attributes:
        place_id (string): The Place id
        user_id (string): The User id
        text (string): The text of the review

    """
    place_id = ""
    user_id = ""
    text = ""
