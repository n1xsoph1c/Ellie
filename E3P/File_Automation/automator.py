import shutil
import os

# Make package directories
class folder:
	def create(name, path):
		os.mkdir(os.path.join(path, name))

# Make files
class file:
	def create (name, *path):
		if len(path) >= 1:
			with open(os.path.join(path[0], name), "w+") as file:
				file.write(f"#{name}\n\n")
		else:
			with open(name, "w+") as file:
				file.write(f"#{name}\n\n")