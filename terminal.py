import subprocess
import sys
from shell import *
from CommandsList import *

def runCommand(commandString):

	if commands.run(commandString):
		runCommand(shell.listener())

os.system('clear')

runCommand(shell.listener())