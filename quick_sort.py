'''
	Written by: Shubham Jain<bugdivine@gmail.com>
	Sorts a list using quick sort
	in the index range [l, r] both inclusive
'''

def partition(aList, l, r):
	pivot = arr[r]
	p = r
	i = l-1
	for a in range(l, r+1):
		if a==p:
			continue
		if aList[a]<=pivot:
			i+=1
			if i==p:
				i+=1
			aList[i], aList[a] = aList[a], aList[i]
	aList[i+1], aList[p] = aList[p], aList[i+1]
	return i+1


def quick_sort(aList, l, r):
	if l<r:
		p=partition(aList, l, r)
		quick_sort(aList, l, p-1)
		quick_sort(aList, p+1, r)

'''
#TEST
arr = [9, 8, 4, 6, 7, 5]
quick_sort(arr, 0, len(arr)-1)
print arr
arr = [9, 5, 4, 30, 7, 8, 6]
quick_sort(arr, 0, len(arr)-1)
print arr
'''