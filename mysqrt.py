# mysqrt.py

def mysqrt(n):
	guess = n // 2
	i = 1
	while i < 30:
		guess = (guess +  (n / guess)) / 2
		i += 1

	return guess
	print(guess)

def main():
	print("Welcome to the Square Root Approximator!")
	number = float(input("Enter a number: "))
	print("The square root of", number, " is", mysqrt(number))
	main()

main()
input("Press enter to continue..");