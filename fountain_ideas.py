import random;

K = 10

def sampleset(x): # return 5 samples based on random seed x from K elements
	random.seed(x)
	return random.sample(xrange(K),5)
  
x = map(sampleset,range(K)) 
y = map(sorted,x)
z = sorted(y)

def expand(a): # expand a sample list into a boolean array of K elements
	def inside(q):
		return (q in a)
	
	return map(inside,range(K))

zz = map(expand,x)  # zz now has lists of true/false for each element

xor = lambda arg1, arg2 : arg1 ^ arg2

# listdiff = lambda arg1, arg2 : list(set(arg1)^set(arg2))
listdiff = lambda arg1, arg2 : sorted(list(set(arg1)^set(arg2)))

bracketn = lambda arg1 : [ arg1 ] # useful for generating lists of lists

source = map(bracketn,xrange(K)) # [[0], [1], [2]...

def swap2(a,b) : # used to swap rows in the Y table, to get a leading value
        source[a],source[b] = source[b],source[a]
        y[a],y[b] = y[b],y[a]
        
def reduce2(a,b) : # used to factor out row b from row a
	source[a] = listdiff(source[a],source[b])
	y[a] = listdiff(y[a],y[b])



