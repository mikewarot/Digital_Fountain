import random;

def sampleset(x): # return 5 samples based on random seed x from 20 elements
	random.seed(x)
	return random.sample(xrange(20),5)
  
x = map(sampleset,range(20)) 
y = map(sorted,x)
z = sorted(y)

def expand(a): # expand a sample list into a boolean array of 20 elements
	def inside(q):
		return (q in a)
	
	return map(inside,range(20))

zz = map(expand,x)  # zz now has lists of true/false for each element\

xor = lambda arg1, arg2 : arg1 ^ arg2

