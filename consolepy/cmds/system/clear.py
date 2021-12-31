import os
import sys

def clear():
	if sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")
