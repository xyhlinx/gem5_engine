import os
import re
import glob
import csv
from datetime import datetime


filename = 'stats.txt'
path = './m5out/1644310610*/'
sim_word = 'simSeconds'
d = {}
workload_list = [
        "Bubblesort",
        "IntMM",
        "Perm",
        "Queens",
        "RealMM",
        "Treesort",
        "FloatMM",
        "Oscar",
        "Puzzle",
        "Quicksort",
        "Towers",
]


for file in glob.glob(path + filename):
    with open(file, 'r') as f:
        for line in f.readlines():
            if sim_word in line:
                d_name = file.split('/')[2]
                workload = ''.join(d_name.split('_')[1])
                d_name = '_'.join(d_name.split('_')[2:])
                if not d_name in d:
                    d[d_name] = {}
                d[d_name][workload] = line.split()[1]


with open('ggg.csv', 'w') as csvfile:
    fields_name = ['core'] + workload_list 
    writer = csv.writer(csvfile)
    writer.writerow(fields_name)
    for k, v in d.items():
        wl = []
        for i in range(len(workload_list)):
            if workload_list[i] in v:
                wl.append(v[workload_list[i]])
                continue
            wl.append(0)
        writer.writerow([k] + wl)
