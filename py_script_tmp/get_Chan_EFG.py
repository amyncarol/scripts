__author__ = 'HongDing'
#used to read files
import os
from pymatgen.io.vaspio.vasp_output import Vasprun,Outcar
from pymatgen.io.vaspio.vasp_input import Potcar,Poscar,Incar

filename = 'vasprun.xml'
N_number = {-1:52,0:68,1:87} # min, best, max
cal_choice = 0 # -1:min, 0: best, 1:max 


vr = Vasprun(os.path.join(filename))
E0 = vr.final_energy
print E0

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
n = Tot_nvalele/N_number[cal_choice]
print n

vr_Minus = Vasprun(os.path.join('Minus_26_68_relax',filename))
E0_Minus = vr_Minus.final_energy
        
print E0_Minus

vr_Plus = Vasprun(os.path.join('Plus_26_68_relax',filename))
E0_Plus = vr_Plus.final_energy
print E0_Plus

E_FG = (E0_Plus+E0_Minus-2*E0)/n
        
print 'E_FG = %s' % (E_FG) 



