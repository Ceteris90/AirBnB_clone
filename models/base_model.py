#!/usr/bin/env python3
"""
===========================================================================
Base Class :  all common attributes/methods for other classes used in clone
===========================================================================
"""
#import the libraries
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """
    ======================================================
    Base class: class that all other classes inherite from
    ======================================================
    """


    def __init__(self, *args, **kwargs):
        """
        ============================================
        __init__:  initialize an instance of a class
        ============================================

        Args:
            -args: allows you to pass a variable arguments to the method
            -kwargs: allows you to pass a keyword arguments to the method

        Return:
            -No return value
        """

        if kwargs:
            for key, value in kwargs.item():
                if key == "__class__":
                    continue
                elif key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    value = datatime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

                if 'id' not in kwargs.items():
                    self.id = str(uuid4())
                elif 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                elif 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()

                setattr(self, key, value)
                model.storage.new(self)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

            model.storage.new(self)

    def __str__(self):
        """
        ========================================================
        return ID of the instance, and the instance's dictionary
        ========================================================

        Args:
            -

        Return:
            - name, id, dictionary
        """
        uid = self.id
        dic = self.__dict__
        return "[{}] ({}) {}".format(type(self).__name__, uid, dic)

    def save(self):
        """
        ============================================
        updates updated_at with the current datetime
        ============================================

        Args:
            _

        Return:
            - no return values
        """
        self.updated_at = datetime.now()
        model.storage.new(self)
        model.storage.save()

    def to_dict(self):
        """
         ===============================================
         returns a dictionary containing all keys/values
         ===============================================

         Args:
            -

        Return:
            -
        """
        temp_dictionary = self.__dict__.copy()
        temp_dictionary['__class__'] = self.__class__.__name__
        temp_dictionary['created_at'] = self.created_at.isoformat()
        temp_dictionary['updated_at'] = self.updated_at.isoformat()
        return temp_dictionary
