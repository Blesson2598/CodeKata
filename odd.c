#include <stdio.h>

int main(void) {
long long int num,mask=1;
scanf("%lld",&num);
if(num<0)
{
printf("invalid");
return 0;
}
if((num&mask))
printf("Odd");
else
printf("Even");
}
