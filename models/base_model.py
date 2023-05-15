#!/usr/bin/python3
"""Implementation of the parent class (BasedModel)."""
# import os
import sys
import uuid
from datetime import datetime
import models


sys.path.append('..')


class BaseModel:
    """Parent/base class. All other classes inherits from here."""

    def __init__(self, *_args, **kwargs):
        if kwargs:
            del kwargs['__class__']
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """A method to save attributes of an instance
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """hadles the key-paired values to dictionary

        Returns:
            dict: return dictionary
        """
        cls_dict = {'__class__': self.__class__.__name__}
        cls_dict.update({k: v.isoformat()
                        if isinstance(v, datetime)
                        else v for k, v in self.__dict__.items()})
        return cls_dict
