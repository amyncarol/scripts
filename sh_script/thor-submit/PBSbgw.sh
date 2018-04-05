#!/bin/bash

#PBS -l nodes=1:ppn=64
#PBS -j oe
#PBS -q default
cd $PBS_O_WORKDIR

echo "PBS_O_WORKDIR is : $PBS_O_WORKDIR"
echo "PBS JOB DIR is: $PBS_JOBDIR"
# Notice that the output of pwd will be in lustre scratch space
echo "PWD is : `pwd`"

BGW_BIN="/home/yaocai/bin/BerkeleyGW/fftw3_mkl/real"
#BGW_BIN="/home/yaocai/bin/BerkeleyGW/fftw3_official/real"
EPSILON="$BGW_BIN/epsilon.real.x"
SIGMA="$BGW_BIN/sigma.real.x"
KERNEL="$BGW_BIN/kernel.real.x"
ABSORPTION="$BGW_BIN/absorption.real.x"
INTEQP="$BGW_BIN/inteqp.real.x"
MPIRUN="mpirun -np 64"
export OMP_NUM_THREADS=1

$MPIRUN $EPSILON &> ./epsilon.out
