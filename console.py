#!/usr/bin/python3
"""
    Console entry point for HBnB
    object and data manipulation
"""

import cmd
from models.base_model import BaseModel
from models import storage as FS


def sub_existance(st):
    """ checks for subclass existance """
    try:
        st = eval(st)
        return True
    except NameError:
        return False

class HBNBCommand(cmd.Cmd):
    """ Command """
    prompt = '(hbnb) '
    file = None

    def do_create(self, args):
        """ create function """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        if not sub_existance(args[0]):
            print("** class doesn't exist **")
        elif args[0] == 'BaseModel':
            new_elem = BaseModel()
            new_elem.save()
            print(new_elem.id)

    def do_show(self, args):
        """ show function """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        if not sub_existance(args[0]):
            print("** class doesn't exist **")
        if not args[1]:
            print("** instance id missing **")
        for k, v in FS.all():
            if 


    def do_destroy(self, args):
        """ destroy function """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        if not sub_existance(args[0]):
            print("** class doesn't exist **")

    def do_all(self, args):
        """ all function """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        if not sub_existance(args[0]):
            print("** class doesn't exist **")

    def do_update(self, args):
        """ update function """
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
