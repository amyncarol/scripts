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

Aele_Screen=['K','Rb','Cs']
Bele_Screen=['Ag','Cu','K','Na','Li']
Cele_Screen=['Bi','Sb','Ce','Pr','Nd','Ta','Mo','Y']
#['Al','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Ga','Ge','As','Y','Zr','Nb',
#'Mo','Ru','Rh','Ag','In','Sb','La','Ce','Pr','Nd','Sm','Eu','Gd','Tb','Dy','Ho',
#'Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Au','Tl','Bi']
Dele_Screen=['F','Cl','Br','I']

Pre_Dir = '/home/zzy/216-Screening/Result' 

Fail_log = open ('Fail_Eg.log','w')
Eg_Result = open ('Eg','w')

mpvis = MPVaspInputSet()
for i in range(len(Aele_Screen)):
	for j in range(len(Bele_Screen)):
		for k in range(len(Cele_Screen)):
			for l in range(len(Dele_Screen)):
				currentfolder=Aele_Screen[i]+'2'+Bele_Screen[j]+'1'+Cele_Screen[k]+'1'+Dele_Screen[l]+'6'

				try:
					Eg = Vasprun(os.path.join(currentfolder,'vasprun.xml.relax')).eigenvalue_band_properties[0]
					if Eg > 0.6 and Eg < 1.7:
						print >>Eg_Result, Aele_Screen[i], Bele_Screen[j],Cele_Screen[k],Dele_Screen[l], Eg	

				except:
					print >> Fail_log, currentfolder
			
			
