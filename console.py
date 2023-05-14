#!/usr/bin/python3
"""console program for AirBnB clone program"""


import cmd
from models import storage
from models.base_model import BaseModel

all_models = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def __valid_command(self, cmd_str):
        args = cmd_str.split(" ")
        if not args[0]:  # missing
            print("** class name missing **")
            return False
        elif args[0] not in all_models.keys():  # doesn't exist
            print("** class doesn't exist **")
            return False
        else:
            return args

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
        args = self.__valid_command(line)
        if args:
            new_model = all_models[args[0]]()
            storage.new(new_model)
            print(new_model.id)  # xxx

    def do_show(self, line):
        """
        Prints the string reprensentation of an instance based
        on the class name and id.
        """
        args = self.__valid_command(line)
        if not args[1]:  # missing
            print("** instance id missing **")
            return
        obj_id = args[0] + "." + args[1]
        obj = storage.all().get(obj_id, 0)
        if not obj:  # doesn't exist
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        args = self.__valid_command(line)
        if not args[1]:  # missing
            print("** instance id missing **")
            return False
        obj_id = args[0] + "." + args[1]
        obj = storage.all().get(obj_id, 0)
        if not obj:  # doesn't exist
            print("** no instance found **")
        else:
            del storage.all().pop(obj_id)
            storage.save()

    def all(self, line=None):
        """
        Prints all string reprensentaton of all instances based
        or not on the class name
        """
        if line:
            args = line.split(" ")
            if args[0] not in all_models.keys():
                print("** class doesn't exist **")
            else:
                print(storage.all(args[0]))
        else:
            print(storage.all())


if __name__ == "__main__":
    HBNBCommand().cmdloop()
