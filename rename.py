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
	if len(years) > 0:
		return years[0]
	else:
		return ""

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

def rename(root, move):
	try:
		for name, dirs, __ in os.walk(root):
			if not dirs:
				name = os.path.normpath(name)
				dir_name = slash(os.path.dirname(name))
				base_name = format(os.path.basename(name))
				if get_year(base_name) != "":
					base_name = add_brackets(base_name)
				if move:
					new = root + base_name
				else:
					new = dir_name + base_name
				os.rename(name, new)
				print name + " -> " + new

		os.rename(root, get_artist_name(root))
		print "\nFinished!!\n"
	except ValueError:
		print "\nError ", ValueError
		raw_input()

if raw_input("Do you want to run this? [yn] ") == "y":
	dir = slash(raw_input("Directory: "))
	move = raw_input("Move all folders to root? [yn] ") == "y"
	rename(dir, move)
	raw_input("\n -- Enter to exit -- \n")
