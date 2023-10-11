#!/usr/bin/env python3

''' This module defines the actual console for the project.'''

import cmd
import json
import re
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    ''' This class creates the project console and defines it's behaviors. '''
    prompt = '(hbnb)'
    _classes = {"State", "User", "BaseModel", "Place", "Review", "Amenity"}

    def do_EOF(self, line=None):
        ''' Exits the console when EOF is encountered. '''
        return True

    def do_quit(self, line=None):
        ''' Quit command to exit the program. '''
        return True

    def do_create(self, classname):
        '''
        Creates new BaseModel object, saves it, and prints the id.
        Usage: $ create <classname>

        Args:
            classname (str): Name of the object class.

        Errors:
            If the class name is absent, ** class name missing ** is printed.
            If the named class does not exist, ** class doesn't exist ** is
                printed.
        '''
        if not classname:
            print("** class name missing **")
            return False
        try:
            new_object = eval(classname)()
            print(new_object.id)
            new_object.save()
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, raw_string):
        '''
        Print string representation of an instance based on class name and id.
        Usage: $ show <classname> <id>

        Exceptions:
            If class name is missing, ** class name missing ** is printed.
            If class name doesn't exist, ** class doesn't exist ** is printed.
            If id is missing, ** instance id missing ** is printed.
            If class name/id pair doesn't exist, ** no instance found **
                is printed.

        Args:
            raw_string (str):String containing classname, and id.
        '''
        if not raw_string:
            print("** class name is missing **")
            return False
        inputs = shlex.split(raw_string)
        if not inputs[1]:
            print("** instance id missing **")
            return False
        if inputs[0] not in self._classes:
            print("** class doesn't exist **")
            return False
        instance = f"{inputs[0]}.{inputs[1]}"
        try:
            print(storage.all()[instance])
        except Exception:
            print("** no instance found **")
            return False

    def do_destroy(self, raw_string):
        '''
        Delete an instance based on classname and id.

        Usage: $ destroy <classname> <id>

        Exceptions:
            If class name is missing, ** class name missing ** is printed.
            If class name doesn't exist, ** class doesn't exist ** is printed.
            If id is missing, ** instance id missing ** is printed.
            If class name/id pair doesn't exist, ** no instance found **
                is printed.

        Args:
            raw_string (str):String containing classname, and id.
        '''
        if not raw_string:
            print("** class name missing **")
            return False
        inputs = shlex.split(raw_string)
        if len(inputs) == 1:
            print("** instance id missing **")
            return False
        instance = f"{inputs[0]}.{inputs[1]}"
        try:
            del storage.all()[instance]
        except Exception:
            print("** no instance found **")
            return False

    def do_all(self, classname=None):
        '''
        Prints string representation of instances based or not on classname.
        '''
        instance_list = []
        if not classname:
            for instance in storage.all().values():
                instance_list.append(instance.__str__())
        else:
            if classname not in self._classes:
                print("** class doesn't exist **")
                return False
            for instance in storage.all().values():
                if instance.__class__.__name__ == classname:
                    instance_list.append(instance.__str__())
        print(instance_list)

    @staticmethod
    def is_float(string):
        '''
        Checks if a string is a floating point number.

        Args:
            string (str): String to be tested.

        Returns:
            True if value is a float.
            False if value is not a float.
        '''
        try:
            float(string)
            return True
        except ValueError:
            return False

    def do_update(self, arg_string):
        '''
        Changes an attribute of an instance based on classname and id.
        Usage: $ update <class name> <id> <attribute name> "<attribute values>"

        Args:
            arg_string (string): This contains args to be parsed.

        Exceptions:
            If class name is missing, ** class name missing ** is printed.
            If class name doesn't exist, ** class doesn't exist ** is printed.
            If id is missing, ** instance id missing ** is printed.
            If class name/id pair doesn't exist, ** no instance found **
                is printed.
            If attribute name is missing, ** attribute name missing **.
            If the value of the attributename doesn't exist, print
                ** value missing **
        '''
        if not arg_string:
            print("** class name missing **")
            return False
        arg_string = arg_string.replace(',', "")
        inputs = shlex.split(arg_string)
        
        if inputs[0] not in self._classes:
            print("** class doesn't exist **")
            return False
        if len(inputs) == 1:
            print("** instance id missing **")
            return False
        instance = f"{inputs[0]}.{inputs[1]}"
        if instance not in storage.all():
            print("** no instance found **")
            return False
        if len(inputs) == 2:
            print("** attribute name missing **")
            return False
        if len(inputs) == 3:
            print("** value missing **")
            return False

        if inputs[3].isnumeric():
            inputs[3] = int(inputs[3])
        elif is_float(inputs[3]):
            inputs[3] = float(inputs[3])
        setattr(storage.all()[instance], data[2], data[3])
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
