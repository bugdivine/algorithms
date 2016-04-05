
class node{
	public:
		int n;
		int d;
		node(int a, int b){
			n = a;
			d = b;
		}
};

bool operator<(const node& a, const node& b) {
	return a.d > b.d;
}

int djikstra(std::vector< pair<int, int> > *edge, int n, int a, int b)
{
	int cost[n];
	bool visited[n];
	for (int i = 0; i < n; ++i)
	{
		cost[i] = INT_MAX;
		visited[i] = false;
	}
	cost[a] = 0;
	priority_queue< node > myqueue;
	myqueue.push(node(a, 0));
	while (!myqueue.empty())
	{
		node x = myqueue.top();
		myqueue.pop();
		int y = x.n;
		if (visited[y])
			continue;
		visited[y] = true;
		int z = edge[y].size();
		for (int i=0; i<z; i++)
		{
			int p = edge[y][i].first;
			int c = edge[y][i].second+x.d;
			if (cost[p] > c)
			{
				cost[p] = c;
				myqueue.push(node(p, c));
			}
		}
	}
	return cost[b];
}
