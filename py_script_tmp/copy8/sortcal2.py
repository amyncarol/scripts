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


Fail_log = open('Fail.log','w')
data = open('screen_list_FBrI','r')
lines = data.readlines()
for line in lines:
    match = re.match(r"([a-z]+)([ ]+)([a-z]+)([ ]+)([a-z]+)([ ]+)([a-z]+)", line, re.I)
    if match:
        items = match.groups()
	Aele_Screen=items[0]
	Bele_Screen=items[2]
	Cele_Screen=items[4]
	Dele_Screen=items[6]
	try:
		currentfolder=Aele_Screen+'2'+Bele_Screen+'1'+Cele_Screen+'1'+Dele_Screen+'6'
		if not os.path.exists(currentfolder):
                        os.mkdir(currentfolder)
			struc = Poscar.from_file('temp_POSCAR').structure
			struc.replace_species({Element('Cs'):Element(Aele_Screen),Element('Ag'):Element(Bele_Screen),Element('Au'):Element(Cele_Screen),Element('Cl'):Element(Dele_Screen)})
			mpvis = MPRelaxSet(struc)
			poscar = mpvis.poscar
			poscar.write_file(os.path.join(currentfolder,'POSCAR'))
                	potcar = mpvis.potcar
               		potcar.write_file(os.path.join(currentfolder,'POTCAR'))
                	shutil.copyfile(os.path.join('INCAR_relax'),os.path.join(currentfolder,'INCAR'))
                	shutil.copyfile(os.path.join('KPOINTS_relax'),os.path.join(currentfolder,'KPOINTS'))
	except:
		print >> Fail_log, currentfolder
			
