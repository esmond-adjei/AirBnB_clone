#!/usr/bin/python3
"""
Implementation of the parent class (BasedModel).
"""


import uuid
from datetime import datetime


class BaseModel:
    """Parent/base class. All other classes inherits from here."""
	def __init__(self):
        	self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = datetime.now()
	
	def __str__(self):
		retturn f"{self.__class__.__name__} {(self.id)} {self.__dict__}"

	def save(self):
		self.updated_at = datetime.now()

	def to_dict(self):
		cls_dict = {__class__ : self.__class__.__name__}
		cls_dict.update({k: v.isoformat() \
			     if isinstance(v, datetime) \
			     else v for k, v in self.__dict__.items()})
		return cls_dict
		
