
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

		return "\r(pyTerm)$"
		return "\r(PyTerm)" + userName +"@" + computerName +":" + currentDir.replace("/home/" + userName, "~") + "$"

	def check(self,commandList):
		isFirst = True
		for text in commandList:
			if isFirst:
				print self.preText(),
			if commands.find(text):
				print bcolors.BOLD + bcolors.OKGREEN + text + bcolors.ENDC,
			else:
				if isFirst:
					print bcolors.BOLD + bcolors.FAIL + text + bcolors.ENDC,
				else:
					print text,

			isFirst = False


