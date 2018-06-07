from pymatgen.io.vasp.inputs import Poscar

structure = Poscar.from_file('POSCAR').structure
structure.make_supercell(2)  #2*2*2

poscar = Poscar(structure)
poscar.write_file('POSCAR_new')

