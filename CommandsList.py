import subprocess
import os

class CommandInspector(object):

	def __init__(self):
		self.available = self.load()

	def load(self):

		currentDir = os.path.dirname(os.path.abspath(__file__))

		command = subprocess.Popen(['bash',currentDir + '/listCommands.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		commands, err = command.communicate()

		commands += " PyTerm"
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
				print e,
			
		print ""

		return True

commands = CommandInspector()