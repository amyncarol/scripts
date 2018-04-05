for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
        if grep -q 'to POSCAR and continue' _JOB_OUTPUT.txt
        then 
	      cp CONTCAR POSCAR       
              sh ~/submit.sh $PWD 64 std
        fi
     cd ..
   fi
done

