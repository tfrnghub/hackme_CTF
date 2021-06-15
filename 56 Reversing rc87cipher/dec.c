#include<stdio.h>
#include<string.h>
unsigned char iv[8];
unsigned char sbox[0x100];
char key[41]="FLAG{Known_Plain_Text_Attack_Is_Awesome}";

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

int main()
{
    int i,j;
    unsigned char tmp[0x2000]={0};
    unsigned char _tmp[0x2000]={0};
    unsigned char out[0x2000];
    unsigned int  itmp;
    
    
    int n;
    FILE *fp;
    fp=fopen("flag.enc","rb");
    fread(iv,1,8,fp);
    n=fread(tmp,1,0x2000,fp);
    fclose(fp);
    
    for(i=0;i<0x100;i++)
        sbox[i]=i;
    for(i=0;i<8;i++)
    {
        box_c(i,iv[i],sbox);
    }
    for(i=0;i<n;i++)
    {
        box_c(i%40,key[i%40],sbox);
        itmp=0xDEADBEEF;
        for(j=0;j<0x100;j++)
        {
            itmp=(itmp*0x5a77)^(sbox[j]*0xc8763);
            itmp=itmp&0xffffffff;
        }
        _tmp[i]=itmp&0xff;
    }
    
    
    for(i=0;i<n;i++)
    {
        itmp=tmp[i]^_tmp[i];
        itmp=itmp+0x100-(itmp&0xf)*0x10;
        out[i]=itmp; 
    }
    
    fp=fopen("flag","wb");
    fwrite(out,1,n,fp);
    fclose(fp);
    return 0;
}
