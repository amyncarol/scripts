#!/usr/bin/python
# -*- coding: iso-8859-1 -*- 
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
from pymatgen.symmetry.bandstructure import HighSymmKpath
from pymatgen.io.vasp.inputs import Kpoints

Fail_log = open('Fail.log','w')
Pre_Dir = '/home/yaocai/Ab/2116/solidsolution/complete/BrCl'

for currentfolder in os.listdir(Pre_Dir):
	if os.path.isdir(os.path.join(Pre_Dir,currentfolder)):
		print(currentfolder)
		try:
			if not os.path.exists(currentfolder):
				os.mkdir(currentfolder)
			shutil.copyfile(os.path.join(Pre_Dir,currentfolder,'CONTCAR'),os.path.join(currentfolder,'POSCAR'))
			shutil.copyfile(os.path.join(Pre_Dir,currentfolder,'POTCAR'),os.path.join(currentfolder,'POTCAR'))
			shutil.copyfile(os.path.join(Pre_Dir,currentfolder,'CHGCAR'),os.path.join(currentfolder,'CHGCAR'))
			shutil.copyfile(os.path.join('INCAR'),os.path.join(currentfolder,'INCAR'))
			structure = Poscar.from_file(os.path.join(currentfolder,'POSCAR')).structure
			syp = HighSymmKpath(structure)
			kpoints = Kpoints.automatic_linemode(3, syp)
			kpoints.write_file(os.path.join(currentfolder,'KPOINTS'))
		except:
			print >> Fail_log, currentfolder
			
