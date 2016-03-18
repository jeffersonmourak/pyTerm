import socket
import os

from decorate import bcolors
import CommandsList as commands

class PyTermUI(object):
	"""docstring for PyTermUI"""
	def __init__(self,config):
		self.config = config

	def preText(self):
		userName = self.config.getUser()
		computerName = socket.gethostname()
		currentDir = self.config.getPath()
		home = os.environ['HOME']
		return "\r(PyTerm)" + userName +"@" + computerName +":" + currentDir.replace(home, "~") + "$ "

	def check(self,commandList):
		for text in commandList:
			if commands.find(text):
				return text

		return ""