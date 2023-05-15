#!/usr/bin/python3
"""Module for base model class"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base model class"""

    def __init__(self, *_args, **kwargs):
        """Constructor for base model class"""
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __set_attributes(self, attributes):
        """Sets the attributes of the model"""
        if '__class__' in attributes:
            del attributes['__class__']
        if 'created_at' in attributes:
            attributes['created_at'] = datetime.strptime(
                attributes['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        if 'updated_at' in attributes:
            attributes['updated_at'] = datetime.strptime(
                attributes['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        for key, value in attributes.items():
            setattr(self, key, value)

    def save(self):
        """Updates the updated_at attribute and saves the model to file"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the model"""
        attributes = self.__dict__.copy()
        attributes['__class__'] = self.__class__.__name__
        attributes['created_at'] = self.created_at.isoformat()
        attributes['updated_at'] = self.updated_at.isoformat()
        return attributes
