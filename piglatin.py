# piglatin.py

def firstvowelindex(word):
	i = 0
	while word[i] not in "aeiou":
		i += 1
	return i

def piglatin(word):
	i = firstvowelindex(word)
	if i == 0:
		return word + "yay"
	return word[i:] + word[:i] + "ay"

def main():
	w = input("enter a word:  ")
	print("In Pig Latin, that is", piglatin(w))


main()