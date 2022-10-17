#!/usr/bin/python3
"""
    Entry point file for HBnB command
    console interpreter. Help for each
    command is found by running the
    "help" command via this console.
"""
import cmd
from models import storage
from models.base_model import BaseModel


def sub_existance(st):
    """
        Checks whether if a string points
        to an existing class or subclass
    """
    try:
        st = eval(st)
        return True
    except NameError:
        return False


class HBNBCommand(cmd.Cmd):
    """
        Command prompt class for HBnB
        object an data management console.
    """
    prompt = '(hbnb) '
    file = None

    def do_create(self, args):
        """
            Creates a new instance of the
            specified class or subclass and
            prints the associated unique identifier.

            Usage: create <class_name>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        if not sub_existance(args[0]):
            print("** class doesn't exist **")
        elif args[0] == 'BaseModel':
            new_elem = BaseModel()
            print(new_elem.id)

    def do_show(self, args):
        """
            Finds and prints an instance of
            the specified class or subclass
            if the corresponding ID matches
            the one specified by the request.

            Usage: show <class_name> <id>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        if not sub_existance(args[0]):
            print("** class doesn't exist **")
        if not args[1]:
            print("** instance id missing **")

    def do_destroy(self, args):
        """
            Finds and deletes an instance of
            the specified class or subclass
            if the corresponding ID matches
            the one specified by the request.

            Usage: destroy <class_name> <id>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        if not sub_existance(args[0]):
            print("** class doesn't exist **")

    def do_all(self, args):
        """
            Finds and prints all instances of
            the specified class or subclass.

            Usage: all <class_name>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        if not sub_existance(args[0]):
            print("** class doesn't exist **")

    def do_update(self, args):
        """
            Finds and updates an instance of
            the specified class or subclass
            if the corresponding ID matches
            the one specified by the request.

            Usage: update <class name> <id> <attribute> "<value>"
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        if not sub_existance(args[0]):
            print("** class doesn't exist **")

    def do_quit(self, args):
        """ test """
        exit()

    def do_EOF(self, args):
        """ EOF reached - exit """
        print("")
        exit()

    def emptyline(self):
        """ do nothing """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
