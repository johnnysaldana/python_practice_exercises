# printfile.py

def printfile(fname):
	with open(fname) as f:
		print(f.read().split())

def main():
	printfile("inp.cwl")

main()
