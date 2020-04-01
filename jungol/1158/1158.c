#include <stdio.h>
#include <string.h>
void insertion_sort(int unsorted_list)
{
	int i,j;
	for(j = 0; j < strlen(unsorted_list); j++)
	{
		int key = unsorted_list[j];
		i = j - 1;
		while (i >= 0 && unsorted_list[i] > key)
		{
			unsorted_list[i + 1] = unsorted_list[i]
			i = i - 1;
		}
		unsorted_list[i + 1] = key
		printf("%d ",unsorted_list)
	}
	return unsorted_list;
}
int main()
{
	int num;
	scanf("%d",&num);
	int unsorted_list[100] = {0};
	for (i = 0; i < num; i++)
	{
		scanf("%d",unsorted_list[i]);
	}
	int sorted_list = insertion_sort(unsorted_list);
}
