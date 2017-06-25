# randints.py

from random import uniform

def randints(n, a, b):
	mylist = []

	while len(mylist) < n:

		new = uniform(a, b)
		while i < len(mylist):
			if new == mylist[i]:
				return
			else:
				i += 1

		mylist = mylist.append(uniform(a, b))

def main():
	n = int(input("Enter n: "))
	a = int(input("Enter a: "))
	b = int(input("Enter b: "))
	print(randints(n, a, b))

main()




