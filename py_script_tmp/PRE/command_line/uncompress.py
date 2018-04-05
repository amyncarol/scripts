#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import shutil
import subprocess
import tarfile

def uncompress() :
	for i in my_range(0, 7.0, 0.1) :
		currentFolder = "U" + "{:3.1f}".format(i)
		fileName = currentFolder + "_vasprun.xml"
		untar(fileName)
		try:
			os.remove(fileName + ".tar.gz")
		except OSError:
			pass

def my_range(start, end, step):
	while start <= end:
		yield start
		start += step


def untar(source_file):
	tar = tarfile.open(source_file + ".tar.gz")
	tar.extractall()
	tar.close()

if __name__ == "__main__":
	uncompress()