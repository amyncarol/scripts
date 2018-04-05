#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import shutil
import subprocess

def URamp() :
	for i in my_range(0, 7, 0.1) :
		currentFolder = "U" + "{:3.1f}".format(i)
		lastFolder = "U" + "{:3.1f}".format(i - 0.1)
		if os.path.exists(currentFolder) :
			shutil.rmtree("U" + "{:3.1f}".format(i))
		if i == 0 :
			shutil.copytree("base", currentFolder)
		else :
			shutil.copytree(lastFolder, currentFolder)  

		shutil.copy(currentFolder + "/CONTCAR", currentFolder + "/POSCAR")

		try:
			os.remove(lastFolder + "/WAVECAR")
		except OSError:
			pass
		
		if i != 0 :
			with open(currentFolder + "/INCAR_new", "wt") as fout:
				with open(currentFolder + "/INCAR", "rt") as fin:
					for line in fin:
						fout.write(line.replace('LDAUU= 0 ' + "{:3.1f}".format(i - 0.1) + ' 0', 'LDAUU= 0 ' + "{:3.1f}".format(i) + ' 0'))
			os.remove(currentFolder + "/INCAR")
			os.rename(currentFolder + "/INCAR_new", currentFolder + "/INCAR")

		subprocess.call(["sh", "/home/yaocai/submit.sh", currentFolder, "64", "c"]) 
		try:
			os.remove(currentFolder + "/finish")
		except OSError:
			pass

		flag = True
		while flag :
			if os.path.exists(currentFolder + "/finish") :
				flag = False


def my_range(start, end, step):
	while start <= end:
		yield start
		start += step

if __name__ == "__main__":
	URamp()
