#!/usr/bin/python3
"""
    Console entry point for HBnB
    object and data manipulation
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """ Command """
    prompt = '(hbnb) '
    file = None

    def do_quit(self, args):
        """ test """
        exit()

    def do_help(self, args):
        """ test """
        return True

    def do_EOF(self, args):
        """ EOF reached - exit """
        exit()

    def emptyline(self, args):
        """ do nothing """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
