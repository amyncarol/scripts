__author__ = 'HongDing'

## used to generate Chan's style Calculation PRL 105, 196403 (2010)

import shutil
import os
import glob
from pymatgen.io.vaspio.vasp_input import Potcar,Poscar,Incar
from pymatgen.io.vaspio.vasp_output import Vasprun,Outcar
from pymatgen.core.periodic_table import Element

N_number_sp = {-1:52,0:68,1:87} # min, best, max
N_number_spd = {-1:59,0:72,1:88} # min, best, max
cal_choice = 0 # -1:min, 0: best, 1:max
cal_files = ['INCAR','KPOINTS','POTCAR','POSCAR']
current_dir = os.path.dirname(os.path.realpath(__file__))

for folder in glob.glob('*'):
    if os.path.isdir(folder):
        try:
            os.chdir(folder)
            pot = Potcar.from_file('POTCAR')
            pos = Poscar.from_file('POSCAR')
            out = Outcar('OUTCAR')
            inc = Incar.from_file('INCAR')
            num_atom = dict(zip(pos.site_symbols,pos.natoms))
            Tot_nvalele = 22
            d_element = False
	    group_sum = 0
            for entry in pot:
                group_sum += Element(entry.element).group
                d_element = d_element or Element(entry.element).is_transition_metal
	    if d_element:
		Tot_nvalele += group_sum-18
		n = float(Tot_nvalele)/N_number_spd[cal_choice] 
	    else:
		Tot_nvalele = 26
		n = float(Tot_nvalele)/N_number_sp[cal_choice]
            if  True: 
		nele_cal = out.nelect
                ### E(N0+n)
		
                newfolder = 'Plus_26_68'
                if not os.path.exists(newfolder):
                    os.mkdir(newfolder)
                for file in cal_files:
                    shutil.copyfile(file,os.path.join(newfolder,file))

                update_incar_param = {'NELECT':nele_cal+n,'ISIF':2,'NSW':0}
                inc.update(update_incar_param)
                inc.write_file(os.path.join(newfolder,'INCAR'))

                ### E(N0-n)
                newfolder = 'Minus_26_68'
                if not os.path.exists(newfolder):
                        os.mkdir(newfolder)

                for file in cal_files:
                        shutil.copyfile(file,os.path.join(newfolder,file))

                update_incar_param = {'NELECT':nele_cal-n,'ISIF':2,'NSW':0}
                inc.update(update_incar_param)
                inc.write_file(os.path.join(newfolder,'INCAR'))

            else:
                print "Valence electron numbers do not match"
        except:
            print folder

        os.chdir(current_dir)
