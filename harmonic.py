# harmonic.py

def harmonic(n):
	total = 0
	for k in range(1, n + 1):
		total += 1/k
	return total

def main():
	n = int(input("Enter a posiive integer: "))
	print("The sum of 1/k for k = 1 to ", n, " is", harmonic(n))

main()
input("Press enter to continue..");