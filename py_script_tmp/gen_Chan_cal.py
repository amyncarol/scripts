__author__ = 'HongDing'

## used to generate Chan's style Calculation PRL 105, 196403 (2010)

import shutil
import os
from pymatgen.io.vaspio.vasp_input import Potcar,Poscar,Incar
from pymatgen.io.vaspio.vasp_output import Vasprun,Outcar


pot = Potcar.from_file('POTCAR')
pos = Poscar.from_file('POSCAR')
out = Outcar('OUTCAR')
inc = Incar.from_file('INCAR')
num_atom = dict(zip(pos.site_symbols,pos.natoms))
Tot_atom = 0
Tot_nvalele = 0

for entry in pot:
	print entry.element, entry.nelectrons,num_atom[entry.element]
	Tot_atom += num_atom[entry.element]
	Tot_nvalele = 26.0 * (Tot_atom/5.0)


N_number = {-1:52,0:68,1:87} # min, best, max

cal_choice = 0 # -1:min, 0: best, 1:max 

cal_files = ['INCAR','KPOINTS','POTCAR','POSCAR']


print out.nelect
print Tot_nvalele

n = Tot_nvalele/N_number[cal_choice]

### E(N0+n)
folder = 'Plus_26_68_relax'
if not os.path.exists(folder): 
	os.mkdir(folder)
for file in cal_files:
	shutil.copyfile(file,os.path.join(folder,file))
update_incar_param = {'NELECT':out.nelect+n,'ISIF':2}
inc.update(update_incar_param)
inc.write_file(os.path.join(folder,'INCAR'))

### E(N0-n)	
folder = 'Minus_26_68_relax'
if not os.path.exists(folder): 
        os.mkdir(folder)

for file in cal_files:
        shutil.copyfile(file,os.path.join(folder,file))
update_incar_param = {'NELECT':out.nelect-n,'ISIF':2}
inc.update(update_incar_param)
inc.write_file(os.path.join(folder,'INCAR'))	

