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
        print("Create called")

    def do_show(self, args):
        """ show function """
        print("Show called")

    def do_destroy(self, args):
        """ destroy function """
        print("Destroy called")

    def do_all(self, args):
        """ all function """
        print("All called")

    def do_update(self, args):
        """ update function """
        print("Update called")

    def do_quit(self):
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
