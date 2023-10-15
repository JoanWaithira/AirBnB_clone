# 0x00. AirBNB clone - The Console

`Group project`	`Python` `OOP`

### Concepts learnt:

* Python packages
* Cmd module
* uuid module
* re module
* unittest module
* args/kwargs

### Specifics

* We learnt:
 * How to create a Python package.
 * How to create a command interpreter in python using the cmd module
 * What is Unit testing and how to implement it in a large project.
 * How to serialize and deserialize a Class
 * How to write and read a JSON file.
 * How to manage datetime
 * What is and UUID
 * What is \*args and how to use it
 * What is \*\*kwargs and how to use it
 * How to handle named arguments in a function

## The console.

* The shell works like this in interactive mode:


```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help	quit	count	all

(hbnb)
(hbnb)
(hbnb) quit
$
```

* To create a new object:

```
(hbnb) create BaseModel
1234-1234-1234-1234
(hbnb)
```

* To show all instances of the class:

```
(hbnb) BaseModel.all()
[BaseModel] (1234-1234-1234-1234) {'created_at":......
```

* To count all instances of a class:

```
(hbnb) BaseModel.count()
1
(hbnb)
```

* To update a particular object:

```
(hbnb) BaseModel.update("1234-1234-1234-1234", name , "Tchaikovsky")
(hbnb)
```

* As you've noticed, there two different supported syntaxes for the various functions
 * One is `$ <function> <class name> <arguments>`
 * The second is: `$ <class name>.<function>(<arguments>)`

* Both sytaxes are supported for the various functions but the latter is preffered.

