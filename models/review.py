#!/usr/bin/python3
"""
=========================================
Reiew class that inherites from BaseModel
=========================================
"""

# import module
from models.base_model import BaseModel


class Review(BaseModel):
    """
    =========================================
    Reiew class that inherites from BaseModel
    =========================================

    Description:
        - class that review the place and user
    """
    place_id = ""
    user_id = ""
    text = ""
