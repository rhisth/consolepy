import sys
import os

from config import argument_separator
modules = []
commands = []

os.chdir("cmds")
folders = os.listdir()
os.chdir("..")
for folder in folders:
    os.chdir("cmds/" + folder)
    files = os.listdir()
    if "requirements.txt" in files:
        file = open("requirements.txt", "r")
        for el in file:
            if not el in modules:
                el = el.replace("\n", "")
                modules.append(el)
        files.remove("requirements.txt")
        file.close()
    os.chdir("../..")
    if "__pycache__" in files:
        files.remove("__pycache__")
    sys.path.append("cmds/" + folder)
    for file in files:
        commands.append(file.replace('.py', ''))
        exec(f"from {file.replace('.py', '')} import {file.replace('.py', '')}")

for module in modules:
    exec(f"import {module}")

if sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")

def compile(cmd):
    global commands
    if not cmd[0] in commands:
        print("[ERROR] Command is not found.")
        return
    str = ""
    if len(cmd) != 1:
        args = cmd[1].split(argument_separator)
        str += ",".join(list(map(lambda x: x.strip(), args)))
    try:
        exec(f"{cmd[0]}({str})")
    except SyntaxError:
        print("[ERROR] Wrong syntax.")
    except TypeError:
        print("[ERROR] Wrong syntax.")
    except NameError:
        print("[ERROR] Wrong syntax.")

while True:
    compile(input(f"{os.getcwd()}>").split(" ", 1))
