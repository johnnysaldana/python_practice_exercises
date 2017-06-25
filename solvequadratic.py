# solvequadratic

from cmath import *

def mysqrt(x):
	x ** (0.5) 

def solvequadratic(a, b, c):
	print("Solving:  ", a, "x^2 + ", b, "x + ", c)

	if (b ** 2.0 - (4.0 * a * c)) < 0:
		sol1 = sqrt(b ** 2.0 - (4.0 * a * c))
		sol2 = sqrt(b ** 2.0 - (4.0 * a * c))

	else:
		sol1 = (-1.0 * b + mysqrt(b ** 2.0 - (4.0 * a * c))) // 2.0 * a
		sol2 = (-1.0 * b - mysqrt(b ** 2.0 - (4.0 * a * c))) // 2.0 * a

	print("The solutions are", sol1, " and ", sol2)

def main():
	a = float(input("Enter a: "))
	b = float(input("Enter b: "))
	c = float(input("Enter c: "))

	solvequadratic(a, b, c)

main()