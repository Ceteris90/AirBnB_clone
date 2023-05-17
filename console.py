#!/usr/bin/python3
""" Holberton AirBnB Console """
import cmd
import sys
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ General Class for HBNBCommand """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'User': User, 'City': City,
               'Place': Place, 'Amenity': Amenity, 'Review': Review,
               'State': State}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print('')
        exit()

    def emptyline(self):
        """ Method to pass when emptyline entered """
        pass

    def do_create(self, arg):
        """ Create a new instance """
        if not arg:
            print('** class name missing **')
            return
        new = None
        if arg in self.classes:
            new = self.classes[arg]()
            new.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Method to print instance """
        if not arg:
            print('** class name missing **')
            return
        arg_list = arg.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print('** instance id missing **')
            return
        key = arg_list[0] + '.' + arg_list[1]
        if key in storage.all():
            instance = storage.all()[key]
            print(instance)
        else:
            print('** no instance found **')

    def do_destroy(self, arg):
        """ Method to delete instance with class and id """
        if not arg:
            print("** class name missing **")
            return
        arg_list = arg.split()
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print('** instance id missing **')
            return
        key = arg_list[0] + '.' + arg_list[1]
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, arg):
        """ Method to print all instances """
        if not arg:
            instances = [str(a) for a in storage.all().values()]
            print(instances)
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = [str(a) for b, a in storage.all().items() if arg in b]
            print(instances)

    def do_update(self, arg):
        """ Method to update JSON file"""
        arg_list = arg.split()
        if not arg_list:
            print('** class name missing **')
            return
        if arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print('** instance id missing **')
            return

        key = arg_list[0] + '.' + arg_list[1]
        if key in storage.all():
            if len(arg_list) < 3:
                print('** attribute name missing **')
                return
            if len(arg_list) < 4:
                print('** value missing **')
                return

        attr_name = arg_list[2]
        attr_value = arg_list[3]

        instance = storage.all()[key]
        setattr(instance, attr_name, attr_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
