#!/bin/bash


benchmarks=(
    "Bubblesort"
    "IntMM"
    "Perm"
    "Queens"
    "RealMM"
    "Treesort"
    "FloatMM"
    "Oscar"
    "Puzzle"
    "Quicksort"
    "Towers"
)

core_types=(
    # "c_8_192_256"
    # "s_8_192_256"
    # "c_8_192_48"
    # "s_8_192_48"
    # "c_2_192_256"
    # "s_2_192_256"
    # "s_8_16_256"
    # "c_8_16_256"
)

for b in "${benchmarks[@]}"
do
    for c in "${core_types[@]}"
    do

        now=$(date +%s)
        ../gem5/build/RISCV/gem5.opt --outdir=m5out/${now}_${b}_${c} run.py $b $c &
    done
done
