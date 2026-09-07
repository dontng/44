// 问题：p = p->next 和 p->next = ...，谁改变了链表？
#include "../linked_list.h"
#include <assert.h>
#include <stddef.h>
#include <stdio.h>

int main(void)
{
    LNode b = {30, NULL};
    LNode a = {10, &b};
    LNode head = {0, &a};
    LNode *p = &a;

    p = p->next;
    assert(p == &b && head.next == &a && a.next == &b);
    puts("移动p：p看到30，表仍为[10, 30]");

    p = &head;
    p->next = p->next->next;
    assert(head.next == &b && a.data == 10);
    puts("修改连接：从表头只能读到[30]，a本身仍存在");
    return 0;
}
