#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import shutil
import subprocess
import tarfile

def compress() :
	for i in my_range(0, 7.0, 0.1) :
		currentFolder = "U" + "{:3.1f}".format(i)
		make_tarfile(currentFolder + "_vasprun.xml", currentFolder + "/vasprun.xml")

def my_range(start, end, step):
	while start <= end:
		yield start
		start += step


def make_tarfile(output_filename, source_file):
	tar = tarfile.open(output_filename + ".tar.gz", "w:gz")
	tar.add(source_file)
	tar.close()

if __name__ == "__main__":
	compress()