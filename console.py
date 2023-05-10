#!/usr/bin/python3
"""
======================================
Entry point of the command interpreter
======================================
"""
# import the cmd module
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
    """
    ======================================================
    HBNBCommand class to implement the command interpreter
    ======================================================
    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """
        ===============================
        EOF command to exit the program
        ===============================

        Args:
            - args : argument enter on the cmd

        Return:
            - True
        """
        print()
        return True

    def emptyline(self):
        """
        ========================================
        Do nothing when an empty line is entered
        ========================================

        Args:
            -

        Return:
            -
        """
        pass

    def do_create(self, args):
        """
        ==============================================================
        Create a new instance of BaseModel, saves it and prints the id
        ==============================================================
        Args:
            - args : arguments input

        Return:
            -
        """
        if not args:
            print("** class name missing **")
            return

        try:
            new_obj = eval(args)()
            new_obj.save()
            print(new_obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, args):
        """
        ========================================================
        Prints the string representation of an class name and id
        ========================================================
        Args:
            -args: argument

        Return:
            -
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objs = storage.all(cls)
        obj_id = args[1]
        key = cls.__name__ + '.' + obj_id

        if key not in objs:
            print("** no instance found **")
            return

        print(objs[key])

    def do_destroy(self, args):
        """
        ==================================================
        Deletes an instance based on the class name and id
        ==================================================
        Args:
            -args: arguments
        Return:
            -
        """

        args = args.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objs = storage.all(cls)
        obj_id = args[1]
        key = cls.__name__ + '.' + obj_id

        if key not in objs:
            print("** no instance found **")
            return

        del objs[key]
        storage.save()

    def do_all(self, args):
        """
        =================================================
        Prints all string representation of all instances
        =================================================
        Args:
            - args: argument
        Return:
            -
        """
        objs = storage.all()
        if not args:
            print([str(objs[obj]) for obj in objs])
            return

        try:
            cls = eval(args)
        except NameError:
            print("** class doesn't exist **")
            return

        print([str(objs[obj]) for obj in objs if isinstance(objs[obj], cls)])

    def do_update(self, args):
        """
        ==================================================
        Updates an instance based on the class name and id
        ==================================================
        Args:
            - args: argument

        Return:
            _
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        objs = storage.all(cls)
        obj_id = args[1]
        key = cls.__name__ + '.' + obj_id

        if key not in objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return


if __name__ == '__main__':
    """
    ====================================================================
    checks if it is being run as the main module and creates an instance
    ====================================================================
    """
    HBNBCommand().cmdloop()
