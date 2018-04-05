#!/home/yaocai/app/bin/python
##python2.7.9 pymatgen 4.5
from pymatgen.io.vasp.outputs import Vasprun
import os
from mpi4py import MPI
from math import ceil

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

mode = MPI.MODE_CREATE | MPI.MODE_WRONLY 
f = MPI.File.Open(comm, "Eg_result", mode)

if rank == 0:
	compounds = []
	for folder in os.listdir('.'):
		if os.path.isdir(folder):
			compounds.append(folder)
	print("there are {} compounds in total".format(len(compounds)))
	#line = 'Compound my_eg bs_eg bs_direct_eg'
	#f.Write_ordered(line)
else:
	compounds = None
compounds = comm.bcast(compounds, root=0)


for j in range(rank, (len(compounds)/size+1)*size, size):
	if j < 	len(compounds):
		try:
			folder = compounds[j]		
			line = str(folder) + ' '
			vr = Vasprun(os.path.join(folder,"vasprun.xml"))
			eg = vr.eigenvalue_band_properties[0]
			efermi = vr.efermi
			vbm = vr.eigenvalue_band_properties[2]

			eig = [vr.eigenvalues[i] for i in vr.eigenvalues]
			occu = [i.tolist() for i in eig]
			occu_flat = [i[1] for sublist in occu for subsublist in sublist for i in subsublist]
			occu_set = set(occu_flat)
					
			if efermi < vbm:
				line += '0 '
			elif len(occu_set) > 2:	
				line += '0 '
			else:
				line += str(eg) + ' '
			bs = vr.get_band_structure()
			line += str(bs.get_band_gap()['energy']) + ' '
			line += str(bs.get_direct_band_gap()) + '\n'
		except:
			line = 'None 0.0 0.0 0.0\n'
	else:
		line = 'None 0.0 0.0 0.0\n'

	f.Write_ordered(line)
	#print("rank {} finishes {}".format(rank, folder))
#comm.Barrier()
f.Close()


