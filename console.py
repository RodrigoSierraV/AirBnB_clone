#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
import models
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb) '

    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']

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
        commands = shlex.split(arg)
        if len(arg) == 0:
            print('** class name missing **')
        elif arg in self.classes:
            new_instance = eval(commands[0])()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an
            instance based on the class name and id"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.classes:
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
        commands = shlex.split(arg)
        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.classes:
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
        commands = shlex.split(arg)
        if len(commands) == 0:
            obj_list = []
            for key in models.storage.all():
                string = str(models.storage.all()[key])
                obj_list.append(string)
            print(obj_list)
        elif commands[0] in self.classes:
            obj_list = []
            for key in models.storage.all():
                if commands[0] in key:
                    string = str(models.storage.all()[key])
                    obj_list.append(string)
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding or
            updating attribute"""
        commands = shlex.split(arg)
        if len(commands) == 0:
            print('** class name missing **')
        elif commands[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(commands) == 1:
            print("** instance id missing **")
        elif commands[0] + '.' + commands[1] not in models.storage.all():
            print('** no instance found **')
        elif len(commands) == 2:
            print('** attribute name missing **')
        elif len(commands) == 3:
            print('** value missing **')
        else:
            instance = commands[0] + '.' + commands[1]
            setattr(models.storage.all()[instance], commands[2], commands[3])
            models.storage.all()[instance].save()

    def default(self, arg):
        """Method to handle unknown arguments"""
        num_of_instances = 0
        if arg[-6:] == '.all()' and arg[:-6] in self.classes:
            self.do_all(arg[:-6])
        elif arg[-8:] == '.count()' and arg[:-8] in self.classes:
            for key in models.storage.all():
                if arg[:-8] in key:
                    num_of_instances += 1
            print(num_of_instances)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
