# guesser.py


def guesser(a, rangeMax, rangeMin, guess, hint):
	while guess != a:
		print(rangeMax)
		print(rangeMin)
		print("Is the number ", (guess) )

		hint = input("greater, less, or equal: ")

		if hint == "greater":
			rangeMin = guess 
			guess = (rangeMax + rangeMin) // 2

		elif hint == "less":
			rangeMax = guess 
			guess = (rangeMax + rangeMin) // 2

		else:
			print("There seems to be a problem :(")

	print("Get Rekt, I know what it is:", guess)

def main():
	rangeMax = int(input("Enter a max range: "))
	rangeMin = int(input("Enter a min range: "))
	a = int(input("Enter a number for me to guess: "))
	guess = (rangeMax + rangeMin) // 2
	hint = ""
	
	guesser(a, rangeMax, rangeMin, guess, hint)

	replay = input("Do you want to play again?")

	if replay == "yes":
		main()

	elif replay == "no":
		print("bye")

	else:
		print("There seems to be a problem with the response")

main()

input("press enter to continue")


