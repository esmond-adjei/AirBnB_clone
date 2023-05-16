#!/usr/bin/python3
"""Definition of file storage class"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file
    and deserializes JSON file to instances."""

    __file_path = 'file_object.json'
    __objects = {}

    def new(self, obj):
        """sets in objects the object with key `<obj name>.id`"""
        if obj is not None:
            obj_id = obj.__class__.__name__ + "." + obj.id
            self.__objects[obj_id] = obj

    def all(self, model_type=None):
        """returns the dictionary `__objects`"""
        if model_type:
            model_cat = list(filter(lambda obj:
                                    str(obj.__class__.__name__) == model_type,
                                    self.__objects.values()))
            return [str(m) for m in model_cat]
        return self.__objects

    def delete(self, model_id):
        """deletes a model from data `__objects`"""
        if self.__objects.get(model_id, 0):
            del self.__objects[model_id]
        else:
            print("Model not found")  # xx

    def save(self):
        """serializes objects to JSON file (path: {self.__file_path})"""
        json_objs = {}
        # convert object to dictionary before saving to file
        for obj_id, obj in self.__objects.items():
            json_objs[obj_id] = obj.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as _f:
            json.dump(json_objs, _f)

    def reload(self):
        """Deserializes the JSON file (path: {self.__file_path})"""
        all_classes = {"BaseModel": BaseModel}
        if not os.path.isfile(FileStorage.__file_path):
            try:
                # Create the file if it doesn't exist
                open(FileStorage.__file_path, 'w', encoding='utf-8').close()
            except IOError as err:
                f_store = FileStorage.__file_path
                print(f"Error occurred while creating file {f_store}: {err}")
        try:
            with open(f_store, 'r', encoding='utf-8') as file:
                json_obj = json.load(file)

            for obj_id, obj_dict in json_obj.items():
                class_type = obj_dict["__class__"]
                FileStorage.__objects[obj_id] = all_classes[
                    class_type](**obj_dict)
        except json.JSONDecodeError as err:
            print(f"Error occurred while decoding JSON: {err}")
        except KeyError as err:
            print(f"Key error occurred: {err}")
        except Exception as err:
            print(f"An error occurred: {err}")
