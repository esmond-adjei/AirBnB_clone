#!/usr/bin/python3
"""Implementation of user class"""

from models.base_model import BaseModel


class User:
    """User class implementation"""

    def __init__(self):
        super().__init__(*args, **kwargs)
        self.username = ""
        self.password = ""
        self.email = ""
