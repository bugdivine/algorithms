#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <stdlib.h>

// Print an array
void printArr(int *arr, int n);

void printArr(int *arr, int n)
{
	for (int i = 0; i < n; ++i)
	{
		printf("%d ", arr[i]);
	}
	printf("\n");
}
