for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
        if [ ! -s "CONTCAR" ]
        then 
              sh ~/submit.sh $PWD 4 std
        fi
     cd ..
   fi
done

