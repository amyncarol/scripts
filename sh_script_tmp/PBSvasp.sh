#!/bin/bash
### Number of nodes - 2 nodes using 12 cores per node
#PBS -l nodes=4:ppn=8:node
### Example: to request 2 VPs on each of 3 nodes and 1 VPs on 2 more nodes
## #PBS -l nodes=10:ppn=4+2:ppn=1
### Output files. If not specified PBS uses the job name and ID.
###PBS -o /home/yaocai/Ab/216/tetra-relax/Cs2Se1Cl6/o.$PBS_JOBID
###PBS -e /home/yaocai/Ab/216/tetra-relax/Cs2Se1Cl6/e.$PBS_JOBID
### Merge stderr with stdout
#PBS -j oe
### Mail to user
#PBS -m eb
### Queue name
#PBS -q default
### Job name
#PBS -N 216/tetra-relax/Cs2Se1Cl6
### Job Accounting Name
#PBS -A Testing
### Declare job-non-rerunable
#PBS -r n

export MKL_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_DYNAMIC=FALSE

PBS_PWD="$(pwd)"
cd "${PBS_O_WORKDIR}"
THIS_HOST="$(hostname)"

###MPI_ARCH="x86_64"
###MPI_BUILD="ib-intel11"
###MPI_ROOT="/opt/open-mpi/${MPI_BUILD}"
OPENMPIRUN_BIN="/opt/open-mpi/ib-intel11/bin/mpirun"
NPROCS="$(wc -l < ${PBS_NODEFILE} | tr -d '[:blank:]')"
MYJOBHOME="/home/yaocai/Ab/216/tetra-relax/Cs2Se1Cl6"
MYMPIPROG="$HOME/bin/vasp.5.4.1_july8"



cd ${MYJOBHOME}



hr()
{
	perl -e 'print "\n" . "-"x70 . "\n\n"';
}

print_job_info()
{
	hr;
	printf "Torque Job ID: %s\n" "${PBS_JOBID}";
	printf "\nRunning on host %s @ %s\n" "${THIS_HOST}" "$(date)";
	printf "\nStarting directory was %s\n" "${PBS_PWD}";
	printf "Working directory is %s\n" "${PBS_O_WORKDIR}";
	printf "The PWD is %s\n" "`pwd`";
	printf "\nThis job runs on the following processors:\n\n\t";
	printf "%s " $(cat ${PBS_NODEFILE} | sort);
	printf "\n\n";
	printf "This job has allocated %s nodes/processors.\n" "${NPROCS}";
	hr;
}

run_mpirun()
{
    OPENMPI_CMD="${OPENMPIRUN_BIN} -np ${NPROCS} ${MYMPIPROG}";
	printf "%s\n\n" "${OPENMPI_CMD}";
	time ${OPENMPI_CMD};
}

main()
{
	print_job_info;
	run_mpirun | tee _JOB_OUTPUT.txt;
	hr;
}

time main 2>info;
echo ${PBS_O_WORKDIR} >> info;
mv info finish;
