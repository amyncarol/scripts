##python 2.7.9 pymatgen 4.5.0
from pymatgen import MPRester
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from pymatgen.phasediagram.analyzer import PDAnalyzer
from pymatgen.phasediagram.maker import PhaseDiagram
def get_pd(vasprun):
    """
    get the phase diagram object given vasprun

    returns:
    pda, entry of the vasprun.xml 
    """
    v = vasprun
    entry = v.get_computed_entry()

    compat = MaterialsProjectCompatibility()
    entry = compat.process_entry(entry)


    el = [specie.symbol for specie in entry.composition.keys()]
    with MPRester(api_key="64JmsIV32c8lUaxu") as mpr:
        entries = mpr.get_entries_in_chemsys(el)
    entries.append(entry)
    pd = PhaseDiagram(entries)
    return pd, entry

def get_e_above_hull(vasprun):
    """ 
    Get e_above_hull for the input vasprun
    """
    pd, entry = get_pd(vasprun)
    pda = PDAnalyzer(pd)
    (decomp, hull) = pda.get_decomp_and_e_above_hull(entry)
    new_decomp = [compound.composition.reduced_formula for compound in decomp]
    return (new_decomp, hull)

def get_formation_energy(vaspun):
    """
    get formation energy per atom given vasprun.xml
    """
    pd, entry = get_pd(vasprun)
    return pd.get_form_energy_per_atom(entry)

    

if __name__ == '__main__':
    v=Vasprun('vasprun.xml')
    print get_e_above_hull(v)

