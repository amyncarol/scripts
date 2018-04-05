#!/bin/bash
#  1 job directory
#  2 number of nodes
#  3 exe version
sed "s:zebra:$1:g" ~/PBSvasp.template.sh > ~/PBSvasp.sh
x=`echo ${1#*/*/*/*/}`
sed "s:giraffe:$x:g" ~/PBSvasp.sh > ~/PBSvasp.temp.sh
mv ~/PBSvasp.temp.sh ~/PBSvasp.sh


if [ "$3" == "std" ]
then
sed "s/sloth/vasp_std/g" ~/PBSvasp.sh > ~/PBSvasp.temp.sh
else
if [ "$3" == "gam" ]
then
sed "s/sloth/vasp_gam/g" ~/PBSvasp.sh > ~/PBSvasp.temp.sh
else
if [ "$3" == "ncl" ]
then
sed "s/sloth/vasp_ncl/g" ~/PBSvasp.sh > ~/PBSvasp.temp.sh
else
printf "which binary"
fi
fi
fi


sed "s/nodes=1:ppn=8/nodes=1:ppn=${2}/g" ~/PBSvasp.temp.sh >~/PBSvasp.sh


rm ~/PBSvasp.temp.sh
qsub ~/PBSvasp.sh
