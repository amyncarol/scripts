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

Aele_Screen=['K','Rb','Cs']
Bele_Screen=['Ag','Cu','K','Na','Li']
Cele_Screen=['Bi','Sb','Ce','Pr','Nd','Ta','Mo','Y']
#['Al','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Ga','Ge','As','Y','Zr','Nb',
#'Mo','Ru','Rh','Ag','In','Sb','La','Ce','Pr','Nd','Sm','Eu','Gd','Tb','Dy','Ho',
#'Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Au','Tl','Bi']
Dele_Screen=['F','Cl','Br','I']

Pre_Dir = '/home/zzy/216-Screening/Result' 

Fail_log = open ('Fail_Hull.log','w')
Hull_Result = open ('Hull_0','w')

mpvis = MPVaspInputSet()
for i in range(len(Aele_Screen)):
	for j in range(len(Bele_Screen)):
		for k in range(len(Cele_Screen)):
			for l in range(len(Dele_Screen)):
				currentfolder=Aele_Screen[i]+'2'+Bele_Screen[j]+'1'+Cele_Screen[k]+'1'+Dele_Screen[l]+'6'

				try:
					v = Vasprun(os.path.join(currentfolder,'vasprun.xml.relax'))	
					hull_value = get_e_above_hull(v)
					if hull_value < 0.001:
						print >>Hull_Result, Aele_Screen[i], Bele_Screen[j],Cele_Screen[k],Dele_Screen[l], hull_value
				except:
					print >> Fail_log, currentfolder
			
			
