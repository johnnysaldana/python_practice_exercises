# dec_to_bin.py

from math import log

def convert(decimal):
	binary = ""
	i = 0
	number = decimal
	power = int(log(decimal) / log(2))

	while power >= 0:
		if number - (2**power) >= 0:
			binary += "1"
		else:
			binary += "0"
		number = number - int(log(decimal) / log(2))
		power -= 1

	return binary

def main():
	k = int(input ("Enter A Decimal to be converted to binary: "))

	print(convert(k))

main()



	



# 1 --> 1

# 4 --> 100

# 10 --> 1010

# 19388 --> 100101110111100