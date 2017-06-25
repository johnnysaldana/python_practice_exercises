# entropy.py

import string

def getsize(path):
	import os
	return os.path.getsize(path)
	

def charsplit(s):
	lst = []
	i = 0
	while i < len(s):
		lst += list(s[i])
		i += 1
	return lst

def file():
	with open("h.txt") as f:
		s = f.read()
	return s

def getdict():
	#print(s)
	d = {}
	charlist = charsplit(file())

	for char in charlist:
		if char in d:
			d[char] += 1
		else:
			d[char] = 1
	return d

def entropy():
	from math import log
	d = getdict()
	H = 0

	for key in d:
		prob = (d[key] / len(d))

		H += -1 * len(d) * (prob * ( log(prob) / log(2)) )
	return(H)

def main():
	print("Welcome to the Shannon entropy solver!!\n\n")
	print("The current file size is:", getsize("h.txt"), "bytes\n")
	print("The Shannon entropy of the file is:", round(entropy()), "bytes\n\n")
	entropy()

main()
