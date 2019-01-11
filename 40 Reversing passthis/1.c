/*
00002040h: C1 CB C6 C0 FC C9 E8 AB A7 DE E8 F2 A7 F4 EF E8 ; ÁËÆÀüÉè«§Þèò§ôïè
00002050h: F2 EB E3 A7 E9 E8 F3 A7 F7 E6 F4 F4 A7 F3 EF E2 ; òëã§éèó§÷æôô§óïâ
00002060h: A7 E1 EB E6 E0 FA 00                            ; §áëæàú.
*/
#include <stdio.h>
#include <string.h>
int main()
{
    char s[39]="\xC1\xCB\xC6\xC0\xFC\xC9\xE8\xAB\xA7\xDE\xE8\xF2\xA7\xF4\xEF\xE8\xF2\xEB\xE3\xA7\xE9\xE8\xF3\xA7\xF7\xE6\xF4\xF4\xA7\xF3\xEF\xE2\xA7\xE1\xEB\xE6\xE0\xFA";
    char r[39]={0};
    int i;
    for(i=0;i<38;i++)
        r[i]=s[i]^0x87;
    puts(r);
    return 0;
}
