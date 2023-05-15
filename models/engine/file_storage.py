#!/usr/bin/python3
"""Definition of file storage class"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances."""

    __file_path = 'file.json'
    __objects = {}

    def new(self, obj):
        """Sets in objects the object with key `<obj name>.id`"""
        if obj is not None:
            obj_id = obj.__class__.__name__ + "." + obj.id
            self.__objects[obj_id] = obj

    def all(self):
        """Returns the dictionary `__objects`"""
        return self.__objects

    def save(self, model=None):
        """Serializes objects to JSON file (path: {self.__file_path})"""
        json_objs = {}
        # Convert object to dictionary before saving to file
        for obj_id, obj in self.__objects.items():
            json_objs[obj_id] = obj.to_dict()
        try:
            with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
                json.dump(json_objs, f)
        except FileNotFoundError as err:
            print(f"Error occurred while opening file: {err}")

    def reload(self):
        """Deserializes the JSON file (path: {self.__file_path})"""
        all_classes = {"BaseModel": BaseModel}
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                    json_obj = json.load(f)

                # Converting from dictionary objects to class objects.
                # This is done by selecting the class type
                # from all_classes dictionary
                for obj_id, obj_dict in json_obj.items():
                    class_type = obj_dict["__class__"]
                    self.__objects[obj_id] = all_classes[
                        class_type](**obj_dict)
            except json.JSONDecodeError as err:
                print(f"Error occurred while decoding JSON: {err}")
            except KeyError as err:
                print(f"Key error occurred: {err}")
            except Exception as err:
                print(f"An error occurred: {err}")
        else:
            print("No file")
