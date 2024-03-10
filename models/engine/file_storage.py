#!/usr/bin/python3
"""This module defines the BaseModel class"""
import os.path
import json

class FileStorage:
    """FileStorage class"""
    
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    __file_path = "file.json"
    __objects = {}

    
    def all(self):
        """ returns the dictionary __objects"""
        return (self.__objects)
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        

    def save(self, obj):
            """ serializes __objects to the JSON file (path: __file_path)"""
            self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj
            serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
            with open(self.__file_path, "w") as file:
                json.dump(serialized_objects, file)
            

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name, obj_id = key.split(".")
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
    
