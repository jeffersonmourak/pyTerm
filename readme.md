#PyTerm

## What's PyTerm ##

PyTerm is a Python-based terminal client for Linux that highlights the available commands of your computer.

#Installation

To install, all you need to do is, run the following commands in your terminal:

```Shell
$ git clone https://github.com/jeffersonmourak/pyTerm.git
$ cd pyTerm/
```

and that's it, now, just go to the Usage topic to see how to use this. :)

#Usage

So, this project is just beginning, you can run the basic terminal commands and those aliases.

To use PyTerm, you need to run the following in your terminal.

```Shell
$ python terminal.py
```

#plugins

A plugin is a Python file, placed inside `plugin/` directory, this file must have a class with the name of the file,

Example: If the file is `plugin.py`, it must have a class `plugin` defined as follows:

```Python
class plugin(object):
```

and this class must have a method called ` __pytermconfig__`.

Without arguments, this method must return a dictionary, with those indexes, 

* "command": Command is the command that will be run in the terminal
* "callback": this is a function file, that will be called when the command is executed

The callback function must have ` *args, **kwargs ` as argument too, to enable get the configurations of the terminal.

### Credits

Jefferson Moura [(jeffersonmourak)](https://github.com/jeffersonmourak).

Jonhnatha Trigueiro [(joepreludian)](https://github.com/joepreludian).
