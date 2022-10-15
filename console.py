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

    def do_create(self, args):
        """ create function """
        pass

    def do_show(self, args):
        """ show function """
        pass

    def do_destroy(self, args):
        """ destroy function """
        pass

    def do_all(self, args):
        """ all function """
        pass

    def do_update(self, args):
        """ update function """
        pass

    def do_quit(self):
        """ test """
        exit()

    def do_EOF(self):
        """ EOF reached - exit """
        print("")
        exit()

    def emptyline(self):
        """ do nothing """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
