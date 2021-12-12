import sys
import os
from config import modules
for module in modules:
    exec(f"import {module}")

commands = []

sys.path.append("cmds/single")

os.chdir("cmds")
folders = os.listdir()
folders.remove("single")
os.chdir("..")
for folder in folders:
    os.chdir("cmds/" + folder)
    files = os.listdir()
    os.chdir("../..")
    if "requirements.txt" in files:
        files.remove("requirements.txt")
    if "__pycache__" in files:
        files.remove("__pycache__")
    sys.path.append("cmds/" + folder)
    for file in files:
        commands.append(file.replace('.py', ''))
        exec(f"from {file.replace('.py', '')} import {file.replace('.py', '')}")

def compile(cmd):
    global commands
    if not cmd[0] in commands:
        print("[ERROR] Command is not found.")
        return
    str = ""
    if len(cmd) != 1:
        args = cmd[1].split(";")
        str = args[0]
        args.remove(args[0])
        for index, item in enumerate(args):
            args[index] = item.strip()
            str += f", {args[index]}"
    try:
        exec(f"{cmd[0]}({str})")
    except SyntaxError:
        print("[ERROR] Wrong syntax.")
    except TypeError:
        print("[ERROR] Wrong syntax.")
    except NameError:
        print("[ERROR] Wrong syntax.")

while True:
    compile(input(">").split(" ", 1))
