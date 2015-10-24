def unary(n):
	x = ['1' for x in range(n)]
	x.extend('0')
	return ''.join(x)

def gamma(n):
  	s = bin(n)[2:]
  	while s[0] == '0':
	  	s = s[1:]
  	s = s[1:]
  	n = unary(len(s))
	return n + ',' + s

def delta(n):
  	s = bin(n)[2:]
  	while s[0] == '0':
	  	s = s[1:]
  	s = s[1:]
  	n = unary(len(s))
	return gamma(len(s)) + ',' + s

n = int(input())
print delta(n)
