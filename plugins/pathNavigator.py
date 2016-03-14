import os

class pathNavigator(object):

	def __pytermconfig__(self):
		return {"command":"cd","callback":self.cd}

	def cd(self,*args, **kwargs):
		pyTerm = kwargs["pyTerm"]
		try:
			sequence = kwargs["sequence"][0]
		except IndexError:
			sequence = ""

		if sequence == "..": # upward
			currentPath = pyTerm.getPath().split("/")[::-1][1::]
			if currentPath[0] == '':
				pyTerm.setPath('/')

			else:
				pyTerm.setPath("/".join(currentPath[::-1]))

		elif sequence == "" or sequence == "~":
			pyTerm.setPath("/home/"+pyTerm.getUser())

		else: # downward
			currentPath = os.path.join(pyTerm.getPath(), sequence)
			if os.path.isdir(currentPath):
				pyTerm.setPath(currentPath)
			else:
				print 'Invalid Directory!'

		os.chdir(pyTerm.currentPath)