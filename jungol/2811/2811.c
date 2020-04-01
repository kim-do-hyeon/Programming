#include <stdio.h>
void prime_number(int n)
{
	int i;
	if(n < 2)
	{
		return 0;
	}
	for(i = 2; i < n; i++)
	{
		if(n % i == 0)
		{
			return 0;
		}
	}
	return 1;
}
int main()
{
	int i;
	int num[5] = {0,};
	for(i = 0; i < 5; i++)
	{
		scanf("%d",&num[i]);
	}
	
	for(i = 0; i < 5; i++)
	{
		if(num[i] < 2)
		{
			printf("number one");
		}
		else if(prime_number(num[i]))
		{
			printf("prime number");
		}
		else
		{
			printf("composite number");
		}
	}
	
}
