#!/usr/bin/python3
"""Definition of file storage class"""


import json
#from models.base_model import BaseModel

#all_classes = {"BaseModel": BaseModel}


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
            return dict(filter(lambda obj_id: obj_id[1].__class__ == model_type, self.__objects.items()))
        return self.__objects

    def delete(self, model_id):
        """deletes a model from data `__objects`"""
        if self.__objects.get(model_id, 0):
            del self.__objects[model_id]
        else:
            print("Model not found")  # xxx

    def save(self):
        f"""serializes objects to JSON file (path: {self.__file_path})"""
        json_objs = {}
        # convert object to dictionary before saving to file
        for obj_id, obj in self.__objects.items():
            json_objs[obj_id] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objs, f)

    def reload(self):
        f"""deserializes the JSON file (path: {self.__file_path})"""
        from models.base_model import BaseModel
        all_classes = {"BaseModel": BaseModel}

        try:
            with open(self.__file_path, 'r') as f:
                json_obj = json.load(f)

            # converting from dictionary objects to class objects.
            # this is done by selecting the class type
            # from all_classes dictionary
            for obj_id, obj_dict in json_obj.items():
                class_type = obj_dict["__class__"]
                self.__objects[obj_id] = all_classes[class_type](**obj_dict)
        except Exception as err:
            print(f"Error occurred while opening file: {err}")
