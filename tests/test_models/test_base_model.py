#!/usr/bin/python3
""" Tests for the base class model """

import unittest
from datetime import datetime
import models

BaseModel = models.base_model.BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Tests to run on Base Model.
    """
    def test_instantiation(self):
        """Tests for object instantiation"""
        model = BaseModel()
        self.assertIs(type(model), BaseModel)
        model.name = 'example'
        model.age = 88
        attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
        }
        for attr, typ in attrs_types.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, model.__dict__)
                self.assertIs(type(model.__dict__[attr]), typ)
        self.assertEqual(model.name, "example")
        self.assertEqual(model.age, 88)


if __name__ == '__main__':
    unittest.main()
