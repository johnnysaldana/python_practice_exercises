# random_rna

from random import uniform

def random_rna(n):
	rna = ""
	base = 0
	i = 0
	while i < n:
		base = int(uniform(1, 5))
		if base == 1:
			rna += "U"
		elif base == 2:
			rna += "A"
		elif base == 3:
			rna += "G"
		elif base == 4:
			rna += "C"
		else:
			rna += "E"
		i+=1
	return rna

def main():
	k = int(input("Enter a number to generate ranom rna: "))
	print(random_rna(k))

main()