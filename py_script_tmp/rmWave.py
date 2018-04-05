#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import shutil
import subprocess

def rmWave() :
	for i in my_range(0, 3.9, 0.1) :
		currentFolder = "U" + "{:3.1f}".format(i)
		try:
			os.remove(currentFolder + "/WAVECAR")
		except OSError:
			pass

def my_range(start, end, step):
	while start <= end:
		yield start
		start += step

if __name__ == "__main__":
	rmWave()			