from pymatgen.io.vaspio import Vasprun
from pymatgen import MPRester
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.phasediagram.pdmaker import PhaseDiagram
from pymatgen.phasediagram.pdanalyzer import PDAnalyzer

def get_e_above_hull(vasprun):
    """ 
    Get e_above_hull for the input vasprun
    """
    v = vasprun
    entry = v.get_computed_entry()

    compat = MaterialsProjectCompatibility()
    entry = compat.process_entry(entry)


    el = [specie.symbol for specie in entry.composition.keys()]
    mpr = MPRester(api_key="64JmsIV32c8lUaxu")
    mp_entries = mpr.get_entries_in_chemsys(el)
    pd = PhaseDiagram(mp_entries)
    a = PDAnalyzer(pd)
    return a.get_e_above_hull(entry)

if __name__ == '__main__':
    v=Vasprun('vasprun.xml')
    print get_e_above_hull(v)

