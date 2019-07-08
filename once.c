#include <stdio.h>

int main(void) {
	int size,ind;
	scanf("%d",&size);
	int arr[size];
	for(ind=0;ind<size;ind++)
	{
		scanf("%d",&arr[ind]);
	}
	int uniq=arr[0];
	for(ind=1;ind<size;ind++)
	{
		uniq^=arr[ind];
	}
	printf("%d",uniq);
	
	return 0;
}
