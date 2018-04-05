#!/home/yaocai/app/bin/python
##python 2.7.9 pymatgen4.5.0
from get_e_above_hull import get_formation_energy
from pymatgen.io.vasp.outputs import Vasprun
import os

with open('formation_energy_result', 'w') as f:
        for folder in os.listdir('.'):
		if os.path.isdir(folder):
                	f.write(folder)
                	f.write(' ')
                	try:                
                		vr = Vasprun(os.path.join(folder,"vasprun.xml"))
                		energy = get_formation_energy(vr)
                		f.write(str(energy))
			except:
				f.write(str(1000))
                	f.write('\n')






			
