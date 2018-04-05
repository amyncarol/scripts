#!/bin/bash
ppn=$1
executable=$2
input=$3
output=$4
cat > PBSqe.sh << EOF
#!/bin/bash

#PBS -l nodes=1:ppn=$ppn
#PBS -l walltime=8:00:00
#PBS -j oe
#PBS -q default
cd `pwd`

echo "PBS_O_WORKDIR is : $PBS_O_WORKDIR"
echo "PBS JOB DIR is: $PBS_JOBDIR"
echo "PWD is : `pwd`"

# run the executable
mpirun $executable -i $input > $output
EOF

qsub PBSqe.sh
