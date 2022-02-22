for (( b=0; b<=4; b++ ))
do
	for (( c=1; c<=3; c++ ))
    	do

        	now=$(date +%s)
        	../gem5/build/RISCV/gem5.opt --outdir=m5out/${now}_${b}_${c} run.py $b $c &
    	done
done

