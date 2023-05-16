#!/usr/bin/python3
"""This module creates a Review class"""

from models.base_model import BaseModel


class Email(BaseModel):
    """Class for managing email objects"""

    email_id = ""
    email = ""
