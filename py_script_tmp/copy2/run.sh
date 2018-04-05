for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
	sh ~/submit.sh $PWD 4 c
     cd ..
   fi
done

