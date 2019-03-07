# find the sum of elements using lists
l=[1,2,3,9,4,1]
def func(l):
	s=0
	for i in l:
		s=s+i
	return s
s=func(l)
print(s)