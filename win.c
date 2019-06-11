#include <stdio.h>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
int main(void) {
	char a[1000],temp[100];
	int n,i,j,w,min=INT_MAX,k=0;
	scanf("%s %d",a,&n);
	int l=strlen(a);
	for(i=0;i<l;i++)
	{
		int f=0;
		for(j=i+1;j<l;j++)
		{
			if(a[i]>=a[j])
			{
				f=1;
				a[i]='{';
				break;
			}
		}
		if(f==0)
		temp[k++]=a[i];
	}
	temp[k]='\0';
	int t=atoi(temp);
	printf("%d",t);
	
}
