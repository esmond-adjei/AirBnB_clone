#!/usr/bin/python3

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_initialization(self):
        """Test object initialization."""
        # Create an instance of BaseModel
        model = BaseModel()

        # Assert that the id, created_at, and updated_at attributes are set
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save(self):
        """Test object save method."""
        # Create an instance of BaseModel
        model = BaseModel()

        # Save the object
        model.save()

        # Assert that the updated_at attribute is updated
        self.assertNotEqual(model.created_at, model.updated_at)

    # Add more test methods as needed

