"""Zip all folders in a given directory."""

import os
import shutil

##
##

FILE_DIR = "/Users/SP/Documents/05-COGS108/PastIterations/Wi18/temp/"
OUT_DIR = "/Users/SP/Documents/05-COGS108/PastIterations/Wi18/ProjectRepos/"

##
##

def main():
	"""   """

	folders = os.listdir(FILE_DIR)

	for folder in folders:

		if folder[0] is '.': continue

		shutil.make_archive(os.path.join(OUT_DIR, folder), 'zip', os.path.join(FILE_DIR, folder))

if __name__ == '__main__':
	main()
