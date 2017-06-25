# removepunc.py

from string import punctuation

def removepunc(s):
	i = 0
	while i < len(punctuation):
		s = s.replace(punctuation[i], "")
		i += 1
	return s

def main():
	k = input("Enter a string to remove punctuation: ")
	print(removepunc(k))

main()