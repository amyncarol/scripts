for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
	 	cp ../custodian_job.py ./.
		cp ../submit.pbs ./.
		qsub submit.pbs
	 cd ..
   fi
done

