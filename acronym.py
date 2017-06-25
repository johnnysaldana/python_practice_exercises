# acronym.py

def acronym(s):
	l = s.split()
	print(l)
	acr = ""
	for i in range(len(l)):
		w = l[i]
		acr = acr + w[0].upper()
		i += 1

	return acr

def main():
	k = input("Enter a word to make into an acronym: ")
	print(acronym(k))

main()

	