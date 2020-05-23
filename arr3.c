#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n,above=0,below=0,sum=0,average;
    int num[100],i;
    printf("enter the numbers:\n");
    scanf("%d",&n);
    printf("enter the elements :\n");
    for( i=0;i<n;i++){
        scanf("%d",&num[i]);
        sum+=num[i];
    }
    average=sum/n;
    for( i=0;i<n;i++){
        if(num[i]>average){
            above++;
        }
        else if(num[i]<=average)
            below++;
    }
    printf("\nthe average is:%d\n",average);
    printf("\nthe above are : %d and below are :%d",above,below);
    return 0;
}
