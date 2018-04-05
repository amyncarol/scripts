#!/usr/bin/python
#python2.7.9 pymatgen4.5.0

import os
import fileinput
import sys
import re
import string
import shutil
from pymatgen.io.vasp.outputs import Vasprun
from pymatgen.io.vasp.inputs import Poscar
from pymatgen.core.periodic_table import Element
from pymatgen.io.vasp.sets import MPRelaxSet


Fail_log = open ('Fail.log','w')
Pre_Dir = '/home/yaocai/Ab/2116/InTl/5atom/relax/complete'
for i in os.listdir(Pre_Dir):
	if os.path.isdir(os.path.join(Pre_Dir, i)):
        	currentfolder = i
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
			
