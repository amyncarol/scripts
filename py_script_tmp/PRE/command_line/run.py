from os import listdir
import os
import shutil
import subprocess
from os.path import isfile

currentDir = os.getcwd()

for f in listdir(currentDir):
	if not(isfile(f)):
		print f
		subprocess.call(["sh", "/home/yaocai/submit.sh", f, "64", "c"]) 