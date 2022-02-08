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
    2_16_48_simple
    8_16_48_simple
    2_192_48_simple
    2_16_256_simple
    2_16_48_complex
    8_192_48_simple
    8_16_256_simple
    8_16_48_complex
    2_192_256_simple
    2_192_48_complex
    2_16_256_complex
    8_192_256_simple
    8_192_48_complex
    8_16_256_complex
    2_192_256_complex
    8_192_256_complex
)

for b in "${benchmarks[@]}"
do
    for c in "${core_types[@]}"
    do

        now=$(date +%s)
        ../gem5/build/RISCV/gem5.opt --outdir=m5out/${now}_${b}_${c} run.py $b $c &
    done
done
