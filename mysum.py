# mysum.py

def mysum(items):
	accum = 0
	for i in len(items):
		accum += items.pop(1)

	return sum

def main():
	items = list(input("Enter a list: "))
	print(mysum(items))

main()
