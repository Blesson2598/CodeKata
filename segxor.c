#include <stdio.h>

int main(void) {
	int size,vals;
	scanf("%d %d",&size,&vals);
	int arr[size],iterator1,iterator2;
	for(iterator1=0;iterator1<size;iterator1++)
		scanf("%d",&arr[iterator1]);
	int start,end;
	for(iterator1=0;iterator1<vals;iterator1++)
	{
	scanf("%d %d",&start,&end);
	int xor=0;
	for(iterator2=start-1;iterator2<end;iterator2++)
	xor^=arr[iterator2];
	printf("%d\n",xor);
	}
	return 0;
}
