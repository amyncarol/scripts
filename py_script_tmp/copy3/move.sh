#!/bin/bash

for dir in `ls .`
 do
   if [ -d $dir ]
   then
     cd $dir
	 if [ -a OUTCAR ]
         then
	    if grep -q 'User time (sec):' OUTCAR
            then
	       cd ..
	       mv $dir ../complete/.
            else
               cd ..
            fi
	 else 
	    cd ..
	 fi
   fi
done

