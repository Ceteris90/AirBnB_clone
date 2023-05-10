#!/usr/bin/python3
"""
===============================================
Amenity class that inherites from the BaseModel
===============================================
"""

# import the module
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    ===============================================
    Amenity class that inherites from the BaseModel
    ===============================================

    Description:
        - Create or input the amenity in the state
    """
    name = ""
