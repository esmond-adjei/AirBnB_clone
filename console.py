#!/usr/bin/python3
"""console program for AirBnB clone program"""


import cmd
from models import storage
from models.base_model import BaseModel

all_models = {"BaseModel": BaseModel}
new_model = ''


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

    def do_create(self, line):
        """Create an instance of BaseModel"""
        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in all_models.keys():
            print("** class doesn't exist **")
        else:
            new_model = all_models[args[0]]()
            print(new_model.id)

    def do_show(self, line):
        """
        Prints the string reprensentation of an instance based
        on the calss name and id.
        """
        
        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in all_models.keys():
            print("** class doesn't exist **")
        elif not args[1]:
            print("** instance id missing **")
        elif new_model.id != args[1]:
            print("** no instance found **")
        else:
            print(storage.all())

    def do_destory(self, line):
        """
        Deletes an instance based on the class name and id.
        """

        args = line.split(" ")
        if not args[0]:
            print("** class name missing **")
        elif args[0] not in all_models.keys():
            print("** class doesn't exist **")
        elif not args[1]:
            print("** instance id missing **")
        elif args[1] != new_model.id:
            print("** no instance found **")
        else:
            storage.delete(args[1])

    def all(self, line = None):
        """
        Prints all string reprensentaton of all instances based
        or not in the class name
        """
        if line:
            args = lines.split()
            if args[0] not in all_models.keys():
                print("** class doesn't exist **")
            else:
                print(storage.all(args[0]))
        else:
            print(storage.all())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
