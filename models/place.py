#!/usr/bin/python3
"""
==========================================
class of place in which amenity is located
==========================================
"""

# import module
from models.base_model import BaseModel


class Place(BaseModel):
    """
    ================================================
    class of place which inherite from the basemodel
    ================================================

    Description:
        - class of place in which amenity is located 
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
