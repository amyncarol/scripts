#!/home/yaocai/app/bin/python
##python2.7.9 pymatgen 4.5
from pymatgen.io.vasp.outputs import Vasprun
import os
import mpi4py

with open('Eg_result', 'w') as f:
	for folder in os.listdir('.'):
		if os.path.isdir(folder):
			f.write(folder)
			f.write(' ')
					
			vr = Vasprun(os.path.join(folder,"vasprun.xml"))
			eg = vr.eigenvalue_band_properties[0]
			efermi = vr.efermi
			vbm = vr.eigenvalue_band_properties[2]

			eig = [vr.eigenvalues[i] for i in vr.eigenvalues]
			occu = [i.tolist() for i in eig]
			occu_flat = [i[1] for sublist in occu for subsublist in sublist for i in subsublist]
			occu_set = set(occu_flat)
			
			if efermi < vbm:
				f.write('0')
			elif len(occu_set) > 2:	
				f.write('0')
			else:
				f.write(str(eg))


			bs = vr.get_band_structure()
			f.write(' ')
			f.write(str(bs.get_band_gap()['energy']))
			f.write(' ')
			f.write(str(bs.get_direct_band_gap()))

			f.write('\n')
