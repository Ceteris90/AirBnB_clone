0x00. AirBnB clone - The console
================================

Welcome to the AirBnB clone project, where we will be building a web application that mimics the functionalities of AirBnB. Before getting started, we recommend reading the AirBnB concept page for a better understanding of the project.

The first step towards building this web application is to write a command interpreter that will manage all AirBnB objects. This initial step is crucial since it lays the foundation for all the following projects such as HTML/CSS templating, database storage, API, and front-end integration.

Each task in this project is interconnected and plays an important role in creating a robust web application. These tasks include creating a parent class, BaseModel, to handle the initialization, serialization, and deserialization of all future instances. It also involves creating a simple flow of serialization/deserialization, which will convert instances to dictionaries, JSON strings, and files for storage and retrieval.

Additionally, we will create all the necessary classes such as User, State, City, and Place that inherit from the BaseModel class. Furthermore, we will create an abstracted storage engine, File storage, to store and retrieve data within the web application. Lastly, we will develop unittests to validate all classes and storage engines created in the previous steps.

How to start the console
========================

To start the console for this project, you will need to use the command "./console.py". Once the console is running, you will be able to manage all objects using the console or command interpreter.

This console will allow you to store and persist objects in a JSON file. It offers a variety of commands that you can use such as create, show, destroy, all (shows all), update, help, and quit.

Here's an example of how to open the console and access the help command:

~$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 


To exit the console, you can simply use the "quit" command:

(hbnb) quit
$

That's all there is to it! With this console, you can easily manage objects and store them in a JSON file for future use.


Author:
	Jonas Kwame Nyador(Ceteris90)
