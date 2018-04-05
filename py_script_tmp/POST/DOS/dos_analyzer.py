"""
Goal of this is to have a set of tasks that can parse dos from halide perovskites...


it gets % band character of 0.5 eV into VBM and CBM...
"""

# import pymatgen.io.vaspio.vasp_output as vr
from pymatgen.io.vasp.outputs import Vasprun 
from pymatgen.core import Element
# import pymatgen.electronic_structure.dos as DOS
# import matplotlib.pyplot as plt
import os
import numpy as np

class Dos_Analyzer:
    def __init__(self,vasprun):
        """
        Takes either a Vasprun object or the name of a vasprun file and makes a Dos_Analyzer
        """
        if type(vasprun) == str:
            vasprun = Vasprun(vasprun)
        if not vasprun.converged:
            print 'warning!! not converged!!'
        cdos=vasprun.complete_dos
        struct=vasprun.final_structure
        energies=cdos.energies
        self.cdos = cdos
        self.struct = struct
        self.energies = energies - vasprun.efermi #shifted to fermi level...
        self.efermi = vasprun.efermi
        bandchar = vasprun.eigenvalue_band_properties
        self.gap = bandchar[0]
        self.cbm = bandchar[1] - vasprun.efermi
        self.vbm = bandchar[2] - vasprun.efermi #shift to fermi level...
        tmpelt_dos = cdos.get_element_dos()
        elt_dos = {}
        elt_pdos = {}
        for elt in list(set(struct.species)):
            elt_dos[elt.symbol] = tmpelt_dos[Element(elt)]
            tmpeltpdos = cdos.get_element_spd_dos(elt.symbol)
            elt_pdos[elt.symbol] = {}
            for orb in tmpeltpdos.keys():
                elt_pdos[elt.symbol][orb.name] = tmpeltpdos[orb]
        self.elt_dos = elt_dos
        self.elt_pdos = elt_pdos

    def get_band_edge_character(self, depth = 0.5):
        #first get indices for tabulating
        vbmind = []
        cbmind = []
        for ind in range(len(self.energies)):
            if (self.energies[ind] <= self.vbm) and (self.energies[ind] >= (self.vbm - depth)):
                vbmind.append(ind)
            elif (self.energies[ind] >= self.cbm) and (self.energies[ind] <= (self.cbm + depth)):
                cbmind.append(ind)
        #next get integrated total densities SIDE NOTE -> this is wrong because total densities gives different
        #       total values than site projected pDOS
        totval = [0.,0.] #first is vbm region, second is cbm region
        for ind in vbmind:
            totval[0] += self.cdos.get_densities(spin=None)[ind]
        for ind in cbmind:
            totval[1] += self.cdos.get_densities(spin=None)[ind]
        #now compile integrated elt-spd pdos
        siteorbvals = {}
        complist_vbm = []
        complist_cbm = []
        for elt in self.elt_pdos.keys():
            siteorbvals[elt] = {}
            for orb in self.elt_pdos[elt].keys():
                tmptotval = [0.,0.]
                for ind in vbmind:
                    tmptotval[0] += self.elt_pdos[elt][orb].get_densities(spin=None)[ind]
                for ind in cbmind:
                    tmptotval[1] += self.elt_pdos[elt][orb].get_densities(spin=None)[ind]
                percvals = [round(100*(tmptotval[0]/ totval[0]),3),
                            round(100.*(tmptotval[1]/ totval[1]),3)]
                siteorbvals[elt][orb] = {'totval':tmptotval, 'percval':percvals}
                complist_vbm.append([percvals[0],elt+'-'+orb])
                complist_cbm.append([percvals[1],elt+'-'+orb])
        complist_vbm.sort(reverse=True)
        complist_cbm.sort(reverse=True)
        print 'complist_vbm:',complist_vbm
        print 'complist_cbm:',complist_cbm
        tmptmp = 0.
        for j in complist_vbm:
            tmptmp += j[0]
        print 'sum of vbm perc is ',tmptmp,' of total DOS in this region'
        tmptmp = 0.
        for j in complist_cbm:
            tmptmp += j[0]
        print 'sum of cbm perc is ',tmptmp,' of total DOS in this region'

