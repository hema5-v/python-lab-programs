#find the largest value using functions and return func
a=int(input("enter second num"))
b=int(input("enter second num"))
c=int(input("enter third num"))
print(a,b,c)

def func1(a,b,c):
	if a>=b and a>=c:
		return a
	elif b>=a and b>=c:
		return b
	elif c>=a and c>=b:
		return c
l=func1(a,b,c)
print(l)			