'''
	Written by: Shubham Jain<bugdivine@gmail.com>
	BFS traversal of a graph
	edge:- [[adjacent nodes of kth vertices].....k]
	s:- index of starting node
'''
def BFS(edge, s):
	queue = [s]
	ledge = len(edge)
	lqueue = 1
	visited = [0 for a in range(ledge)]
	b = 0
	flag = 1
	while ledge>lqueue and flag!=0:
		flag=0
		visited[queue[b]]=1
		for a in edge[queue[b]]:
			if visited[a]!=0:
				continue
			queue.insert(lqueue, a)
			lqueue+=1
			flag=1
		b+=1
	print queue

#BFS([[1, 2], [2], [0, 3], [3]],
#	2 )
