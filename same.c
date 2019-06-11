#include <stdio.h>

int main(void) {
char s1[100],s2[100];
scanf("%s %s",s1,s2);
int i,j,l1=strlen(s1),l2=strlen(s2),f=0,c=0;
for(i=0;i<l1;i++)
{
	f=0;
	for(j=0;j<l2;j++)
	{
		if(s1[i]==s2[j])
		{
			f=1;
			s2[j]='{';
		}
	
	}
	if(f==1)
	{
		for(int j1=i+1;j1<l1;j1++)
		{
			if(s1[i]==s1[j1])
			s1[j1]='{';
			
		}
	s1[i]='{';
	
	}
}
for(i=0;i<l1;i++)
{
	if(isalpha(s1[i]))
	c++;
}
for(i=0;i<l2;i++)
{
	if(isalpha(s2[i]))
	c++;
}
printf("%d",c);
	return 0;
}
