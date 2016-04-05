long arraySum(int *arr, int n)
{
	long sum = 0;
	for (int i = 0; i < n; ++i)
	{
		sum+=*arr;
		arr++;
	}
	return sum;
}
