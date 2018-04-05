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
from pymatgen.io.vaspio import Vasprun
from pymatgen import MPRester
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.phasediagram.pdmaker import PhaseDiagram
from pymatgen.phasediagram.pdanalyzer import PDAnalyzer
from get_e_above_hull import get_e_above_hull

Fail_log = open ('Fail_hull.log','w')
data = open('screen_list_Cl','r')
hull_all = open('hull_Cl_all','w')
hull_30 = open('hull_Cl_30','w')
hull_30_50 = open('hull_Cl_30_50','w')
lines = data.readlines()
for line in lines:
    match = re.match(r"([a-z]+)([ ]+)([a-z]+)([ ]+)([a-z]+)([ ]+)([a-z]+)", line, re.I)
    if match:
        items = match.groups()
	Aele_Screen=items[0]
	Bele_Screen=items[2]
	Cele_Screen=items[4]
	Dele_Screen=items[6]
	currentfolder=Aele_Screen+'2'+Bele_Screen+'1'+Cele_Screen+'1'+Dele_Screen+'6'

	try:
		v = Vasprun(os.path.join(currentfolder,'vasprun.xml'))	
		hull_value = get_e_above_hull(v)
		print >>hull_all, Aele_Screen, Bele_Screen,Cele_Screen,Dele_Screen, hull_value	
		if hull_value < 0.03:
			print >>hull_30, Aele_Screen, Bele_Screen,Cele_Screen,Dele_Screen, hull_value
		elif hull_value < 0.05:
			print >>hull_30_50, Aele_Screen, Bele_Screen,Cele_Screen,Dele_Screen, hull_value

	except:
		print >> Fail_log, currentfolder
			
			
