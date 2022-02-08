import os
import re
import glob
import csv
from datetime import datetime


filename = 'stats.txt'
path = './m5out/1644295714*/'
sim_word = 'simSeconds'
d = {}

for file in glob.glob(path + filename):
	with open(file, 'r') as f:
		for line in f.readlines():
			if sim_word in line:
				d_name = file.split('/')[2]
				d_name = '_'.join(d_name.split('_')[2:])
				d[d_name] = line.split()[1]


with open('ggg.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	for k, v in d.items():
		writer.writerow([k, v])
