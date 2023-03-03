from math import tan,pi
n=int(input('numbers of sides:'))
l=float(input('the length of a side:'))
area=n*(l**2)/(4*tan(pi/n))
print(round(area))