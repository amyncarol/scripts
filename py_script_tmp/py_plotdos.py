#!/usr/bin/env python


"""
plot selected site projected Dos

e.g py_plotdos 5 6 7 8
    plot the projected dos on atom 5 6 7 and 8
"""

import argparse
import os
import re
import logging
import multiprocessing
import sys
import datetime

from collections import OrderedDict

from pymatgen import Structure
from pymatgen.io.vaspio import Outcar, Vasprun, Chgcar
from pymatgen.util.string_utils import str_aligned
from pymatgen.apps.borg.hive import SimpleVaspToComputedEntryDrone, \
    VaspToComputedEntryDrone
from pymatgen.apps.borg.queen import BorgQueen
from pymatgen.electronic_structure.plotter import DosPlotter
from pymatgen.io.vaspio import Poscar
from pymatgen.io.cifio import CifParser, CifWriter
from pymatgen.io.vaspio_set import MPVaspInputSet, MITVaspInputSet
from pymatgen.io.cssrio import Cssr
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.alchemy.materials import TransformedStructure
from pymatgen.analysis.diffraction.xrd import XRDCalculator
from prettytable import PrettyTable


def plot_dos():

    v = Vasprun("./vasprun.xml")
    dos = v.complete_dos

    all_dos = OrderedDict()
    # all_dos["Total"] = dos

    structure = v.final_structure

    for i in sys.argv[1:]:
    	site = structure[int(i)-1]
    	all_dos["Site " + i + " " + site.specie.symbol] = dos.get_site_dos(site)
    # if args.site:
    #     for i in range(len(structure)):
    #         site = structure[i]
    #         all_dos["Site " + str(i) + " " + site.specie.symbol] = \
    #             dos.get_site_dos(site)

    # if args.element:
    #     syms = [tok.strip() for tok in args.element[0].split(",")]
    #     all_dos = {}
    #     for el, dos in dos.get_element_dos().items():
    #         if el.symbol in syms:
    #             all_dos[el] = dos
    # if args.orbital:
    #     all_dos = dos.get_spd_dos()

    plotter = DosPlotter()
    plotter.add_dos_dict(all_dos)
    plotter.get_plot().savefig("tmp_dos")
 
if __name__ == "__main__":
    plot_dos()