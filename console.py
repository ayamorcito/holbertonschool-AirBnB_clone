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
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
        else:
            try:
                cl = eval(args[0])
                new_element = cl()
                new_element.save()
                print(new_element.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
            Finds and prints an instance of
            the specified class or subclass
            if the corresponding ID matches
            the one specified by the request.

            Usage: show <class_name> <id>
        """
        elem = None
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                cl = eval(args[0])
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    for key, value in storage.all().items():
                        if value.__class__.__name__ == args[0]:
                            elem = value if value.id == args[1] and not elem else None
                    if elem is not None:
                        print(elem)
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

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
        else:
            ekey = None
            try:
                cl = eval(args[0])
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    if storage.delete(args[1]):
                        pass
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, args):
        """
            Finds and prints all instances of
            the specified class or subclass.

            Usage: all <class_name>
        """
        args = args.split()
        ls = []
        if len(args) == 0:
            print("** class name missing **")
        else:
            try:
                cl = eval(args[0])
                for key, value in storage.all().items():
                    if value.__class__.__name__ == args[0]:
                        ls.append(str(value))
                print(ls)
            except NameError:
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
        else:
            try:
                cl = eval(args[0])
                if len(args) < 2:
                    print("** instance id missing **")
                    return
                if len(args) < 3:
                    print("** attribute name missing **")
                    return
                if len(args) < 4:
                    print("** value missing **")
                    return
                if storage.update(args[1], args[2], args[3]):
                    storage.save()
                else:
                    print("** no instance found **")
            except NameError:
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
