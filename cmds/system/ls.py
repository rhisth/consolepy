import os

def ls(path="."):
	try:
		list = (os.listdir(path=path))
	except PermissionError:
		print("No permission")
	else:
		for el in list:
			print(el)
