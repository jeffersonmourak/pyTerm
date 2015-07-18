import os
class listDirectory(object):

	def __pytermconfig__(self):
		return {"command":"ls","callback":self.ls}

	def ls(self,*args, **kwargs):
		print ""
		pyTerm = kwargs["pyTerm"]
		currentPath = pyTerm.getPath()
		dirs = os.listdir(currentPath)

		for file in dirs:
			print file
		