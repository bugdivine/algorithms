'''
	Written by: Shubham Jain<bugdivine@gmail.com>
	Depth first traversal of a graph
	edge:- [[adjacent nodes of kth vertices].....k]
	stack:- Nodes neighbours to already visited nodes
	visited:- Already visited nodes.
'''
def DFS(edge, stack, visited):
	ledge = len(edge)
	lstack = len(stack)
	for a in stack:
		visited[a] = 1
		for b in edge[a]:
			if b in stack:
				continue
			visited[b] = 1
			stack.insert(0, b)
			DFS(edge, stack, visited)
'''
s = [0]
visited = [0 for a in range(4)]
DFS([[1, 2], [2], [0, 3], [3]],
	s,
	visited )
print s[::-1]
'''