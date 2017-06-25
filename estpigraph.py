# estpigraph

from random import uniform

from math import sqrt

from turtle import *
def drawline(x0, y0, x1, y1):
	penup()
	setposition(x0, y0)
	pendown()
	setposition(x1, y1)
	penup()

def drawsemicircle():
	pen(up)
	setposition(-500, 0)
	pen(down)
	for i in range(500):
		goto((-500 + i), (sqrt(-1 *((i-500) ** 2) + 250000)) )
		stamp()
		i += 1
	for i in range(500):
		setposition((i), (sqrt(-1 *((i) ** 2) + 250000)) )
		stamp()
		i += 1
	pen(up)


def drawestpi():
	hits = 0

	for i in range(100):
		x = uniform(-500, 500)
		y = uniform( -500, 500)
		goto(x, y)
		if y <= (sqrt(-x ** 2 + 250000)):
			hits += 1
		stamp()

	estimate = (hits / 1000) * 4 

	return estimate

def main():
	setworldcoordinates(-500, -500, 500, 500)
	drawline(-500, 0, 500, 0)
	drawline(0, 500, 0, -500)
	drawsemicircle()
	drawestpi()
	print("Welcome to the Monte Carlo Simulation for Estimating Pi!")
	exitonclick()

main()