#!/usr/bin/python3
"""This module defines the BaseModel class"""
<<<<<<< Updated upstream
from models import storage
from uuid import uuid4
import datetime


=======
from uuid import uuid4
import datetime
>>>>>>> Stashed changes
class BaseModel:
    """BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns official string representation"""

        return "[{}] ({}) {}".\
            format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""

<<<<<<< Updated upstream
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
=======
>>>>>>> Stashed changes
    def __init__(self, id=None):
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = self.created_at
        
    def save(self):
        """update the public instace attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now().isoformat()
    
    def to_dict(self):
        """ returns a dictionary containing all keys/values of __dict__ of the instance"""
        return (
            {
                '__class__': self.__class__.__name__,
                'created_at': self.created_at,
                'updated_at': self.updated_at,
                'id': self.id
            }
        )
