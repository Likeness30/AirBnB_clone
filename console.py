#!/usr/bin/python3
import cmd


class CommandLine(cmd.Cmd):
    """A simple Command interpreter"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Exits the cmd"""
        return (True)

    def do_EOF(self, args):
        """EOF"""
        return (True)

    def emptyline(self):
        pass


if __name__ == "__main__":
    CommandLine().cmdloop()
