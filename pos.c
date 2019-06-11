#include<stdio.h>
#include <stdlib.h>
#include<string.h>
#include<ctype.h>
int main()
{
    char a[100];
    scanf("%s",&a);
    int l=strlen(a);
    for(int i=0;i<l;i++)
    {
    	
    	if(a[0]=='-')
    	continue;
    	if(isalpha(a[i]) || !isalnum(a[i]))
    	{
    		printf("Invalid");
    		return 0;
    	}
    }
    int num=atoi(a);
    if(num<0)
    printf("Negative");
    if(num==0)
    printf("Zero");
    if(num>0)
    printf("Positive");
}
