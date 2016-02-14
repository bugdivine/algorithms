'''
	Written by: Shubham Jain<bugdivine@gmail.com>
	0-1 knapsack problem
	For a capacity of weight 'w' find the max value we can obtain
'''

def knapsack(w, weight, value):
	v = len(value)
	ksp = [[0 for a in range(w+1)] for b in range(v+1)]
	for a in range(v+1):
		for b in range(w+1):
			if a==0 or b==0:
				ksp[a][b]=0
			elif weight[a-1]<=b:
				ksp[a][b]=max(value[a-1] + ksp[a-1][b-weight[a-1]],  ksp[a-1][b])
			else:
				ksp[a][b]=ksp[a-1][b]
	return ksp[v][w]
'''
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(W, wt, val))
'''