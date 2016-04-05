'''
	Author: Shubham Jain < bugdivine@gmail.com >
	
	arr is the array
	Returns the maximum sum of contigous and
	non-contigous elements in the array respectively
'''
def max_sum(arr):
	# diff_array for sum of contigous elements
	diff_array = [0 for a in range(n)]
	# sum_array for sum of non-contigous elements
	sum_array = [0 for a in range(n)]
	# to find maximum element in array
	_max = -10000000
	# to check if some element is positive in array
	flag = 0
	diff_array[0] = max(0, arr[0])
	if (arr[0]>=0):
		flag = 1
		if arr[0]>_max:
			_max = arr[0]
		sum_array[0] = arr[0]
	for a in range(1, n):
		if arr[a]>_max:
			_max=arr[a]
		# to find max contiguos sum
		# keep diff zero if going negative
		if arr[a]+diff_array[a-1]<0:
			diff_array[a]=0
		else:
			diff_array[a]=diff_array[a-1]+arr[a]
		# do not decrease sum if arr is negative
		sum_array[a] = max(sum_array[a-1], sum_array[a-1]+arr[a])
		if arr[a]>=0:
			flag=1
	if flag==0:
		# for at least one element in arr to be taken
		return _max, _max
	else:
		return max(diff_array), sum_array[n-1]
