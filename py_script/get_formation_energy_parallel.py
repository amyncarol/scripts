#!/home/yaocai/app/bin/python
##python 2.7.9 pymatgen4.5.0
import os
from mpi4py import MPI
from mmtools.utilsvasp_folder_analysis import VasprunAnalyzer
from pymatgen.io.vasp.outputs import Vasprun


comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

mode = MPI.MODE_CREATE | MPI.MODE_WRONLY 
f = MPI.File.Open(comm, "formation_result_test", mode)

if rank == 0:
	compounds = []
	for folder in os.listdir('.'):
		if os.path.isdir(folder):
			compounds.append(folder)
	print("there are {} compounds in total".format(len(compounds)))
else:
	compounds = None
compounds = comm.bcast(compounds, root=0)

for j in range(rank, (len(compounds)//size+1)*size, size):
	if j < 	len(compounds):
		try:
			folder = compounds[j]
			line = str(folder) + ' '  
			vr = Vasprun(os.path.join(folder,"vasprun.xml"))
			energy = VasprunAnalyzer(vr).get_formation_energy()
			line += str(energy)
			line += '\n'
		except:
			line = 'None 1000\n'
	else:
		line = 'None 1000\n'
	f.Write_ordered(line)

f.Close()






			
