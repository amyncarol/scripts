#!/usr/bin/python
# -*- coding: iso-8859-1 -*- 

import os
import fileinput
import sys
import re
import string
import shutil
from pymatgen.io.vaspio.vasp_output import Vasprun
from pymatgen.io.vaspio.vasp_input import Poscar
from pymatgen.core.periodic_table import Element
from  pymatgen.io.vaspio_set import MPVaspInputSet

Fail_log = open ('Fail.log','w')
Pre_Dir = '/home/yaocai/Ab/2116/relax-Cl/complete'
data = open('hull_Cl_30','r')
lines = data.readlines()
for line in lines:
	items = line.split()
	Aele_Screen=items[0]
	Bele_Screen=items[1]
	Cele_Screen=items[2]
	Dele_Screen=items[3]
	currentfolder=Aele_Screen+'2'+Bele_Screen+'1'+Cele_Screen+'1'+Dele_Screen+'6'
	try:
	 	if not os.path.exists(currentfolder):
			os.mkdir(currentfolder)
		shutil.copyfile(os.path.join(Pre_Dir,currentfolder,'CONTCAR'),os.path.join(currentfolder,'POSCAR'))
		shutil.copyfile(os.path.join(Pre_Dir,currentfolder,'POTCAR'),os.path.join(currentfolder,'POTCAR'))
		shutil.copyfile(os.path.join(Pre_Dir,currentfolder,'CHGCAR'),os.path.join(currentfolder,'CHGCAR'))
		shutil.copyfile(os.path.join('INCAR_DOS'),os.path.join(currentfolder,'INCAR'))
		shutil.copyfile(os.path.join('KPOINTS_DOS'),os.path.join(currentfolder,'KPOINTS'))					
	except:
		print >> Fail_log, currentfolder
			
