from Getch import getch
from ui import PyTermUI

class Shell(object):

	def __init__(self,config):
		self.config = config
		self.pyTermUI = PyTermUI(self.config)

	def listener(self):

		may_i_continue = True
		string_query = ''
		print self.pyTermUI.preText(),

		while may_i_continue:
			char_data = getch()
			pressedKey = ord(char_data)

			#print str(pressedKey)

			if pressedKey == 12:
				os.system('clear')
				print self.pyTermUI.preText() + "%s" % string_query + " ",
			elif pressedKey == 127:
				string_query = string_query[:-1]
				print self.pyTermUI.preText() + "%s" % string_query + " ",
				print self.pyTermUI.preText() + "%s" % string_query,
			elif not pressedKey == 3:
				string_query += char_data
				print self.pyTermUI.preText() + "%s" % string_query,
			elif pressedKey == 3:
				return "{{BREAKAPPLICATION}}"

			commands = string_query.split()

			self.pyTermUI.check(commands)

			may_i_continue = False if pressedKey == 13 or pressedKey == 3 else True

	 	return string_query