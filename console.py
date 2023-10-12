#!/usr/bin/python3
"""command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """class of the command interpreter"""
    prompt = "(hbnb) "

    classes = {
         "BaseModel": BaseModel,
         "User" : User,
         "State" : State,
        "City" : City,
        "Amenity" : Amenity,
        "Place" : Place,
        "Review" : Review,      
     }

    
    def emptyline(self):
        """handle empty line + ENTER """
        pass

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True
    
    def do_EOF(self, arg):
        """ if EOF exit the program """
        print()
        return True

    def do_create(self, arg):
        """: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        else:
            object_ = self.__class__.classes[arg]()
            object_.save()
            print(object_.id)
            
    def do_show(self, args):
        """ Prints the string representation of an instance based on the class name and id.
          Ex: $ show BaseModel 1234-1234-1234."""
        arg = args.split()
        if len(arg) > 1:
            key = arg[0]+ '.' + arg[1]
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) <= 1:
            print("** instance id missing **")
        elif arg[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        elif key not in storage.all():
            print("* no instance found **")
        else:
            print(f"{storage.all()[key]}")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id 
            (save the change into the JSON file). 
            Ex: $ destroy BaseModel 1234-1234-1234."""
        arg = args.split()
        if len(arg) > 1:
            key = arg[0]+ '.' + arg[1]
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) <= 1:
            print("** instance id missing **")
        elif arg[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        elif key not in storage.all():
            print("* no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, args):
        """Prints all string representation of all instances based or not on the class name.
            Ex: $ all BaseModel or $ all."""
        list_of_instances = []
        arg = args.split()
        if len(arg) >= 1:
            if arg[0] not in self.__class__.classes.keys():
                print("** class doesn't exist **")
                return
            for key, value in storage.all().items():
                if arg[0] in key:
                    list_of_instances.append(str(value))
        else:
            for key, value in storage.all().items():
                list_of_instances.append(str(value))
        print(list_of_instances)

    def do_update(self, args):
        """  Updates an instance based on the class name and id by adding 
            or updating attribute (save the change into the JSON file). 
            Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
            Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        arg = args.split()
        if len(arg) > 1:
            key = arg[0]+ '.' + arg[1]
        if len(arg) == 0:
            print("** class name missing **")
        elif len(arg) == 1:
            print("*** instance id missing **")
        elif arg[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        elif key not in storage.all():
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        else:
            instance = storage.all()[key]
            setattr (instance, arg[2], arg[3])
            storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()