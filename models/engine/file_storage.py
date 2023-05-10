#!/usr/bin/python3
"""
===================================================================
FileStorage that serializes and deserializes JSON file to instances
===================================================================
"""

# import the neccessary libraries
import json
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    ===============================================================
    construct a class de/serializes instances to a JSON file
    ===============================================================
    """

    """
    =======================
    Private Class Attribute
    =======================
    """
    __file_path = "file.json"
    __objects = {}

    """
    =======================
    Public Instance Method
    =======================
    """
    def all(self):
        """
        ================================
        Returns the dictionary __objects
        ================================

        Args:
            - no arguments

        Return:
            - dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        ======================================================
        Sets in __objects the obj with key <obj class name>.id
        ======================================================

        Args:
            - obj : object

        Return:
            -
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        =====================================
        serializes __objects to the JSON file
        =====================================

        Args:
            -

        Return:
            -
        """
        dict_to_save = {}
        for key, value in FileStorage.__objects.items():
            dict_to_save[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(dict_to_save, f)

    def reload(self):
        """
        =======================================
        deserializes the JSON file to __objects
        =======================================

        Args:
            -

        Return:
            _
        """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                dict_loaded = json.load(f)
                for key, value in dict_loaded.items():
                    module_name = value["__class__"]
                    cls = eval(module_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
