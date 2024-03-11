#!/usr/bin/python3
"""This module defines the BaseModel class"""
import os.path
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """FileStorage class"""

    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Instantiate the class"""
        self.__models_available = {"User": User, "BaseModel": BaseModel,
                                   "Amenity": Amenity, "City": City,
                                   "Place": Place, "Review": Review,
                                   "State": State}
        self.reload()

    def all(self, cls=None):
        """
        Returns the required objects

        **Arguments**
            cls: not required, a valid Class Name
        """
        if cls is None:
            return FileStorage.__objects
        else:
            result = {}
            for k, v in FileStorage.__objects.items():
                if v.__class__.__name__ == cls:
                    result[k] = v
            return result

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
