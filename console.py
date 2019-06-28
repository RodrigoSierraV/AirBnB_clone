#!/usr/bin/python3
import cmd, sys
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Command to exit the Interpreter typing EOF"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """empty line + ENTER execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        #saving to JSON file is missing
        if len(arg) == 0:
            print('** class name missing **')
        elif arg == 'BaseModel':
            new_instance = BaseModel()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an
            instance based on the class name and id"""
        commands = arg.split()
        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        #Searhing ID is missing

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        commands = arg.split()
        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        #Searhing ID is missing

    #all and update methods are missing

if __name__ == '__main__':
    HBNBCommand().cmdloop()
