#!/usr/bin/python3
"""this is the default console module"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """A simple Command interpreter"""

    def do_quit(self, args):
        """Exits the cmd"""
        return (True)

    def do_EOF(self, args):
        """EOF"""
        return (True)

    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
