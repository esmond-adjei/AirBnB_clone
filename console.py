#!/usr/bin/python3
"""console program for AirBnB clone program"""


import cmd
import shlex
import models
from models.base_model import BaseModel

all_models = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def __valid_command(self, cmd_str):
        args = cmd_str.split(" ")  # shlex.split(cmd_str)
        if not args[0]:  # missing
            print("** class name missing **")
            return False
        elif args[0] not in all_models.keys():  # doesn't exist
            print("** class doesn't exist **")
            return False
        else:
            return args

    def __valid_id(self, cmd_args):
        if len(cmd_args) < 2:  # missing id in command
            print("** instance id missing **")
            return False
        obj_id = cmd_args[0] + "." + cmd_args[1]
        obj = models.storage.all().get(obj_id, 0)
        if not obj:  # id doesn't exist in DB
            print("** no instance found **")
            return False
        else:
            return obj

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
            models.storage.new(new_model)
            models.storage.save()
            print(new_model.id)

    def do_show(self, line):
        """
        Prints the string reprensentation of an instance based
        on the class name and id.
        """
        args = self.__valid_command(line)
        if not args:
            return False
        obj = self.__valid_id(args)
        if obj:
            print(obj)

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id.
        """
        args = self.__valid_command(line)
        if not args:
            return False
        obj_id = args[0] + "." + args[1]
        if self.__valid_id(args):
            models.storage.delete(obj_id)
            models.storage.save()

    def do_all(self, line=None):
        """
        Prints all string reprensentaton of all instances based
        or not on the class name
        """
        if line:
            args = line.split(" ")
            if args[0] not in all_models.keys():
                print("** class doesn't exist **")
            else:
                print(models.storage.all(model_type=args[0]))
        else:
            print(models.storage.all())

    def do_update(self, line):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        args = self.__valid_command(line)
        if not args:
            return False
        obj = self.__valid_id(args)
        if not obj:
            return False
        if len(args) <= 2:
            print("** attribute name missing **")
            return False
        elif len(args) <= 3:
            print("** value missing **")
            return False
        else:
            value = args[3]
            print("all args: ", args)
            if ('"' in value or "'" in value) \
                    and (value[0] == value[-1]):
                value = value.replace('"', '').replace("'", '')
            else:
                try:
                    value = eval(value)
                except Exception as err:
                    print("** Invalid attribute type **", err)
                    return False
            setattr(obj, args[2], value)
            obj.save()
            print(obj)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
