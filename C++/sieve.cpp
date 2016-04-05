#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;

int *sieve(int n)
{
	int *result = (int *)malloc((n+1)*sizeof(int));
	for (int i = 0; i < n+1; ++i)
	{
		result[i]=(i+1)%2;
	}
	result[1] = 1;
	result[2] = 0;
	double x = sqrt(n);
	for (int i = 3; i <= x; ++i)
	{
		if (result[i]==0)
		{
			int j=i*i;
			while (j<=n)
			{
				result[j]=1;
				j+=i;
			}
		}
	}
	return result;
}
