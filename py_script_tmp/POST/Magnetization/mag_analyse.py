#!/usr/bin/env python
# -*-coding:utf-8 -*-

import os
import shutil
import subprocess
import pymatgen.io.vaspio as vaspio
from pylab import *

def data():
	U = []
	Nb1 = []
	Nb2 = []
	Nb3 = []
	Nb4 =[]
	for i in my_range(0, 7.0, 0.1) :
		currentFolder = "U" + "{:3.1f}".format(i)
		outcarFile = currentFolder + "/OUTCAR"
		mag = read_Mag(outcarFile)
		U.append(i)
		Nb1.append(mag[4]['d'])
		Nb2.append(mag[5]['d'])
		Nb3.append(mag[6]['d'])
		Nb4.append(mag[7]['d'])
	plotMag(U, Nb1, Nb2, Nb3, Nb4)

def plotMag(U, Nb1, Nb2, Nb3, Nb4):	
	figure(1)
	plot(U, Nb1, label = 'Nb1')
	plot(U, Nb2, label = 'Nb2')
	plot(U, Nb3, label = 'Nb3')
	plot(U, Nb4, label = 'Nb4')
	legend(loc='lower left')

	xlabel('U (eV)')
	ylabel('d orbital magnetization')
	title('')
	grid(True)
	savefig("mag_U.png")
	show()	

def read_Mag(outcarFile):
	outcar = vaspio.Outcar(outcarFile)
	mag = outcar.magnetization
	return mag	

def my_range(start, end, step):
	while start <= end:
		yield start
		start += step

if __name__ == "__main__":
	data()
