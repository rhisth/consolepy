import os
import sys

def exit():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
    sys.exit(0)
