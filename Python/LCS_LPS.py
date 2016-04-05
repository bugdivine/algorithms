'''
	Written by: Shubham Jain <bugdivine@gmail.com>
	Finds the length of longest common
	subsequence of two strings
	Run time:- O(n^2)
'''

def LCS(s1, s2):
	l1, l2 = len(s1), len(s2)
	L = [[0 for a in range(l2+1)] for b in range(l1+1)]
	for a in xrange(1,l1+1):
		for b in xrange(1,l2+1):
			if s1[a-1]==s2[b-1]:
				L[a][b]=L[a-1][b-1]+1
			else:
				L[a][b]=max(L[a-1][b],L[a][b-1])
			pass
	return L[l1][l2]

'''
	Written by: Shubham Jain <bugdivine@gmail.com>
	Returns the longest common subsequence
	Run time:- O(n^2)
'''
def getLCS(s1, s2):
	l1, l2 = len(s1), len(s2)
	L = [[0 for a in range(l2+1)] for b in range(l1+1)]
	for a in xrange(1,l1+1):
		for b in xrange(1,l2+1):
			if s1[a-1]==s2[b-1]:
				L[a][b]=L[a-1][b-1]+1
			else:
				L[a][b]=max(L[a-1][b],L[a][b-1])

	l3 = L[l1][l2]
	a, b = l1, l2
	sub = ""

	while l3>0:
		if s1[a-1]==s2[b-1]:
			a-=1
			b-=1
			l3-=1
			sub = s1[a]+sub
		else:
			if L[a][b]==L[a][b-1]:
				b-=1
			else:
				a-=1
	return sub

'''
	Written by: Shubham Jain <bugdivine@gmail.com>
	Finds the length of longest palindromic
	subsequence of two strings
	Run time:- O(n^2)
'''
def LPS(s1):
	s2 = s1[::-1]
	return LCS(s1, s2)

'''
	Written by: Shubham Jain <bugdivine@gmail.com>
	Returns the longest palindromic subsequence
	Run time:- O(n^2)
'''
def getLPS(s1):
	s2 = s1[::-1]
	return getLCS(s1, s2)

