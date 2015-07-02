import os, re, sys

def slash(path):
	return path + "\\"

def print_files(files):
	for f in files:
		print "  " + f
	print " "

def regex_strip(expr, s):
	return re.sub(expr, "", s)

def regex_trim(s):
	temp = re.sub(r"^\s+", "", s)
	temp = re.sub(r"\s+$", "", temp)
	return temp

root_dir = slash("C:\\Users\\Cam\\Documents\\rtest")

def rename(path):
	try:
		for subdir, _, files in os.walk(path):
			if len(files) > 0:
				print subdir
				#print_files(files)
				for f in files:
					basename, fileExtension = os.path.splitext(f)
					print "1: " + f
					basename = regex_strip(r"[\[\]\(\)\-_]", basename)
					basename = re.sub(r"\s{2,}", " ", basename)
					basename = regex_trim(basename)
					f = basename + fileExtension
					print "2: " + f
					print
				years = re.findall(r"\d{4}", subdir)
				year = ""
				if len(years) > 0:
					year = years[0]
	except:
		print "Error"


if raw_input("Do you want to run this? yn\n") == "y":
	rename(root_dir)

raw_input(" -- Enter to exit -- ")