'''
	Written by: Shubham Jain<bugdivine@gmail.com>
	Sorts a list using merge sort
	Returns the sorted list
'''

def merge(aList, bList):
	a = len(aList)
	b = len(bList)
	a_s = 0
	b_s = 0
	result = []
	c = 0
	while a_s<a or b_s<b:
		if a==a_s:
			result.insert(c, bList[b_s])
			c+=1
			b_s+=1
		elif b==b_s:
			result.insert(c, aList[a_s])
			c+=1
			a_s+=1
		else:
			if aList[a_s]<=bList[b_s]:
				result.insert(c, aList[a_s])
				c+=1
				a_s+=1
			else:
				result.insert(c, bList[b_s])
				c+=1
				b_s+=1
	return result

def merge_sort(aList):
	l=0
	r=len(aList)-1
	if l<r:
		m = (l+r)/2
		left = merge_sort(aList[l:m+1])
		right = merge_sort(aList[m+1:r+1])
		return merge(left, right)
	return aList

'''
#TEST
arr = [9, 8, 4, 6, 7, 5]
print merge_sort(arr)
arr = [9, 5, 4, 30, 7, 8, 6]
print merge_sort(arr)
'''