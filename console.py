#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """A simple Command interpreter"""

    def __init__(self, interactive=True):
        super().__init__()
        self.is_interactive = interactive
        self.prompt = "(hbnb) " if interactive else "(hbnb)\n"

    def do_quit(self, args):
        """Exits the cmd"""
        return (True)

    def do_EOF(self, args):
        """EOF"""
        return (True)

    def emptyline(self):
        pass

    def precmd(self, line):
        return line.strip()

    def postcmd(self, stop, line):
        if not self.is_interactive:
            print("")
            print("(hbnb)")
        return stop


if __name__ == "__main__":
    HBNBCommand().cmdloop()
