#!/bin/bash

for dir in `ls .`
do
   if [ -d $dir ]
   then
     cd $dir
	 if [ -a OUTCAR ]
         then
	       cd ..
	       mv $dir calculating/.
         else
               cd ..
         fi
    fi
done

