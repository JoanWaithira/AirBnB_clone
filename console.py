#!/usr/bin/env python3

''' This module defines the actual console for the project.'''

import cmd

class HBNBCommand(cmd.Cmd):
    ''' This class creates the project console and defines it's behaviors. '''
    prompt = '(hbnb)'
    def do_EOF(self, line=None):
        ''' Exits the console when EOF is encountered. '''
        return True

    def do_quit(self, line=None):
        ''' Quit command to exit the program. '''
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
