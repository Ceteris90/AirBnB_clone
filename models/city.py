#!/usr/bin/python3
"""
========================================
City class that inherits from BaseModel.
========================================
"""

# import module
from models.base_model import BaseModel


class State(BaseModel):
    """
    ============================================
    State class that inherite from the BaseModel
    ============================================
    Description:
        - to set the user state and location
    """
    state_id = ""
    name = ""
