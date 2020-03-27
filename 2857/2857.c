#include <stdio.h>
#include <string.h>
int main()
{
    int i,j;
    int max = 0;
    char line[5][15] = {0};
    for(i = 0; i < 5; i++)
    {
        scanf("%s",line[i]);
        if(strlen(line[i]) > max)
        {
            max = strlen(line[i]);
        }
    }
    for(i = 0; i < max; i++)
    {
        for(j = 0; j < 5; j++)
        {
            if(line[j][i] == NULL)
            {
                continue;
            }
            printf("%c",line[j][i]);
        }
    }
}