import math as m
scale = input("Enter the scale factor: ")
scaleF = float(scale)
print("begin: ")
while True:
	x	= input("Score: ")
	xFloat	= float(x)
	print(m.ceil(2*xFloat*scaleF)/2)
