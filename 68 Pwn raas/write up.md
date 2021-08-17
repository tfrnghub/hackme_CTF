- ### hackme: Pwn-raas
```
struct record {
    void (*print)(struct record *);
    void (*free)(struct record *);
    union {
        int integer;
        char *string;
    };
};
void do_new()
{
    ...
    struct record *r = records[idx] = (struct record *)malloc(sizeof(struct record));
    r->print = rec_int_print;
    r->free = rec_int_free;
    ...
    switch(type) {
        case 1:
            r->integer = ask("Value");
            break;
        case 2:
            len = ask("Length");
            if(len > 1024) {
	            puts("Length too long, please buy record service premium to store longer record!");
	            return;
            }
            r->string = malloc(len);
            printf("Value > ");
            fgets(r->string, len, stdin);
            r->print = rec_str_print;
            r->free = rec_str_free;
```
```
record的大小为12字节；
record分为integer和string两种类型；
如果type是integer，最后四个字节存输入的整数；
如果type是string，获取长度，malloc一个指定长度的堆，最后四个字节存malloc指针。
```
use after free，利用思路：
```
new 两个record，delete掉，这里的record类型随意，但是字符的要注意新new的长度不要等于12；
new一个字符串类型的record，长度为12，假设new的两个record是0、1，删除的顺序是0、1，那么这个时候在fastbin的链表里面是 1->0 ，new一个record，存函数指针那个堆复用了1的堆，用来存内容的那个堆是用了0的堆；
往0那个堆里面写我们想要的东西，再删除0的record，这样就能getshell。
```
