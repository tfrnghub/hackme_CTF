#include <stdio.h>
int main()
{
    char a[18]="UIJT.JT.ZPVS.GMBH";
    char b[18]={0};
    int i;
    for (i=0;i<17;i++)
        b[i]=a[i]-1;
    puts(b);
    return 0;
}
