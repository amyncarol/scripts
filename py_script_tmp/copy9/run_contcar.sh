for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
        if [ -s "CONTCAR" ]
        then 
	      cp CONTCAR POSCAR       
              sh ~/submit.sh $PWD 4 std
        fi
     cd ..
   fi
done

