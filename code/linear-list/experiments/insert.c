// 问题：插入的两句代码交换顺序，会发生什么？
#include "../linked_list.h"
#include <stddef.h>
#include <stdio.h>

int main(void)
{
    LNode tail = {30, NULL};
    LNode pre = {10, &tail};
    LNode s = {20, NULL};

#ifdef WRONG_ORDER
    pre.next = &s;
    s.next = pre.next;
#else
    s.next = pre.next;
    pre.next = &s;
#endif

    // 只检查地址关系，不遍历可能形成的环；错误版本也能安全观察。
    printf("前驱接到s：%d\n", pre.next == &s);
    printf("s接到原后继：%d\n", s.next == &tail);
    printf("s接到自身：%d\n", s.next == &s);
    if (pre.next != &s || s.next != &tail) {
        puts("FAIL：插入没有保住原后继");
        return 1;
    }
    puts("PASS：次序为10, 20, 30");
    return 0;
}
