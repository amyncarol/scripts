#!/bin/bash

#PBS -l nodes=1:ppn=64
#PBS -l walltime=8:00:00
#PBS -j oe
#PBS -q default
cd $PBS_O_WORKDIR



inputfile=scf.in

echo "PBS_O_WORKDIR is : $PBS_O_WORKDIR"
echo "PBS JOB DIR is: $PBS_JOBDIR"
# Notice that the output of pwd will be in lustre scratch space
echo "PWD is : `pwd`"



#/opt/intel/composer_xe_2013.3.163/mkl run the executable
/opt/openmpi/bin/mpirun -np 64 pw.x -i $inputfile > output.$PBS_JOBID
