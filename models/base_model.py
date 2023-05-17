#!/usr/bin/python3
""" Class BaseModel """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ Constructor """

    def __init__(self, *args, **kwargs):
        """ Construct """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ String """
        return f'[{type(self).__name__}] ({self.id}) {str(self.__dict__)}'

    def save(self):
        """ Save function """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary """
        temp_dict = self.__dict__.copy()
        temp_dict['__class__'] = self.__class__.__name__
        temp_dict['created_at'] = self.created_at.isoformat()
        temp_dict['updated_at'] = self.updated_at.isoformat()
        return temp_dict
