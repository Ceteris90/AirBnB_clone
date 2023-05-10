#!/usr/bin/python3
"""
==================================================
User class that inherites from the Basemodel class
==================================================
"""

# import the important libraries
from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    """
    ==================================================
    User class that inherites from the BaseModel class
    ==================================================

    Description:
        - This allows for a creation of new user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
