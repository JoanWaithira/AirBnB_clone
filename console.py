#!/usr/bin/env python3

''' This module defines the actual console for the project.'''

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    ''' This class creates the project console and defines it's behaviors. '''
    prompt = '(hbnb)'

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
            new_object = eval(classname)
            print(new_object.id)
            new_object.save()
        except NameError:
            print("** class doesn't exist **")
        return

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
        inputs = raw_string.split()
        if not inputs[1]:
            print("** instance id missing **")
            return False
        if inputs[0] != "BaseModel":
            print("** class doesn't exist **")
            return False
        

if __name__ == "__main__":
    HBNBCommand().cmdloop()
