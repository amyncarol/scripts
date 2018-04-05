for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
		cp ../KPOINTS .
	 	sed s@P000@$dir@g ../new.pbs>new.pbs
		qsub new.pbs
	 cd ..
   fi
done

