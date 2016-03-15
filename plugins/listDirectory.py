import os
from decorate import bcolors

class listDirectory(object):

	def __pytermconfig__(self):
		return {"command":"ls","callback":self.ls}

	def ls(self,*args, **kwargs):
		print ""
		pyTerm = kwargs["pyTerm"]
		currentPath = pyTerm.getPath()
		dirs = os.listdir(currentPath)

		for file in dirs:
			if os.path.isdir(os.path.join(pyTerm.getPath(), file)):
				print bcolors.BOLD + bcolors.OKGREEN + file + bcolors.ENDC
			else:
				print file
