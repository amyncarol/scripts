#!/home/yaocai/app/bin/python
##python2.7.9 pymatgen 4.5
import os

with open('Dos_result', 'w') as f:
	for folder in os.listdir('.'):
		if os.path.isdir(folder):
			f.write(folder)
			f.write('\n')
