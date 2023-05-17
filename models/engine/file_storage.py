#!/usr/bin/python3
""" Class FileStorage
    Serializes instances to a JSON file
    and deserializes JSON file to instances """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ Construct """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Return dictionary of objects """
        return self.__objects

    def new(self, obj):
        """ Set the obj in the dictionary with key <obj class name>.id """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Serialize objects to the JSON file (path: __file_path) """
        new_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """ Reload the file """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                l_json = json.load(f)
                for key, val in l_json.items():
                    class_name = val['__class__']
                    cls = eval(class_name)
                    self.__objects[key] = cls(**val)
