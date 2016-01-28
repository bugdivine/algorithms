# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
	Author: Shubham Jain < bugdivine@gmail.com >
	
	n is the number of nodes
	edge is the list of all undirected edges
	in [[x, y, length], .....] format
	s is the starting node for building MST

	Returns the order of traversal of all nodes
	to obtain MST
'''
def prim(n, edge, s):
	# Weightage of all nodes
	weight = [1000000000 for a in range(n)]
	weight[s] = 0

	# Node yet to be added to MST
	queue = [a for a in range(n)]
	del queue[s]

	# Nodes already added to MST
	mst = [s]

	# Setting current node
	node = s

	while len(queue)>0:
		'''
			Update all neighbours of previous node
		'''
		for a in edge:
			if a[0]==node and a[1] not in mst and weight[a[1]]>a[2]:
				weight[a[1]] = a[2]
			elif a[1]==node and a[0] not in mst and weight[a[0]]>a[2]:
				weight[a[0]] = a[2]

		'''
			Find a new node, not already chosen
			and with minimum weight
		'''
		w = 1000000000
		for a in queue:
			if weight[a]<w:
				node = a
				w = weight[a]

		'''
			Add new node to MST
		'''
		queue.remove(node)
		mst.insert(len(mst), node)

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
print prim(n, edge, s)
'''
'''
#INPUT
5 6
1 2 3
1 3 4
4 2 6
5 2 2
2 3 5
3 5 7
1
'''
