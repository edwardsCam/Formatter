import os, re, sys

def slash(path):
	return path + "\\"

def strip(expr, s):
	return re.sub(expr, "", s)

def trim(s):
	temp = re.sub(r"^\s+", "", s)
	temp = re.sub(r"\s+$", "", temp)
	return temp

def rename(path):
	try:
		for subdir, _, files in os.walk(path):
			if len(files) > 0:
				print subdir
				#print_files(files)
				for f in files:
					basename, fileExtension = os.path.splitext(f)
					print "1: " + f
					basename = strip(r"[\[\]\(\)\-_]", basename)
					basename = re.sub(r"\s{2,}", " ", basename)
					basename = trim(basename)
					f = basename + fileExtension
					print "2: " + f
					print
				years = re.findall(r"\d{4}", subdir)
				year = ""
				if len(years) > 0:
					year = years[0]

	except:
		print "Error"



root_dir = slash("C:\\Users\\Cam\\Documents\\rtest")

if raw_input("Do you want to run this? yn\n") == "y":
	rename(root_dir)
	raw_input(" -- Enter to exit -- ")
