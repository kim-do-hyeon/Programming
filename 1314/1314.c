#include <stdio.h>
void Reset(int result);
int main()
{
	int i,j;
	int n = 0;
	char arr[100][100];
	
	scanf("%d",&n);

	int result = 65;
	
	for(i = 0; i < n; i++)
	{
		if(i % 2 == 0)
		{
			for(j = 0; j < n; j++)
			{
				arr[j][i] = result++;
				if(result > 90)
				{
					result = 65;
				}
			}
		}
		else
		{
			for(j = n - 1; j >= 0; --j)
			{
				arr[j][i] = result++;
				if(result > 90)
				{
					result = 65;
				}
			}
		}
	}
	
	for(i = 0; i < n; ++i)
	{
		for(j = 0; j < n; ++j)
		{
			printf("%c ",arr[i][j]);	
		}
		printf("\n");;
	}
}
