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
Pre_Dir = '/home/yaocai/Ab/2116/dos_full/1batch'
with open('/home/yaocai/Ab/2116/HSE_stampede/screen_list_hse_50meV_1.5direct_nonzerogap', 'r') as f:
    for i in f:
        currentfolder = i.strip()
        try:
            if not os.path.exists(currentfolder):
                os.mkdir(currentfolder)
                
            v = Vasprun(os.path.join(Pre_Dir,currentfolder,'vasprun.xml'))
            struc = v.structures[-1]
            mpvis = MPRelaxSet(struc)
            poscar = mpvis.poscar
            poscar.write_file(os.path.join(currentfolder,'POSCAR'))
            potcar = mpvis.potcar
            potcar.write_file(os.path.join(currentfolder,'POTCAR'))

            #shutil.copyfile(os.path.join(Pre_Dir,currentfolder,'CHGCAR'),os.path.join(currentfolder,'CHGCAR'))
            shutil.copyfile(os.path.join('INCAR'),os.path.join(currentfolder,'INCAR'))
            shutil.copyfile(os.path.join('KPOINTS'),os.path.join(currentfolder,'KPOINTS'))                  
        except:
            print >> Fail_log, currentfolder
            
