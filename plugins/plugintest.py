class plugintest(object):

	def __pytermconfig__(self):
		return {"command":"pluginTest","callback":self.test}

	def test(self):
		print "This is a test"