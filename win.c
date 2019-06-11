#include <stdio.h>
#include<string.h>
#include<stdlib.h>
#include<limits.h>
int main(void) {
	char a[1000],temp[100];
	int n,i,j,w,min=INT_MAX,k=0;
	scanf("%s %d",a,&n);
	int l=strlen(a);
	w=l-n;
	for(i=0;i<=l-w;i++)
	{
	 for(j=i;j<i+w;j++)
	 temp[k++]=a[j];
	 int t=atoi(temp);
	 if(t<min)
	 min=t;
	 for(int v=0;v<k;v++)
	 temp[v]='\0';
	 k=0;
	}
	printf("%d",min);
	return 0;
}
