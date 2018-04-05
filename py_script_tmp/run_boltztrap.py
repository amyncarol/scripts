#!/usr/bin/python
# -*- coding: iso-8859-1 -*- 

def run_boltztrap(path_of_vasprun, scissor, doping):
	"""
	path_of_vasprun: 
	scissor: the gap of the scissor operation
	doping: list of doping,i.e.[1e16,1e17]
	"""
	import os
	import re
	from pymatgen.electronic_structure.boltztrap2 import BoltztrapAnalyzer, BoltztrapRunner
	from pymatgen.io.vasp.outputs import Vasprun
	#define pn_doping
	pn_doping = []
	pn_doping.extend([i for i in doping])
	pn_doping.extend([0-i for i in doping])
	#get number of electrons
	vasprun = open(path_of_vasprun,'r')
        vasprun_mat = vasprun.readlines()
	for line in vasprun_mat:
    		match = re.match(r"([ \<i]+)(name=\"NELECT\"\>)([ ]+)([0-9.]+)(\</i\>)", line, re.I)
		if match:
        		items = match.groups()
			nelect = int(float(items[3]))

			#get band structure
			bands = Vasprun(path_of_vasprun).get_band_structure()
			#run boltztrap
			b_run = BoltztrapRunner(bs = bands, nelec = nelect, 
					scissor = scissor,
					doping=doping, tmax=300,
					energy_span_around_fermi=1.5)
			#path of boltztrap files
			path = os.path.dirname(os.path.realpath(__file__))
			path_dir = b_run.run(path_dir=path)
			break
if __name__ == "__main__":
	gap_HSE = 1.172
	run_boltztrap(path_of_vasprun='vasprun.xml', scissor=gap_HSE, doping=[1e16, 1e17, 1e18, 1e19, 1e20])
