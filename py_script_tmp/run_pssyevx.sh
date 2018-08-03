for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
        if grep -q 'ERROR in subspace rotation PSSYEVX' _JOB_OUTPUT.txt
        then 
                     rm WAVECAR
	             rm CHGCAR
                     mv INCAR INCAR_3
                     sed 's@ALGO = F@ALGO = N@g' < INCAR_3 > INCAR
                     rm INCAR_3     
	             sh ~/submit.sh $PWD 4 std
        fi
     cd ..
   fi
done

