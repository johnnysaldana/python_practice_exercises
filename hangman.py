# hangman.py


def words():
	with open("hangman.txt", encoding="ISO-8859-1") as f:
		l = f.read().split()
	return l

def hideword(actual, guesses):
	display = ""
	lst = guesses
	print(lst)
	if lst == []:
		i = 0
		while i < len(actual):
			display += "_ " 
			i += 1
		print(display)
		print("case 1")
		return display
	else:
		i = 0
		display = actual
		print(display)
		print("case 2")
		while i < len(actual):
			if i == 0 and display[i].islower:
				print("1")
				display = display.replace(display[i], "_ ")
				print(display)
				i += 2

			elif display[i].islower:
				print("1")
				display = display.replace(display[i], "_ ")
				print(display)
				i += 2

			else:
				print("2")
				i += 1
				print(display)
		print("P")
		print(display)
		return display




def hangman():
	from random import uniform
	guesses = []
	print(guesses)
	q = int(uniform(0, len(words() )))
	word = words().pop(q).lower()
	print(word)
	won = 0
	wordtoshow = hideword(word, guesses)
	print(wordtoshow)
	while len(guesses) <= 6 :
		wordtoshow = hideword(word, guesses)
		print(wordtoshow)
		print("So far you have guessed: ", guesses)
		if won == 0:
			print("Keep going")
		elif won == 1:
			print("You won!")
			main()

		else:
			print("You lose!")
			main()
		choice = input("Enter a letter or type 'guess' to attempt to solve: ").upper()
		if choice == "guess":
			w = input("Enter the word you think I picked: ")
			if w == word:
				won == 1
			else:
				won == 2
		else:
			guesses.append(choice)

	print("You lose!")
	main()



def main():
	print("Welcome to hangman\nPress any key to start!")
	input("")
	hangman()

main()
