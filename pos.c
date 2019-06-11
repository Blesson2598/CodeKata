#include<stdio.h>
#include <stdlib.h>
 
int main()
{
    long long int num;
    scanf("%lld",&num);
    if(num<0)
    printf("Negative");
    if(num==0)
    printf("Zero");
    if(num>0)
    printf("Positive");
}
