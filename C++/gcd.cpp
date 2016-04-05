
int GCD(int a, int b)
{
	int tmp;
	while ((tmp=(a%b))!=0)
	{
		a=b;
		b=tmp;
	}
	return b;
}
