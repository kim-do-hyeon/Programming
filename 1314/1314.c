#include <stdio.h>
void Reset(char result);
int main()
{
	int i,j;
	int n = 0;
	char arr[100][100];
	
	scanf("%d",&n);

	char result = 'A';
	
	for(i = 0; i < n; i++)
	{
		if(i % 2 == 0)
		{
			for(j = 0; j < n; j++)
			{
				arr[j][i] = result++;
				Reset(result);
			}
		}
		else
		{
			for(j = n - 1; j >= 0; --j)
			{
				arr[j][i] = result++;
				Reset(result);
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

void Reset(char result)
{
	if(result > 'Z')
	{
		result = 'A';
	}
}
