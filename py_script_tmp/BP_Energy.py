from pymatgen.io.vaspio.vasp_output import Vasprun
import numpy as np
import os
import glob

def BZ_avg(eigenvalues, band_index,kpoints,kpoints_weights):
    """
    :param eigenvalues: eigenvalues of all bands with the format of Vasprun.eigenvalues
    :param band_index: the band index for averaging
    :param kpoints: sampled k-points
    :param kpoints_weights: the weights of sampled k-points
    :return: the average of a particular band over k-points in the BZ
    """
    energy_array = [ eigenvalues[(1,k_point_index)][band_index][0] for k_point_index in range(len(kpoints))]
    return np.average(energy_array, weights=kpoints_weights)


def Branch_point_energy(vr, cb_sampling_num, vb_sampling_num):
    """
    Calculate the Branch_point_energy with the formula proposed in:
    APPLIED PHYSICS LETTERS 94, 012104 2009 ; doi: 10.1063/1.3059569

    :param vr: Vasprun Object
    :param cb_sampling_num: the number of cb for sampling. Default vb_sampling_num = 2* cb_sampling_num
    :return:
    """
    #vb_sampling_num = 2*cb_sampling_num
    vbm_band_index = len(filter(lambda u:u[1]!=0, vr.eigenvalues[(1,0)]))-1

    vb_sampling_indexes = [vbm_band_index-i for i in range(vb_sampling_num)]
    cb_sampling_indexes = [vbm_band_index+i+1 for i in range(cb_sampling_num)]
    
    vb_avg = sum([BZ_avg(vr.eigenvalues,vb_index,vr.actual_kpoints,vr.actual_kpoints_weights)
               for vb_index in vb_sampling_indexes])/len(vb_sampling_indexes)
    cb_avg = sum([BZ_avg(vr.eigenvalues,cb_index,vr.actual_kpoints,vr.actual_kpoints_weights)
               for cb_index in cb_sampling_indexes])/len(cb_sampling_indexes)
    
    return np.mean([vb_avg,cb_avg])


if __name__ == "__main__":
    results = open('results_2','w')	
    fail = open('fail.log','w')
    for mpid in os.listdir('.'):
        if not os.path.isfile(mpid):
            try:
                vr = Vasprun(os.path.join(mpid,'vasprun.xml'))
                vbm = vr.eigenvalue_band_properties[2]
                cbm = vr.eigenvalue_band_properties[1]
                ebp = Branch_point_energy(vr,cb_sampling_num=1, vb_sampling_num=2)
                bandgap = vr.eigenvalue_band_properties[0]
                ebp_position = (ebp-vbm)/bandgap
	        
                print >>results, "%s %4.2f %4.2f %4.2f %4.2f %4.2f" %(mpid, vbm, cbm, bandgap, ebp, ebp_position)
            except:
                print >>fail , mpid


