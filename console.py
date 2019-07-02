#!/usr/bin/python3
import cmd, sys
from models.base_model import BaseModel
import models

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
        if len(arg) == 0:
            print('** class name missing **')
        elif arg == 'BaseModel':
            new_instance = BaseModel()
            new_instance.save()
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
        else:
            instance = commands[0] + '.' + commands[1]
            if instance in models.storage.all():
                print(models.storage.all()[instance])
            else:
                print('** no instance found **')

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id"""
        commands = arg.split()
        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        else:
            instance = commands[0] + '.' + commands[1]
            if instance in models.storage.all():
                del models.storage.all()[instance]
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        commands = arg.split()
        if len(commands) == 0 or commands[0] == 'BaseModel':
            obj_list = []
            for key in models.storage.all():
                string = str(models.storage.all()[key])
                obj_list.append(string)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or
            updating attribute"""
        commands = arg.split()
        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        elif len(commands) > 1:
            instance = commands[0] + '.' + commands[1]
            if instance not in models.storage.all():
                print('** no instance found **')
        elif len(commands) == 2:
            print('** attribute name missing **')
        elif len(commands) == 3:
            print('** value missing **')
        else:
            setattr(models.storage.all()[instance], commands[2], commands[3])
            models.storage.all().save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
