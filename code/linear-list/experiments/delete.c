// 问题：删除首元结点，为什么仍然只需修改前驱？
#include "../linked_list.h"
#include <assert.h>
#include <stddef.h>
#include <stdio.h>

int main(void)
{
    LNode b = {30, NULL};
    LNode a = {10, &b};
    LNode head = {0, &a};
    LNode *pre = &head;
    LNode *q = pre->next;

    pre->next = q->next;
    assert(head.next == &b && q == &a && q->data == 10);
    puts("删首元：表为[30]，被摘下的a仍然存在");

    q = pre->next;
    pre->next = q->next;
    assert(head.next == NULL);
    puts("再删唯一元素：表为空，头结点保留");
    // a、b 是局部变量，不是 malloc 申请的对象，所以这里不能 free(q)。
    return 0;
}
