#include <stdio.h>

int main(void) {
	char a[100];
	scanf("%s",a);
	int i,j,l=strlen(a),f=0;
	for(i=0;i<l;i++)
	{
		if(!isalpha(a[i]))
		{
		f=1;
		break;
		}
	}
	if(f==1)
	printf("No");
	else
	printf("Alphabet");
	return 0;
}
