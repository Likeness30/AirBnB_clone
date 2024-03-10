#!/usr/bin/python3
"""this is the default console module"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """A simple Command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exits the cmd"""
        return True

    def do_EOF(self, args):
        """EOF"""
        return True

    def emptyline(self):
        pass

    def precmd(self, line):
        return line.strip()

    def do_create(self, args):
        """Creates a new instance of BaseModel,
        saves it to the JSON file, and prints the id."""
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance."""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        print(objects[key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id."""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        del objects[key]
        storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances."""
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
            return
        arg_list = args.split()
        if arg_list[0] not in globals():
            print("** class doesn't exist **")
            return
        print([str(obj) for key, obj in objects.items()
               if key.startswith(arg_list[0])])

    def do_update(self, args):
        """Updates an instance based on
        the class name and id by adding or updating attribute."""
        if not args:
            print("** class name missing **")
            return
        arg_list = args.split()
        if arg_list[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        key = arg_list[0] + "." + arg_list[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        setattr(objects[key], arg_list[2], arg_list[3])
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
