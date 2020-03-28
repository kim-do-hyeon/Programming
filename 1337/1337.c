#include <stdio.h>

int main()
{
	int N;
	scanf("%d", &N);
	
	int i, j, k;
	int arr[100][100];
	int num = 0;
	int flag = 0;
	int n = N;

	for(i = 0; i < N; i++)
	{
		for(j = 0;j < N; j++)
		{
		    arr[i][j] = 10;
		}
	}

	j = -1;
	k = -1;
	while(1){
		for(i = 0; i < n; i++)
		{
			switch(flag)
			{
				case 0:
				    j++;
				    k++;
				    break;
				case 1:
				    k--;
				    break;
				case 2:
				    j--;
				    break;
			}
			arr[j][k] = num;
			num = (num + 1) % 10;
		}
		flag = (flag + 1) % 3;
		n--;
		if(n == 0)
		{
			break;	
		}
	}

    for(i = 0; i < N; i++)
	{
        for(j = 0; j < N; j++)
		{	
            if(arr[i][j] != 10)
			{
				printf("%d ", arr[i][j]);	
			}
        }
        printf("\n");
    }
}
