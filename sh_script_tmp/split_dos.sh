#!/bin/sh
basefile="DOSCAR"
inputfile="DOSCAR_new"
rm -fr $inputfile
tmpfile="tmp"
numdos=1001
grep -A $numdos " 14.00000000     -4.00000000" $basefile>>$inputfile
rm -fr $tmpfile
grep -n " 14.00000000     -4.00000000" $inputfile>>$tmpfile;
enum=`cat $tmpfile | wc -l | awk '{printf "%12d", $1}'`
((num=$enum-0))
lastnum=0

for ((i=1; i<= $num ; i++))
do
	outfile="DOS_$i"
	rm -fr $outfile
	startalign=`head -$i $tmpfile |tail -1| awk '{printf "%12d", $1}'`
	((numalign=$numdos))
	((tailalign=$startalign+$numdos))
	head -$tailalign $inputfile |tail -$numalign>>$outfile

done

