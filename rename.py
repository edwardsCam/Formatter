import os, re

def slash(path):
	if path.endswith("\\"): return path
	else: return path + "\\"

def unslash(path):
	if path.endswith("\\"): return path[:-1]
	else: return path

def strip(expr, s):
	return re.sub(expr, "", s)

def trim(s):
	temp = re.sub(r"^\s+", "", s)
	temp = re.sub(r"\s+$", "", temp)
	return temp

def format(s):
	s = strip(r"[\[\]\(\)\-_]", s)
	s = re.sub(r"\s{2,}", " ", s)
	s = trim(s)
	return s

def split(s):
	years = re.findall(r"\d{4}", s)
	if len(years) > 1:
		print "\n -- Unclear format on ", s, " --"
		print " -- Cannot decipher album name / year -- "
		album = ""
		while album == "":
			album = raw_input("Please enter the album name: ")
		year = raw_input("Please enter the year (leave blank if unknown): ")
		print
	elif len(years) > 0:
		year = years[0]
		album = format(re.sub(year, "", s))
	else:
		year = ""
		album = format(s)

	return [year, album]

def get_artist_name(path):
	disc = re.search(r"\W*discography", path, re.IGNORECASE)
	if disc:
		d = disc.group(0)
		idx = path.find(d)
		return path[:idx]
	else: return path

def bracket(s):
	if len(s) > 0: return "[" + s + "] "
	else: return s

def fprint(d):
	max_len = 0
	for k in d:
		if len(k) > max_len:
			max_len = len(k)
	for k in sorted(d):
		diff = 1 + max_len - len(k)
		print k, " "*diff, " ->  ", d[k]

def rename(root, move):
	artist = get_artist_name(root)
	os.rename(root, artist)
	root = slash(artist)
	idx = len(os.path.dirname(unslash(root)))
	output = {}
	try:
		for path, dirs, __ in os.walk(root):
			if not dirs:
				path = os.path.normpath(path)
				if move:
					dir_name = root
				else:
					dir_name = slash(os.path.dirname(path))
				base_name = format(os.path.basename(path))
				album = split(base_name)
				base_name = bracket(album[0]) + album[1]
				new = dir_name + base_name
				os.rename(path, new)
				output[path[idx:]] = new[idx:]

		fprint(output)
		print "\n -- Success! -- \n"

	except ValueError:
		print "\nError ", ValueError
		raw_input()

if raw_input("Are you sure you want to run this? [yn] ") == "y":
	dir = slash(raw_input("Directory: "))
	move = raw_input("Move all subfolders to the given root directory? [yn] ") == "y"
	print
	rename(dir, move)
	raw_input("\n -- Enter to exit -- \n")
