'''
	Written by: Shubham Jain<bugdivine@gmail.com>
	Sarches list aList for element x
	Return -1 if not present otherwise index.
'''

def binary_search(aList, x):
	lo=0
	hi=len(aList)-1
	while lo<=hi:
		mid=(hi+lo)/2
		if aList[mid]==x:
			return mid
		if aList[mid]>x:
			hi=mid-1
		else:
			lo=mid+1
	return -1

'''
# TEST
print binary_search([1, 2, 3, 4, 5], 1)
print binary_search([1, 2, 3, 4, 5], 2)
print binary_search([1, 2, 3, 4, 5], 3)
print binary_search([1, 2, 3, 4, 5], 4)
print binary_search([1, 2, 3, 4, 5], 5)
print binary_search([1, 2, 3, 4, 5], 6)
print binary_search([1, 2, 3, 4, 5], 0)
'''