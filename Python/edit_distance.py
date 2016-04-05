def edit_distance(s1, s2):
	l1 = len(s1)
	l2 = len(s2)
	dist = [[0 for a in range(l2+1)] for a in range(l1+1)]
	for a in range(l1+1):
		for b in range(l2+1):
			if a==0:
				dist[a][b]=b
			elif b==0:
				dist[a][b]=a
			elif s1[a-1]==s2[b-1]:
					dist[a][b]=dist[a-1][b-1]
			else:
				dist[a][b]=1+min(dist[a-1][b], dist[a][b-1], dist[a-1][b-1])
	return dist[l1][l2]
'''
s1 = 'sunday'
s2 = 'saturday'
print edit_distance(s1, s2)
'''