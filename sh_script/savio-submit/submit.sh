#!/bin/bash
#SBATCH -J vjob
#SBATCH -o vjob.o%j
#SBATCH -e vjob.e%j
#SBATCH --partition=savio2

#SBATCH --nodes=2
#SBATCH --ntasks-per-node=24
#SBATCH --export=ALL
#SBATCH -t 00:30:00

#SBATCH --account=fc_mdasta

#SBATCH --mail-user=caiyao214@gmail.com
#SBATCH --mail-type=END
#SBATCH --exclusive

module unload openmpi/1.6.5-intel
module load intel/2013_sp1.4.211
module load mkl/2013_sp1.4.211
export PATH=/global/home/users/yaocai/intel_ib/bin:$PATH
export LD_LIBRARY_PATH=/global/home/users/yaocai/intel_ib/lib:$LD_LIBRARY_PATH

#Use ibrun to run the MPI job. It will detect the MPI, generate the hostfile
# and doing the right binding. With no options ibrun will use all cores.
export OMP_NUM_THREADS=1
export MV2_USE_ZCOPY_REDUCE=0
export MV2_USE_SLOT_SHMEM_COLL=0
export MV2_USE_ZCOPY_REDUCE=0

echo "Job started at `date`"
#mpirun /global/home/users/yaocai/bin/vasp_std >vasp.out
srun --mpi=pmi2 /global/home/users/yaocai/bin/vasp_std >vasp.out
echo "Job ended at `date`"
