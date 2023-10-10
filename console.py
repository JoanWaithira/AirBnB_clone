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
        try:
            new_object = eval(classname)
            print(new_object.id)
            new_object.save()
        except NameError:
            print("** class doesn't exist **")
        return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
