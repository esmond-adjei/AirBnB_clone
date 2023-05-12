#!/usr/bin/python3
"""console program for AirBnB clone program"""


import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit/Exit program"""
        return True

    def do_EOF(self, arg):
        """Quit/Exit when End-of-File (EOF) character is entered"""
        return True

    def emptyline(self):
        """Overlook empty lines"""
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
