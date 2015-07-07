import os, re, sys

def slash(path):
	return path + "\\"

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

def get_artist_name(path):
	disc = re.search(r"\W*discography", path, re.IGNORECASE)
	if disc:
		d = disc.group(0)
		idx = path.find(d)
		return path[:idx]
	else:
		return path

def add_brackets(s):
	return "[" + s[:4] + "]" + s[4:]

def rename(path):
	root_dir_len = len(path)
	try:
		for subdir, _, files in os.walk(path):
			if len(subdir) == root_dir_len:
				new = get_artist_name(subdir)
			else:

				#TODO only format end-level directories

				folder_name = subdir[root_dir_len:]
				folder_name = format(folder_name)
				folder_name = add_brackets(folder_name)
				new = path + folder_name
			os.rename(subdir, new)
			print "Renamed " + subdir + " to " + new
		print "Finished!!"
	except:
		print "Error"

if raw_input("Do you want to run this? yn\n") == "y":
	rename(slash(raw_input("Directory: ")))
	raw_input(" -- Enter to exit -- ")
