'''
	Author: Shubham Jain < bugdivine@gmail.com >
	
	n is the number of nodes
	edge is the list of all undirected edges
	in [[x, y, length], .....] format
	s is the starting node for building MST

	Returns the various vertices joined
	in a group in a MST using kruskal algorithm
'''


import itertools

'''
	Searches for a number is two dimensional list
'''
def find(hay, needle):
	c = 0
	for a in hay:
		if needle in a:
			return c
		c += 1
	return -1

def kruskal(n, edge, s):
	# Sort edges by their weights
	edge.sort(key=lambda a: (a[2], a[0]+a[1]+a[2]))

	# Initialise mst
	# Disjoint data structure to check for cycle
	mst = [[s]]

	# Queue to maintain list of all elements yet
	# to be added to mst
	queue = [a for a in range(n)]
	del queue[s]

	# Iterate over sorted list of edges
	for e in edge:
		if len(queue)==0 and len(mst)==1:
			break

		# Find if two nodes forming a cycle
		a = find(mst, e[0])
		b = find(mst, e[1])

		# Both nodes adding new
		if a==b and a==-1:
			newSet = [e[0], e[1]]
			mst.insert(len(mst), newSet)
			queue.remove(e[0])
			queue.remove(e[1])
		# First node is new
		elif a!=b and a==-1:
			mst[b].insert(len(mst[b]), e[0])
			queue.remove(e[0])
		# Second node is new
		elif a!=b and b==-1:
			mst[a].insert(len(mst[a]), e[1])
			queue.remove(e[1])
		# Both node old but not forming cycle
		elif a!=b:
			newSet = list(itertools.chain(mst[a],mst[b]))
			mst.insert(len(mst), newSet)
			del mst[min(a, b)]
			del mst[max(a, b)-1]

	return mst

'''
# FOR TEST PURPOSE
n, m = map(int, raw_input().split())
edge = []
for a in range(m):
	e = [int(A)-1 for A in raw_input().split()]
	e[2] += 1
	edge.insert(len(edge), e)
s = int(input())-1
print kruskal(n, edge, s)
'''
'''
#INPUT
4 6
1 2 5
1 3 3
4 1 6
2 4 7
3 2 4
3 4 5
1
'''
