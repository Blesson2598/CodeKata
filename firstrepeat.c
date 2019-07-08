#include <iostream>
using namespace std;

int main() {
	int size;
	scanf("%d",&size);
	int arr[size],mark[size]={0};
	int ind,ind2;
	for(ind=0;ind<size;ind++)
	{
		scanf("%d",&arr[ind]);
	}
	for(ind=0;ind<size;ind++)
	{
		int flag=0;
		for(ind2=ind+1;ind2<size;ind2++)
		{
			if(arr[ind]==arr[ind2])
			{
				if(flag==0)
				{
			mark[arr[ind]]=ind2;
				flag=1;
				arr[ind2]=-1;
				}
				else{
					arr[ind2]=-1;
				}
			}
		}
	}
	int min=100000,ele=0;
	for(ind=0;ind<size;ind++)
	{
		if(mark[arr[ind]]<min && arr[ind]!=-1 && mark[arr[ind]]!=0)
		{
		min=mark[arr[ind]];
		ele=arr[ind];
		}
		
	}
	printf("%d",ele);
	return 0;
}
