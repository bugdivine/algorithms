#include <iostream>
#include <cstdio>
#include <cstring>
#include <deque>
#include <cstdlib>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#define FOR(i, a, b) for(int i=a; i<b; i++)
#define RFOR(i, a, b) for(int i=a-1; i>=b; i--)
inline int MIN(int a, int b) { return (a<b)?a:b; }
inline int MAX(int a, int b) { return (a<b)?b:a; }
inline int ABS(int a) { if (a<0) a=-a; return a; }

typedef long long Int;
using namespace std;

#define MAX 100000

struct node
{
	int lsum;
	int rsum;
	int msum;
};

int arr[MAX+1];

node tree[4*MAX+1];

void init(int n, int l, int r)
{
	if (l==r)
	{
		tree[n] = ( (node) { arr[l], arr[l], arr[l] } );
	}
	else
	{
		int mid = (l+r)/2;
		init(2*n, l, mid);
		init(2*n+1, mid+1, r);
		node left = tree[2*n],
			right = tree[2*n+1];
		tree[n].lsum = left.msum;
		tree[n].rsum = right.msum;
		tree[n].msum = left.msum+right.msum;
	}
}

node query(int n, int a, int b, int l, int r)
{
	if (a==l && b==r)
	{
		return tree[n];
	}
	else if (r <= (a+b)/2)
	{
		return query(n*2, a, (a+b)/2, l, r);
	}
	else if (l > (a+b)/2)
	{
		return query(n*2+1, (a+b)/2+1, b, l, r);
	}
	node left = query(n*2, a, (a+b)/2, l, (a+b)/2);
	node right = query(n*2+1, (a+b)/2+1, b, (a+b)/2+1, r);

	return (
		(node) {
			left.msum,
			right.msum,
			left.msum+right.msum
		}
	);
}

void update(int n, int a, int l, int r)
{
	if (l==r)
	{
		tree[n] = ( (node) { arr[l], arr[l], arr[l] } );
	}
	else if (a <= (l+r)/2)
	{
		update(n*2, a, l, (l+r)/2);
		tree[n].lsum = tree[2*n].msum;
		tree[n].msum = tree[2*n].msum+tree[2*n+1].msum;
	}
	else if (a > (l+r)/2)
	{
		update(n*2+1, a, (l+r)/2+1, r);
		tree[n].rsum = tree[2*n+1].msum;
		tree[n].msum = tree[2*n].msum+tree[2*n+1].msum;
	}
}


int main()
{
	int n;
	scanf(" %d", &n);
	FOR(i,0,n)
	{
		scanf(" %d", &arr[i]);
	}
	init(1, 0, n);
	int q;
	scanf(" %d", &q);
	while (q--) {
		int x, a, b;
		scanf("%d %d %d", &x, &a, &b);
		if (x==0)
		{
			a--; b--;
			printf("%d\n", query(1, 0, n, a, b).msum);
		}
		else
		{
			a--;
			arr[a]+=b;
			update(1, a, 0, n);
		}
	}
	return 0;
}
