import os 
import shutil  

from automator import folder, file

def main(path):
	#Creating a package folder 
	folder.create("Package", path)
	print(f"Created a Folder named \"Package\" at \"{path}\"")

	#Creating some files
	file.create("__init__.py", path)
	print(f"Created a file named \"__init__.py\" at \"{path}\"")
	file.create("main.py", path)
	print(f"Created a file named \"main.py\" at \"{path}\"")
	file.create("Readme.md", path)
	print(f"Created a file named \"Readme.md\" at \"{path}\"")

main("/Users/elain/Desktop/Projects/Python/WinORG")