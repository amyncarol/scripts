#!/home/yaocai/app/bin/python
##python2.7.9 pymatgen 4.5
from pymatgen.io.vasp.outputs import Vasprun
import os
##hey!!!
with open('Eg_result', 'w') as f:
	for folder in os.listdir('.'):
		if os.path.isdir(folder):
			f.write(folder)
			f.write(' ')
					
			vr = Vasprun(os.path.join(folder,"vasprun.xml"))
			eg = vr.eigenvalue_band_properties[0]
			efermi = vr.efermi
			vbm = vr.eigenvalue_band_properties[2]
			energy = vr.final_energy
			a = vr.structures[0].lattice.a

			eig = [vr.eigenvalues[i] for i in vr.eigenvalues]
			occu = [i.tolist() for i in eig]
			occu_flat = [i[1] for sublist in occu for subsublist in sublist for i in subsublist]
			occu_set = set(occu_flat)

			f.write(str(a))
			f.write(' ')

			f.write(str(energy))
			f.write(' ')
			
			if efermi < vbm:
				f.write('0')
			elif len(occu_set) > 2:	
				f.write('0')
			else:
				f.write(str(eg))
			f.write('\n')
