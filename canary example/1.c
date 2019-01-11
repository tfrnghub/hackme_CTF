/**
* compile cmd: gcc 1.c -m32 -fstack-protector-all -no-pie -o bin
**/
#include <stdio.h>
#include <unistd.h>

void getflag(void) {
    char flag[100];
    FILE *fp = fopen("./flag", "r");
    if (fp == NULL) {
        puts("get flag error");
    }
    fgets(flag, 100, fp);
    puts(flag);
}
void init() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void fun(void) {
	char buffer[100];
	read(STDIN_FILENO, buffer, 120);
}

int main(void) {
	char buffer[6];
	init();
	scanf("%6s",buffer);
	printf(buffer);
	fun();
}
