for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
	rm WAVECAR
        rm CHGCAR
        mv INCAR INCAR_3
        sed 's@ALGO = N@ALGO = V@g' < INCAR_3 > INCAR
	sh ~/submit.sh $PWD 4 c &
        wait
     cd ..
   fi
done

