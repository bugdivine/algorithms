#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
using namespace std;

/**
 * Sieve of Eratosthenses
 * https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
 * n: Number till which we want to find if a number is prime or not
 * returns: Boolean array. 0 => Prime, 1 => Composite
 */
bool *sieve(int n)
{
	assert(n >= 1);
	bool *result = (bool *)malloc((n+1)*sizeof(bool));

	// Mark all even numbers as composite and all odd numbers as prime
	for (int i = 0; i < n+1; ++i)
		result[i] = (i+1)%2;

	// Cases which fail the generalization that all even numbers are 
	// composite
	result[1] = 1;
	if (n >= 2)
		result[2] = 0;

	double x = sqrt(n);
	// Iterate over all the prime marked numbers and
	// mark their multiples as composite
	// All numbers greater than x and less than n are already marked as
	// prime or composite as multiples of lesser numbers than x
	for (int i = 3; i <= x; i+=2)
	{
		if (result[i]==0)
		{
			int j = i*i;
			while (j <= n)
			{
				result[j] = 1;
				j += i;
			}
		}
	}
	return result;
}
