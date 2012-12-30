import random;

def sampleset(x): # return 5 samples based on random seed x from 1000 elements
	random.seed(x)
	return random.sample(xrange(20),5)
  
x = map(sampleset,range(20)) 
y = map(sorted,x)
z = sorted(y)

