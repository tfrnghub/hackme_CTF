#include<stdio.h>
unsigned char iv[8]={0xe3, 0x10, 0x3c, 0x8c, 0x28, 0x47, 0x87, 0xa9};
unsigned char sbox[0x100];
char key[10]="keykey";
char plain[20]="012fuck3456789";

void box_c(unsigned int a,unsigned int b)
{
    int i;
    int tmp;
    for(i=0;i<0x24;i++)
    {
        a=((0xff-a)*13)&0xff;
        b=((0xff-b)*17)&0xff;
        tmp=sbox[a];
        sbox[a]=sbox[b];
        sbox[b]=tmp;
        
    }
}

int main()
{
    plain[14]=0x0a;
    int i,j;
    for(i=0;i<0x100;i++)
        sbox[i]=i;
    unsigned int tmp;
    for(i=0;i<8;i++)
    {
        box_c(i,iv[i]);
    }
    for(i=0;i<0x100;i++)
    {
        printf("%02x ",sbox[i]);
        if((i+1)%0x10==0)
            printf("\n");
    }
    for(i=0;i<15;i++)
    {
        box_c(i%3,key[i%3]);
        tmp=0xDEADBEEF;
        for(j=0;j<0x100;j++)
        {
            tmp=(tmp*0x5a77)^(sbox[j]*0xc8763);
            tmp=tmp&0xffffffff;
        }
        printf("=====\n%08x\n",tmp);
        tmp^=(plain[i]*17)&0xff;
        printf("%08x\n",tmp);
        
    }
    
    return 0;
}
