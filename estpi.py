# estpi.py

from random import uniform

from math import sqrt
def estpi(n):
	hits = 0
	for i in range(n):
		x = uniform(-10, 10)
		y = uniform( 0, 10)
		if y <= (sqrt(-x ** 2 + 100)):
			hits += 1
	estimate = (hits / n) * 4 
	return estimate

def main():
	print("Welcome to the Monte Carlo Simulation for Estimating Pi!")
	darts = int(input("Enter number of darts to throw: "))
	print(estpi(darts))

main()
input("Press enter to continue..");
main()