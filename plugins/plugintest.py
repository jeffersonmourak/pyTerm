class plugintest(object):

	def __pytermconfig__(self):
		return {"command":"pluginTest","callback":self.test}

	def test(self,*args, **kwargs):
		pyTerm = kwargs["pyTerm"]

		print pyTerm.getPath()

		print "This is a test"