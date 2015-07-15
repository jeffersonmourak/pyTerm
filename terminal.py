import subprocess
import sys
import os
import getpass
import socket

def loadAllCommands():

	command = subprocess.Popen(['bash','./listCommands.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	commands, err = command.communicate()

	commands += " PyTerm"
	return commands.split()


class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class _Getch:
	"""Gets a single character from standard input.  Does not echo to the
screen."""
	def __init__(self):
		try:
			self.impl = _GetchWindows()
		except ImportError:
			self.impl = _GetchUnix()
 
	def __call__(self): return self.impl()
 
 
class _GetchUnix:
	def __init__(self):
		import tty, sys
 
	def __call__(self):
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch
 
 
class _GetchWindows:
	def __init__(self):
		import msvcrt
 
	def __call__(self):
		import msvcrt
		return msvcrt.getch()
 

allCommands = loadAllCommands()
getch = _Getch()
 
def findTheCommand(query):
	for command in allCommands:
		if command == query:
			return True

	return False

def preText():
	userName = getpass.getuser()
	computerName = socket.gethostname()
	currentDir = os.path.dirname(os.path.abspath(__file__))
	return "\r(PyTerm)" + userName +"@" + computerName +":" + currentDir.replace("/home/" + userName, "~") + "$ "

def getCommands():
	may_i_continue = True
	string_query = ''
	print preText(),

	while may_i_continue:
		char_data = getch()
		pressedKey = ord(char_data)

		#print str(pressedKey)

		if pressedKey == 12:
			os.system('clear')
			print preText() + "%s" % string_query + " ",
		elif pressedKey == 127:
			string_query = string_query[:-1]
			print preText() + "%s" % string_query + " ",
			print preText() + "%s" % string_query,
		elif not pressedKey == 3:
			string_query += char_data
			print preText() + "%s" % string_query,
		elif pressedKey == 3:
			return "{{BREAKAPPLICATION}}"
 		
		
		
		

		commands = string_query.split()
		
		try:

			separator = " " if len(commands) > 1 else ""

			if findTheCommand(commands[0]):

				print preText() + bcolors.BOLD + bcolors.OKGREEN + commands[0] + bcolors.ENDC + separator + ' '.join(commands[1::]),
			else:
				print preText() + bcolors.BOLD + bcolors.FAIL + commands[0] + bcolors.ENDC + separator + ' '.join(commands[1::]),

			may_i_continue = False if pressedKey == 13 or pressedKey == 3 else True
		except IndexError:
			pass

		
 		
 	return string_query

print ""

def runCommand(commandString):

	commandLine = commandString.split()
	if not commandString == "{{BREAKAPPLICATION}}" and len(commandLine) > 0:
		
		print ""
		test = subprocess.Popen(commandLine, stdout=subprocess.PIPE)
		output = test.communicate()[0]
		print output
		
	elif commandString == "{{BREAKAPPLICATION}}":
		return False

	print ""
	runCommand(getCommands())

os.system('clear')

runCommand(getCommands())