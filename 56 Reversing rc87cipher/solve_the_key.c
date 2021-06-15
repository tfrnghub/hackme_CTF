#include<stdio.h>
#include<string.h>
unsigned char iv[8];
unsigned char ctmp[100];


void box_c(unsigned int a,unsigned int b,unsigned char _sbox[0x100])
{
    int i;
    int tmp;
    for(i=0;i<0x24;i++)
    {
        a=((0xff-a)*13)&0xff;
        b=((0xff-b)*17)&0xff;
        tmp=_sbox[a];
        _sbox[a]=_sbox[b];
        _sbox[b]=tmp;
        
    }
}
void run(unsigned char _key[20],int _len)
{
    int i,j;
    unsigned int itmp;
    unsigned char sbox[0x100];
    for(i=0;i<0x100;i++)
        sbox[i]=i;
    for(i=0;i<8;i++)
    {
        box_c(i,iv[i],sbox);
    }
    for(i=0;i<_len;i++)
    {
        box_c(i,_key[i],sbox);
    }
    
    unsigned int  t_key;
    unsigned char t_sbox[0x100];
    for(t_key=0x21;t_key<0x7f;t_key++)
    {
        memcpy(t_sbox,sbox,0x100);
        box_c(i,t_key,t_sbox);
        itmp=0xDEADBEEF;
        for(j=0;j<0x100;j++)
        {
            itmp=(itmp*0x5a77)^(t_sbox[j]*0xc8763);
            itmp=itmp&0xffffffff;
        }
        itmp=itmp&0xff;
        if(itmp==ctmp[i])
        { 
            _key[_len]=t_key;
            if((t_key=='}')&&(_len+1==40))
            {
                for(j=0;j<_len+1;j++)
                    printf("%c",_key[j]);
                printf("\n"); 
            }
            if(_len<40)
                run(_key,_len+1);
        }     
    }
    
}
int main()
{
    int i;
    unsigned char key[45]={0};
    FILE *fp,*op;
    fp=fopen("rc87.enc","rb");
    op=fopen("rc87","rb");
    fread(iv,1,8,fp);
    for(i=0;i<100;i++)
        ctmp[i]=((fgetc(op)*0x11)&0xff)^fgetc(fp);
    fclose(fp);
    fclose(op);
    run(key,0);
    return 0;
}
