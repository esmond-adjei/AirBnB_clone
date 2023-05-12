#!/usr/bin/python3
"""
Implementation of the parent class (BasedModel).
"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """Parent/base class. All other classes inherits from here."""
    def __init__(self, *args, **kwargs):
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
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        cls_dict = {'__class__': self.__class__.__name__}
        cls_dict.update({k: v.isoformat()
                        if isinstance(v, datetime)
                        else v for k, v in self.__dict__.items()})
        return cls_dict
