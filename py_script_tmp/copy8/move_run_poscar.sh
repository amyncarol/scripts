for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
        if grep -q 'to POSCAR and continue' _JOB_OUTPUT.txt
        then 
	      cd ..
	      mv $dir poscar_run/.
	else
	      cd ..       
        fi
   fi
done

