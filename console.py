#!/usr/bin/python3
"""console program for AirBnB clone program"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User

all_models = {"BaseModel": BaseModel, "User": User}


class HBNBCommand(cmd.Cmd):
    """A Class to define an AirBnB console for Web Developement

    Args:
        cmd (module): a Cmd module, this implements the
        readline function to accept inputs form user.

    Returns:
        Bool: Return Booltype base on the execution of the methods.
    """

    prompt = "(hbnb) "

    def __valid_command(self, cmd_str):
        args = cmd_str.split(" ")

        if not args[0]:  # missing
            print("** class name missing **")
            return False
        elif args[0] not in all_models:  # doesn't exist
            print("** class doesn't exist **")
            return False
        else:
            return args

    def do_quit(self, _arg):
        """Quit/Exit program"""
        return True

    def do_EOF(self, _arg):
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
            models.storage.new(new_model)
            models.storage.save()
            print(new_model.id)  # xx

    def do_show(self, line):
        """
        Prints the string reprensentation of an instance based
        on the class name and id.
        """
        args = self.__valid_command(line)
        if not args:
            return False
        if len(args) < 2:  # missing
            print("** instance id missing **")
            return False
        obj_id = args[0] + "." + args[1]
        obj = models.storage.all().get(obj_id, 0)
        if not obj:  # doesn't exist
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        args = self.__valid_command(line)
        if not args:
            return False
        if len(args) < 2:  # missing
            print("** instance id missing **")
            return False
        obj_id = args[0] + "." + args[1]
        obj = models.storage.all().get(obj_id, 0)
        if not obj:  # doesn't exist
            print("** no instance found **")
        else:
            models.storage.delete(obj_id)
            models.storage.save()

    def do_all(self, line=None):
        """
        Prints all string reprensentaton of all instances based
        or not on the class name
        """
        if line:
            args = line.split(" ")
            if args[0] not in all_models:
                print("** class doesn't exist **")
            else:
                model_type = args[0]
                print(models.storage.all(model_type))
        else:
            print(models.storage.all())

    def do_update(self, line):
        """Update an instance based on the class name and id"""
        args = self.__valid_command(line)
        if not args:
            return False
        if len(args) < 2:
            print("** instance id missing **")
            return False
        obj_id = args[0] + "." + args[1]
        obj = models.storage.all().get(obj_id, None)
        if not obj:
            print("** no instance found **")
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        setattr(obj, args[2], args[3])
        models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
