'''
	Written by: Shubham Jain<bugdivine@gmail.com>
	Dijkstra algorithm to find shortest path from node s
	edge:- [[adjacent nodes of kth vertices].....k]
	dist:- [[corresponding distance].....k]
	s:- starting node
'''
def dijkstra(edge, dist, s):
	queue = [s]
	d = [1000000 for a in edge]
	d[s] = 0
	while len(queue)>0:
		k = queue.pop()
		for a, b in zip(edge[k], dist[k]):
			if d[k]+b<d[a]:
				d[a]=d[k]+b
				queue.insert(0, a)
	print d

#dijkstra([[1, 7], [0, 2, 7], [1, 3, 5, 8], [2, 4, 5], [3, 5], [2, 4, 6], [3, 5, 7, 8], [0, 1, 6, 8], [2, 6, 7]],
#	[[4, 8], [4, 8, 11], [8, 7, 4, 2], [7, 9, 14], [9, 10], [4, 10, 2], [14, 2, 1, 6], [8, 11, 1, 7], [2, 6, 7]], 
#	0 )
