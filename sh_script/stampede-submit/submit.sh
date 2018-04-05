#!/bin/bash

#SBATCH -J myjob           
#SBATCH -o myjob.o%j      
#SBATCH -e myjob.e%j     
#SBATCH -p normal        
#SBATCH -N 4               
#SBATCH --ntasks-per-node 68              
#SBATCH -t 12:00:00        
###SBATCH -A myproject       

ibrun /home1/05018/tg843171/vasp.5.4.4_vtst/bin/vasp_ncl         

