'''
	Written by: Shubham Jain <bugdivine@gmail.com>
	Searches a string for a pattern using KMP search
'''

def KMP(hay, needle):
	M = len(hay)
	N = len(needle)

	lps = calculateLPS(needle)

	i=0
	j=0
	while i<M:
		if hay[i]==needle[j]:
			i+=1
			j+=1
		if j==N:
			return i-j
		if hay[i]!=needle[j]:
			if j!=0:
				j=lps[j-1]
			else:
				i+=1
	return -1

def calculateLPS(s):
	l = len(s)
	arr = [0 for a in s]
	m = 0
	a = 1
	while a<l:
		if s[a]==s[m]:
			arr[a]=m+1
			m+=1
			a+=1
		else:
			if m!=0:
				m=arr[m-1]
			else:
				arr[a]=0
				a+=1
	return arr

'''
#TEST
print calculateLPS('AABAACAABAA')
print calculateLPS('ABCDE')
print calculateLPS('AAAAA')
print calculateLPS('AAABAAA')
print calculateLPS('AAACAAAAAC')

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
print KMP(txt, pat), txt.find(pat)
'''