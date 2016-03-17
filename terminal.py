import subprocess
import sys,os
from shell import Shell
from CommandsList import commands
import getpass

class Configs(object):

	def __init__(self):
		self.currentPath = os.getcwd()

	def setPath(self,path):
		self.currentPath = path

	def getPath(self):
		return self.currentPath

	def getUser(self):
		return getpass.getuser()

configs = Configs()

shell = Shell(configs)

def runCommand(commandString):

	if commands.run(commandString,configs):
		runCommand(shell.listener())
		os.system('clear')

runCommand(shell.listener())