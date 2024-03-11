#!/usr/bin/python3
"""This module defines the BaseModel class"""
import os.path
import json
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class"""

    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Instantiate the class"""
        self.__models_available = {"BaseModel": BaseModel}
        self.reload()

    def all(self):
        """ returns the dictionary __objects"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """puts all the object to file after serializing them"""
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_dict()
        with open(FileStorage.__file_path, mode="w+", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def reload(self):
        """
        Restart from what is saved on file
        All errors will be silently skipped
        """
        FileStorage.__objects = {}
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as fd:
                temp = json.load(fd)
        except Exception as e:
            return
        for k in temp.keys():
            cls = temp[k].pop("__class__", None)
            if cls not in self.__models_available.keys():
                continue
            # call a good init function
            FileStorage.__objects[k] = self.__models_available[cls](**temp[k])
