class pathNavigator(object):

	def __pytermconfig__(self):
		return {"command":"cd","callback":self.cd}

	def cd(self,*args, **kwargs):
		pyTerm = kwargs["pyTerm"]
		try:
			sequence = kwargs["sequence"][0]
		except IndexError:
			sequence = ""
		if sequence == "..":
			currentPath = pyTerm.getPath().split("/")[::-1]
			currentPath = currentPath[1::]
			if currentPath[0] == '':
				pyTerm.setPath('/')
			else:
				currentPath = currentPath[::-1]
				currentPath = "/".join(currentPath)
				pyTerm.setPath(currentPath)

		elif sequence == "":
			pyTerm.setPath("/home/"+pyTerm.getUser())