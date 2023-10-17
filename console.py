#!/usr/bin/env python3

''' This module defines the actual console for the project.'''

import cmd
import json
import re
import shlex
from models import storage
from models.amenity import Amenity
from models.city import City
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    ''' This class creates the project console and defines it's behaviors. '''
    prompt = '(hbnb)'
    _classes = ["Amenity",
                "BaseModel",
                "City",
                "Place",
                "Review",
                "State",
                "User"]

    def default(self, line):
        '''
        This method handles unknown command syntaxes.
        Here it's meant to handle commands of the format:

            $ <class name>.<method>(<arguments>)

        for pre-specified commands.

        Supported commands:
            all()
            count()
            show()
            destroy()
            update() # Even with dictionary form attributes.
        '''
        functions = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update}
        regex = r"(.*)\.(.*)\((.*)\)"

        if re.search(regex, line):
            inputs = re.sub(regex, r"\2 \1 \3", line)
            inputs = shlex.split(inputs)
            if inputs[0] in functions.keys():
                if inputs[0] == "update":
                    self.do_update(line)
                else:
                    functions[inputs[0]](' '.join(inputs[1:]))
            else:
                print("*** Unknown syntax: {line}")
        else:
            print(f"*** Unknown syntax: {line}")

    def emptyline(self):
        ''' Handling of no argument entered. '''
        print(end="")

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
        inputs = shlex.split(classname)
        if inputs[0] not in self._classes:
            print("** class doesn't exist **")
            return False
        new_object = eval(inputs[0])()
        print(new_object.id)
        new_object.save()

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
            print("** class name missing **")
            return False
        inputs = shlex.split(raw_string)
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
        print(storage.all()[instance])

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
        if inputs[0] not in self._classes:
            print("** class doesn't exist **")
            return False
        if len(inputs) == 1:
            print("** instance id missing **")
            return False
        instance = f"{inputs[0]}.{inputs[1]}"
        try:
            del storage.all()[instance]
            storage.save()
        except Exception:
            print("** no instance found **")
            return False

    def do_all(self, classname=None):
        '''
        Prints string representation of instances based or not on classname.
        Usage: $ all <class name>

        If class name is absent, all available instances are printed.

        Exceptions:
            If class name does not exist, ** class doesn't exist ** is printed.
        '''
        instance_list = []
        if not classname:
            for instance in storage.all().values():
                instance_list.append(instance.__str__())
        else:
            classname = shlex.split(classname)[0]
            if classname not in self._classes:
                print("** class doesn't exist **")
                return False
            for instance in storage.all().values():
                if instance.__class__.__name__ == classname:
                    instance_list.append(instance.__str__())
        print(instance_list)

    def do_update(self, arg):
        '''
        Changes an attribute of an instance based on classname and id.
        Usage: $ update <class name> <id> <attribute name> "<attribute values>"

        Args:
            arg (string): This contains args to be parsed.

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
        arglist = self.arg_handler(arg)
        obj_dict = storage.all()

        if len(arglist) == 0:
            print("** class name missing **")
            return False
        if arglist[0] not in HBNBCommand._classes:
            print("** class doesn't exist **")
            return False
        if len(arglist) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arglist[0], arglist[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arglist) == 2:
            print("** attribute name missing **")
            return False
        if len(arglist) == 3 and not isinstance(eval(arglist[2]), dict):
            print("** value missing **")
            return False

        if len(arglist) == 4:
            obj = obj_dict["{}.{}".format(arglist[0], arglist[1])]
            if arglist[2] in obj.__class__.__dict__.keys():
                type_value = type(obj.__class__.__dict__[arglist[2]])
                obj.__dict__[arglist[2]] = type_value(arglist[3])
            else:
                obj.__dict__[arglist[2]] = arglist[3]
        elif isinstance(eval(arglist[2]), dict):
            obj = obj_dict["{}.{}".format(arglist[0], arglist[1])]
            for key, value in eval(arglist[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {
                            str, int, float}):
                    type_value = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = type_value(value)
                else:
                    obj.__dict__[key] = value
        storage.save()

    def do_count(self, classname):
        '''
        Counts the number of active instances of a class.
        Usage: $ count <class name>
        '''
        count = 0
        if not classname:
            print("** class name missing **")
            return False
        classname = shlex.split(classname)[0]

        if classname not in self._classes:
            print("** class doesn't exist **")
            return False

        for instance in storage.all().values():
            if classname == instance.__class__.__name__:
                count += 1
        print(f"{count}")

    @staticmethod
    def arg_handler(arg):
        """Parse an argument into a list of tokens.
        Args:
            arg (str): The argument to parse.
        Returns:
            list: A list of tokens.
        """
        curlybraces = re.search(r"\{(.*?)\}", arg)
        sq_brackets = re.search(r"\[(.*?)\]", arg)
        if curlybraces is None:
            if sq_brackets is None:
                return [i.strip(",") for i in split(arg)]
            else:
                tokens_list = split(arg[:sq_brackets.span()[0]])
                parsed_tokens = [i.strip(",") for i in tokens_list]
                parsed_tokens.append(sq_brackets.group())
                return parsed_tokens
        else:
            tokens_list = shlex.split(arg[:curlybraces.span()[0]])
            parsed_tokens = [i.strip(",") for i in tokens_list]
            parsed_tokens.append(curlybraces.group())
            return parsed_tokens

if __name__ == "__main__":
    HBNBCommand().cmdloop()
