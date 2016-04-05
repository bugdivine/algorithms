#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>

// Print an array
void printArr(int *arr, int n);

// Merge two arrays arr1 and arr2 of sizes s1 and s2 respectively
int *merge(int *arr1, int s1, int *arr2, int s2);

// Merge Sort an array from index l to r(both inclusive)
int *mergeSort(int *arr, int l, int r);

int *merge(int *arr1, int s1, int *arr2, int s2)
{
	int *result = (int *)malloc((s1+s2)*sizeof(int));
	int a=0, b=0, c=0;
	while (c < s1+s2)
	{
		if (a>=s1)
			result[c++]=arr2[b++];
		else if (b>=s2)
			result[c++]=arr1[a++];
		else if (arr1[a]<=arr2[b])
			result[c++]=arr1[a++];
		else
			result[c++]=arr2[b++];
	}
	return result;
}

int *mergeSort(int *arr, int l, int r)
{
	if (l == r)
		return arr+l;
	int *part1 = mergeSort(arr, l, (l+r)/2);
	int *part2 = mergeSort(arr, (l+r)/2+1, r);
	return merge(part1, (l+r)/2-l+1, part2, r-(l+r)/2);
}

void printArr(int *arr, int n)
{
	for (int i = 0; i < n; ++i)
	{
		printf("%d ", arr[i]);
	}
	printf("\n");
}
