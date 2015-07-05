import os, re, sys

def slash(path):
	return path + "\\"

root_dir = slash("C:\Users\Cam\Downloads\Tycho - Discography (2002-2014) [FLAC]")
root_dir_len = len(root_dir)

def strip(expr, s):
	return re.sub(expr, "", s)

def trim(s):
	temp = re.sub(r"^\s+", "", s)
	temp = re.sub(r"\s+$", "", temp)
	return temp

def get_year(s):
	years = re.findall(r"\d{4}", s)
	return years[0] if len(years) > 0 else ""

def format(s):
	s = strip(r"[\[\]\(\)\-_]", s)
	s = re.sub(r"\s{2,}", " ", s)
	s = trim(s)
	return s

def add_brackets(s):
	return "[" + s[:4] + "]" + s[4:]

def rename(path):
	try:
		for subdir, _, files in os.walk(path):
			if len(subdir) != root_dir_len:
				folder_name = subdir[root_dir_len:]
				folder_name = format(folder_name)
				folder_name = add_brackets(folder_name)
				os.rename(subdir, root_dir + folder_name)
				
			"""
			for f in files:
				basename, fileExtension = os.path.splitext(f)
				print "1: " + f
				f = format(basename) + fileExtension
				print "2: " + f
				print get_year(basename)
				print
				"""

	except:
		print "Error"

if raw_input("Do you want to run this? yn\n") == "y":
	rename(root_dir)
	raw_input(" -- Enter to exit -- ")
