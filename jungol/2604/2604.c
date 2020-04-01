#include <stdio.h>
#include <string.h>
int main()
{
	int i, height;
	char dish[100];
	int count;
	scanf("%s", dish);
	height = 10;
	count = strlen(dish);
	for(i = 1; i < count; i++)
	{
		if(dish[i] == dish[i - 1])
		{
			height += 5;
		}
		else
		{
			height += 10;
		}
	}
	printf("%d",height);
	return 0;
}
