# interesttable.py

principle = float(input("Enter starting amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time: "))

def compound(p, r, t):
	p * (1.0 + r) ** t

def main():
	for i in range(int(time)):
		print(compound(principle, rate, i))
		i += 1

print(compound(principle, rate, time))
