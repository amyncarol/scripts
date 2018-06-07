from pymatgen.io.vasp.inputs import Poscar

structure = Poscar.from_file('POSCAR').structure
structure.apply_strain(0.014)  #1.4% positive

poscar = Poscar(structure)
poscar.write_file('POSCAR_new')

