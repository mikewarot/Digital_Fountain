import random;

K = 500    # how many blocks makes the whole set
M = 7      # how many blocks do we Mix to get an output block? (should be ODD)
Extras = 5 # how many extra samples?

def sampleset(x): # return M samples based on random seed x from K elements
	random.seed(x)
	return random.sample(xrange(K),M)
  
x = map(sampleset,range(K+Extras)) 
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

source = map(bracketn,xrange(K+Extras)) # [[0], [1], [2]...

def swap2(a,b) : # used to swap rows in the Y table, to get a leading value
        source[a],source[b] = source[b],source[a]
        y[a],y[b] = y[b],y[a]
        
def reduce2(a,b) : # used to factor out row b from row a
	source[a] = listdiff(source[a],source[b])
	y[a] = listdiff(y[a],y[b])

def hasit(a) : # return a list of all entries in Y containing a
	foundlist = list()
	for i in range(len(y)):
		if a in y[i] : foundlist.append(i)
	return foundlist

def findup(a) : # return a list of entries in y containing a, started at a
	foundlist = list()
	for i in range(a,len(y)):
		if a in y[i] : foundlist.append(i)
	return foundlist

def findgreater_reduce(a) : # return a list of entries in y containing a, started after a AND reduce2 them
	foundlist = list()
	for i in range(a+1,len(y)):
		if a in y[i] :
			foundlist.append(i)
			reduce2(i,a)
	return foundlist

def grindup(a) : # get entry a reduced from all greater entries
	lst = findup(a)
	if len(lst) >= 1 :
		if lst[0] <> a :
			swap2(a,lst[0])
	return findgreater_reduce(a)

def grinddown(a) : # reduce out all entries less than a
	lst = hasit(a)
	for i in lst:
		if (i < a):
			reduce2(i,a)



map(grindup,range(K))            # forward elimination in the matrix
map(grinddown,range(K-1,0,-1))   # factoring out single entries


