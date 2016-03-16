import subprocess
import os
import importlib
from time import sleep
from sys import platform as _platform


currentDir = os.path.dirname(os.path.abspath(__file__))

def callPlugin(command,config):
	sequence = command.split()[1::]
	command = command.split()[0]

	for plugin in plugins:
		if plugin["command"] == command:
			command = plugin["callback"]
			command(pyTerm=config,sequence=sequence)
			return True
	return False

def importPlugins():
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

	plugins = pluginData
	return pluginCommands

def load_commands():
	if _platform == "linux" or _platform == "linux2":
		filename = currentDir + '/listCommands.sh'
	elif _platform == "darwin":
		filename = currentDir + '/mac_commands.sh'
	else:
		print "Your system is not supported"
		exit()

	command = subprocess.Popen(['bash',filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	commands, err = command.communicate()
	commands = commands.replace("ls","")
	commands += " PyTerm"
	commands += importPlugins()
	return commands.split()

def cache_commands(commands):
	commandsString = " ".join(commands)
	with open(os.path.join(currentDir, "/config/commands"), 'w') as cC:
		cC.write(commandsString)

def load():
	if os.path.isfile("config/commands"):
		with open(os.path.join(currentDir, "/config/commands"), 'r') as cC:
			cachedCommands = cC.read()
		return cachedCommands.split()
	else:
		commands = load_commands()
		cache_commands(commands)
		return commands

def find(query):
	for command in available:
		if command == query:
			return True

	return False

def run(commandString,config):
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
			if not callPlugin(commandString,config):
				print e,

	if commandLine[0] == "ls":
		callPlugin(commandString,config)

	print ""

	return True

available = load()
