'''
	Author: Shubham Jain < bugdivine@gmail.com >
	
	s is the list for which we want to find the powerset
	Generates all powersets of s
'''

def powerset(s):
    n = len(s)
    masks = [1<<j for j in xrange(n)]
    for i in xrange(2**n):
        yield [s[j] for j in range(n) if (masks[j] & i)]
