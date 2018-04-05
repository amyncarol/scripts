for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
         if [ -s CHGCAR.relax ]
	 then 
             mv CHGCAR.relax CHGCAR
	 fi
     cd ..
   fi
done

