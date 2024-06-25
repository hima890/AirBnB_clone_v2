#!/usr/bin/python3

from models.base_model import BaseModel


class User(BaseModel):
    """
    user class with basic info email/password/first-last(name)

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
