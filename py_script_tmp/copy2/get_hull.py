#!/home/yaocai/app/bin/python
##python 2.7.9 pymatgen4.5.0
from pymatgen.io.vasp.outputs import Vasprun
import os
from get_e_above_hull import get_e_above_hull

with open('Hull_result', 'w') as f:
        for folder in os.listdir('.'):
		if os.path.isdir(folder):
                	f.write(folder)
                	f.write(' ')
                	try:                
                		vr = Vasprun(os.path.join(folder,"vasprun.xml"))
                		(decomp, hull) = get_e_above_hull(vr)
                		f.write(str(hull))
				f.write(' ')
				for compound in decomp:
					f.write(str(compound))
					f.write(' ')
			except:
				f.write(str(1000))
                	f.write('\n')






			
