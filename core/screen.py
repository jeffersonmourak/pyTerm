import sys
import subprocess
import shlex
from blessings import Terminal
import os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.sys.path.insert(0,parentdir) 
from decorate import bcolors

term = Terminal()
renderLine = 1
linesToBreak = 1
def render(string, keyword="" ,breakLine=False):
	clearLine()
	with term.location(0, renderLine):
		if not keyword == "":
			print highlight(string, keyword)
		else:
			print string
			global linesToBreak
			linesToBreak = (len(string) / term.width) + 1
		if breakLine:
			_breakLine()
	resetCursor(len(string))

def resetCursor(pos):
	sys.stdout.flush()

def highlight(string, keyword, AS = "correct"):
	array = string.split(" ")
	for i,word in enumerate(array):
		if word == keyword:
			if AS == "correct":
				array[i] = markCorrect(word)
			elif AS == "incorrect":
				array[i] = markIncorrect(word)
			break

	string = " ".join(array)
	return string

def markCorrect(string):
	return bcolors.BOLD + bcolors.OKGREEN + string + bcolors.ENDC

def markIncorrect(string):
	return bcolors.BOLD + bcolors.FAIL + string + bcolors.ENDC

def clearLine():
	for i in range(renderLine, term.height - renderLine):
		with term.location(0, i):
			print " " * term.width

def clearScreen():
	for i in range(term.height):
		with term.location(0, i):
			print " " * term.width

def _breakLine():
	global renderLine, linesToBreak
	renderLine += linesToBreak
	linesToBreak = 1