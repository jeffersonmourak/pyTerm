#PyTerm

## What's PyTerm ##

PyTerm is a terminal client for linux, that show a hightlight on the availables commands of your computer

#Instalation

To install, you just need run on terminal.

``` git clone https://github.com/jeffersonmourak/pyTerm.git ```

``` cd pyTerm/ ```

and done, just go to Usage topic to see how to use this :)

#Usage

So, how this project is just beginning, you just can run the terminal commands and those aliases.

To run the commands, you just run this command.

``` python terminal.py ```

#plugins

A plugin is a python file inside of "plugin/" directory, this file must have a class with the name of file,

example: if the file is plugin.py must have a class 

``` class plugin(Object): ```

inside this class must have a method called 

``` __pytermconfig__ ```

without arguments, this method must return a dictionary, with those indexes, 

- "command": Command is the command that will be called on terminal
- "callback": this is a function file, that will be called when the command is called

The callback function must have ``` *args, **kwargs ``` as argument too, to enable get the configurations of terminal

### Credits ###

Jefferson Moura [(jeffersonmourak)](https://github.com/jeffersonmourak).

Jonhnatha Trigueiro [(joepreludian)](https://github.com/joepreludian).