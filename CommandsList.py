import subprocess
import os
import importlib
from sys import platform as _platform

currentDir = os.path.dirname(os.path.abspath(__file__))

class CommandInspector(object):
    def __init__(self):
        self.available = self.load_commands()

    def callPlugin(self, command, config):
        sequence = command.split()[1::]
        command = command.split()[0]

        for plugin in self.plugins:
            if plugin["command"] == command:
                command = plugin["callback"]

                command(pyTerm=config, sequence=sequence)

                return True
        return False

    def importPlugins(self):
        dirs = os.listdir(os.path.join(currentDir, "plugins"))
        pluginData = []
        pluginCommands = " "

        for file in dirs:
            if not "pyc" in file.split(".") and not "__init__" in file.split("."):
                moduleName = os.path.splitext(file)[0]
                module = importlib.import_module("plugins." + moduleName)
                moduleClassPrototype = getattr(module, moduleName)
                moduleLoadedClass = moduleClassPrototype()

                initiator = getattr(moduleLoadedClass, "__pytermconfig__")
                data = initiator()
                pluginData.append(initiator())
                pluginCommands += data["command"] + " "

        self.plugins = pluginData
        return pluginCommands

    def load_commands(self):
        if _platform == "linux" or _platform == "linux2":
            filename = os.path.join(currentDir, 'listCommands.sh')
        elif _platform == "darwin":
            filename = os.path.join(currentDir, 'mac_commands.sh')
        else:
            print "Your system is not supported"
            exit()

        command = subprocess.Popen(['bash', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        commands, err = command.communicate()
        commands = commands.replace("ls", "")
        commands += " PyTerm"
        commands += self.importPlugins()
        return commands.split()

    def find(self, query):
        for command in self.available:
            if command == query:
                return True
        return False

    def run(self, commandString, config):
        commandLine = commandString.split()

        if commandString == "{{BREAKAPPLICATION}}":
            return False
        if not commandString == "{{BREAKAPPLICATION}}" and len(commandLine) > 0 and not commandLine[0] == "ls":
            try:
                print ""
                test = subprocess.Popen(commandLine, stdout=subprocess.PIPE)
                output = test.communicate()[0]
                print output
            except OSError as e:
                if not self.callPlugin(commandString, config):
                    print e,

        if commandLine[0] == "ls":
            self.callPlugin(commandString, config)
        print ""
        return True

commands = CommandInspector()