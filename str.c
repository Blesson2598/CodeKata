#include <stdio.h>

int main(void) {
 char a[10]={'H','e','l','l','o','\0'};
 int n;
 scanf("%d",&n);
 for(int i=0;i<n-1;i++,printf("\n"))
	printf("%s",a);
	if(n>0)
	printf("%s",a);
	return 0;
}
