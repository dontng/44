// 问题：有头结点，为什么仍然可以是空表？
#include "../linked_list.h"
#include <assert.h>
#include <stddef.h>
#include <stdio.h>

int main(void)
{
    LNode head = {0, NULL};
    LinkList L = &head;
    assert(L != NULL && L->next == NULL);
    puts("只有头结点：元素数=0");

    LNode a = {10, NULL};
    head.next = &a;
    assert(L->next == &a && L->next->data == 10);
    puts("接入a：第1个元素=10");

    a.next = L;
    assert(L->next->next == L);
    puts("把链尾接回头结点：成为循环链表，结点类型没变");
    return 0;
}
