for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
        if grep -q 'ERROR FEXCF' _JOB_OUTPUT.txt
        then 
                     rm WAVECAR
	             rm CHGCAR
                     cp ../INCAR_SMASS ./INCAR    
	             sh ~/submit.sh $PWD 4 std
        fi
     cd ..
   fi
done

