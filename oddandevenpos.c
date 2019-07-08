#include <stdio.h>

int main(void) {
	int size,ind;
	scanf("%d",&size);
	int arr[size];
	for(ind=0;ind<size;ind++)
	{
		scanf("%d",&arr[ind]);
		if(ind%2==0 && arr[ind]&1)
		printf("%d ",arr[ind]);
		else if(ind&1 && arr[ind]%2==0)
		printf("%d ",arr[ind]);
	}
	return 0;
}
