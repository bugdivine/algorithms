#include <iostream>
#include <cstdio>
using namespace std;

int isPalindrome(int n)
{
	int str[10];
	int l=0;
	while(n>0)
	{
		str[l++]=n%10;
		n/=10;
	}
	for (int i = 0; i < l/2; ++i)
	{
		if (str[i]!=str[l-i-1])
			return 0;
	}
	return 1;
}
