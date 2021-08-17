#include <stdio.h>
#include <string.h>

typedef long unsigned int u64;
typedef unsigned int u32;
typedef unsigned char u8;

u64 aaa(u64 x)
{
    return (0x777777 * x + 12345) & 0x7FFFFFFFFFFFFFFF;
}


int cipher(FILE *fp,FILE *op,char password[],int mode)
{
    u64 v7 = 0xDEADBEEF01234567;
    int i,j,k;
    u8 c;
    u64 tmp;
    k=0;
    do
    {
        c=password[k];
        tmp=777 * c ^ 3333 * aaa(v7);
        v7 = ((tmp >> 13)^tmp)+ 0x5555555555555555;
        for(i=0;i<c+66;i++)
        {
            v7 = aaa(v7);
        }
        k++;
    }while(c);
     __int128 v11=7;
    while(1)
    {
        int ch=fgetc(fp);
        u8 och;
        if(ch==EOF)
            break;
        for(i=0;i<v11;i++)
        {
            v7 = aaa(v7);
        }
        if(mode)
        {
            v11 = ((21 * v11 * 0xCCCCCCCCCCCCCCCD >> 64) >> 3) ^ ch;
            och = v7 ^ ch;
        }
        else
        {
            och = v7 ^ ch;
            v11 = ((21 * v11 * 0xCCCCCCCCCCCCCCCD >> 64) >> 3) ^ och;
        }
        printf("%02x    %02x    \n",ch,och);
        fputc(och,op);
    }
    return 0;
}

int main()
{
    FILE *fp,*op;
    fp=fopen("1.txt","rb");
    op=fopen("3.txt","wb");
    char password[4]="123";
    int mode=0;
    // 'D' &0xdf==0x44 => mode=0
    cipher(fp,op,password,mode);
    fclose(fp);
    fclose(op);

}
