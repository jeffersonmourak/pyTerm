from Getch import getch
from ui import PyTermUI
from core import screen

class Shell(object):

	def __init__(self,config):
		self.config = config
		self.pyTermUI = PyTermUI(self.config)

	def backspace(self,string):
		if len(string) > 0:
			string = list(string)
			del string[-1]
			return ''.join(string)
		return ""

	def listener(self):

		screen.render(self.pyTermUI.preText())
		may_i_continue = True
		string_query = ''
		while may_i_continue:
			char_data = getch()
			pressedKey = ord(char_data)

			if pressedKey == 12:
				screen.clearScreen()
				string_query = ''
			elif pressedKey == 127:
				screen.clearLine()
				string_query = self.backspace(string_query)
			elif pressedKey == 3:
				return "{{BREAKAPPLICATION}}"
			else:
				string_query += char_data

			commands = string_query.split()
			screen.render(self.pyTermUI.preText() + string_query, self.pyTermUI.check(commands))

			if pressedKey == 13:
				screen._breakLine()

			may_i_continue = False if pressedKey == 13 or pressedKey == 3 else True

	 	return string_query