#!/bin/bash

#PBS -l nodes=1:ppn=64
#PBS -l walltime=8:00:00
#PBS -j oe
#PBS -q default
cd $PBS_O_WORKDIR

for (( id=0 ; id<64 ; id++ ))
do
  mcsqs -n=40 -ip=$id &
done
wait
