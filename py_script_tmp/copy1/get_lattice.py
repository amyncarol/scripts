#!/home/yaocai/app/bin/python
##python2.7.9 pymatgen 4.5
from pymatgen.io.vasp.outputs import Vasprun
import os
from mpi4py import MPI
from math import ceil, sqrt

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

mode = MPI.MODE_CREATE | MPI.MODE_WRONLY 
f = MPI.File.Open(comm, "lattice_result", mode)

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
			a = vr.final_structure.lattice.a * sqrt(2)
			line += str(a) + '\n'

		except:
			line = 'None 0.0\n'
	else:
		line = 'None 0.0\n'

	f.Write_ordered(line)
	#print("rank {} finishes {}".format(rank, folder))
#comm.Barrier()
f.Close()


