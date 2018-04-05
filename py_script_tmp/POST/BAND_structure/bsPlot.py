#!/usr/local/bin/python
from pymatgen.io.vasp,outputs import Vasprun
from pymatgen.electronic_structure.plotter import BSPlotter
"""
for quick check
"""

v = Vasprun("vasprun.xml")

bs = v.get_band_structure(line_mode=True)

plotter = BSPlotter(bs)

plotter.show()





