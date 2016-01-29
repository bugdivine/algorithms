'''
	Author: Shubham Jain < bugdivine@gmail.com >
	
	n is the number to which we want to run sieve
	Returns a list arr
	arr[i]=0 => prime
	arr[i]=1 => composite
'''
def sieve(n):
	arr = [0 for a in range(n+1)]
	for a in range(2, n+1):
		if arr[a]==0:
			for b in range(a+a, n+1, a):
				arr[b] = 1
	return arr

'''
#TEST
n = int(input())
print sieve(n)
'''
