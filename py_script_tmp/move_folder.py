#!/home/yaocai/app/bin/python
##python2.7.9 pymatgen 4.5
import pandas as pd
import os
import shutil
b = pd.read_csv('remain_eff', names = ['ID', 'Compound'])
compounds = b['Compound'].values.tolist()

os.makedirs('new')
for j in compounds:
	shutil.move(j, 'new/')
	