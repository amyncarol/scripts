for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
	 	cp ../custodian_job.py ./.
		cp ../submit_custodian.pbs ./.
		qsub submit_custodian.pbs
	 cd ..
   fi
done

