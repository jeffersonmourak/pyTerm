import subprocess
import os
import importlib
from time import sleep

class CommandInspector(object):

	def __init__(self):
		self.available = self.load()

	def callPlugin(self,command):
		for plugin in self.plugins:
			if plugin["command"] == command.split()[0]:
				command = plugin["callback"]
				command()
				return True

		return False

	def importPlugins(self):

		currentDir = os.path.dirname(os.path.abspath(__file__))

		dirs = os.listdir( currentDir + "/plugins")

		pluginData = []
		pluginCommands = " "

		for file in dirs:
			if not "pyc" in file.split(".") and not "__init__" in file.split("."):
				
				moduleName = os.path.splitext(file)[0]

				module = importlib.import_module("plugins." + moduleName)
				moduleClassPrototype = getattr(module,moduleName)
				moduleLoadedClass = moduleClassPrototype()

				initiator = getattr(moduleLoadedClass,"__pytermconfig__")
				data = initiator()
				pluginData.append(initiator())
				pluginCommands += data["command"] + " "

		self.plugins = pluginData
		return pluginCommands

	def load(self):

		currentDir = os.path.dirname(os.path.abspath(__file__))

		command = subprocess.Popen(['bash',currentDir + '/listCommands.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		commands, err = command.communicate()

		commands += " PyTerm"

		commands += self.importPlugins()

		return commands.split()

	def find(self,query):
		for command in self.available:
			if command == query:
				return True

		return False

	def run(self,commandString):
		commandLine = commandString.split()
		
		if commandString == "{{BREAKAPPLICATION}}":
			return False

		if not commandString == "{{BREAKAPPLICATION}}" and len(commandLine) > 0:
			
			try:

				print ""
				test = subprocess.Popen(commandLine, stdout=subprocess.PIPE)
				output = test.communicate()[0]
				print output
			except OSError as e:
				if not self.callPlugin(commandString):
					print e,
			
		print ""

		return True

commands = CommandInspector()