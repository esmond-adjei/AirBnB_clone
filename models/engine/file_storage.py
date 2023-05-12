"""Definition of file storage class"""


from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file
       and deserializes JSON file to instances."""

    __file_path = 'file_object.json'
    __objects = {}

    all_classes = {"BaseModel": BaseModel}

    def all(self):
        """returns the dictionary `__objects`"""
        return self.__objects

    def new(self, obj):
        """sets in objects the object with key `<obj name>.id`"""
        if obj is not None:
            obj_id = obj.__class__.__name__ + "." + obj.id
            self.__objects[obj_id] = obj

    def save(self):
        f"""serializes objects to JSON file (path: {__file_path})"""
        json_objs = {}
        # convert object to dictionary before saving to file
        for obj_id, obj in self.__objects.items():
            json_objs[obj_id] = obj.to_dict()
        with open(__file_path, 'w') as f:
            json.dump(json_objs, f)

    def reload(self):
        try:
            f"""deserializes the JSON file (path: {__file_path})"""
            with open(__file_path, 'r') as f:
                json_obj = json.load(self.__objects, f)

            # converting from dictionary objects to class objects.
            # this is done by selecting the class type
            # from all_classes dictionary
            for obj_id, obj_dict in json_obj.items():
                class_type = obj_dict["__class__"]
                self.__objects[obj_id] = all_classes[class_type](**obj_dict)
        except Exception as err:
            print("Error occured while opening file", err)
