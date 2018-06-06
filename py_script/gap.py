#!/home/yaocai/app/bin/python2
#python2.7.9 pymatgen4.5
from pymatgen.io.vasp.outputs import Vasprun
vr = Vasprun("vasprun.xml")
print(vr.eigenvalue_band_properties)
efermi = vr.efermi
vbm = vr.eigenvalue_band_properties[2]

eig = [vr.eigenvalues[i] for i in vr.eigenvalues]
occu = [i.tolist() for i in eig]
occu_flat = [i[1] for sublist in occu for subsublist in sublist for i in subsublist]
occu_set = set(occu_flat)

if efermi < vbm:
    print("Metal: efermi<vbm efermi=", efermi, "vbm=", vbm)

if len(occu_set) > 2:
  print("Metal: fractional occupation:", occu_set)

bs = vr.get_band_structure()
print('Eg from band structure: {}'.format(bs.get_band_gap()['energy']))
print('transition: {}'.format(bs.get_band_gap()['transition']))
print('Direct Eg from band structure: {}'.format(bs.get_direct_band_gap()))