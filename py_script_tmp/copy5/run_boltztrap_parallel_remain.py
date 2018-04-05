#!/home/yaocai/app/bin/python
##python2.7.9 pymatgen 4.5
from mpi4py import MPI
import pandas as pd
import os
import re
from pymatgen.electronic_structure.boltztrap2 import BoltztrapAnalyzer, BoltztrapRunner
from pymatgen.io.vasp.outputs import Vasprun

def run_boltztrap(path_of_folder, scissor, doping):
	"""
	path_of_folder: 
	scissor: the gap of the scissor operation
	doping: list of doping,i.e.[1e16,1e17]
	"""
	#define pn_doping
	pn_doping = []
	pn_doping.extend([i for i in doping])
	pn_doping.extend([0-i for i in doping])
	#get number of electrons
	with open(os.path.join(path_of_folder, 'vasprun.xml'),'r') as f:
		vasprun_mat = f.readlines()
	for line in vasprun_mat:
		match = re.match(r"([ \<i]+)(name=\"NELECT\"\>)([ ]+)([0-9.]+)(\</i\>)", line, re.I)
		if match:
			items = match.groups()
			nelect = int(float(items[3]))
			#get band structure
			bands = Vasprun(os.path.join(path_of_folder, 'vasprun.xml')).get_band_structure()
			#run boltztrap
			b_run = BoltztrapRunner(bs = bands, nelec = nelect, 
					scissor = scissor,
					doping=doping, tmax=300,
					energy_span_around_fermi=1.5)
			#path of boltztrap files
			path_dir = b_run.run(path_dir=path_of_folder)
			break

if __name__ == "__main__":
	comm = MPI.COMM_WORLD
	size = comm.Get_size()
	rank = comm.Get_rank()

	if rank == 0:
		b = pd.read_csv('remain_eff', names = ['ID', 'Compound'])
        	compounds = b['Compound'].values.tolist()
		print("there are {} compounds in total".format(len(compounds)))
	else:
		compounds = None
	compounds = comm.bcast(compounds, root=0)

	for j in range(rank, len(compounds), size):
		folder = compounds[j]
		try:
			directory = os.path.dirname(os.path.realpath(__file__))  ##directory .py file is in
			path_of_folder = os.path.join(directory, folder)
			run_boltztrap(path_of_folder=path_of_folder, scissor=0, doping=[1e16, 1e17, 1e18, 1e19, 1e20])
		except:
			print(folder)




