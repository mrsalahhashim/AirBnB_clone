#!/usr/bin/python3

"""
This file defines the UserModel class, which inherits from BaseModel.
"""


from models.base_model import BaseModel


class User(BaseModel):
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
