#include "linked_list.h"
#include <stdio.h>
#include <stdlib.h>

LinkList list_create(void)
{
    LinkList L = malloc(sizeof *L);
    if (L != NULL)
        L->next = NULL;
    return L;
}

bool list_empty(LinkList L)
{
    return L->next == NULL;
}

int list_length(LinkList L)
{
    int n = 0;
    for (LNode *p = L->next; p != NULL; p = p->next)
        ++n;
    return n;
}

static LNode *node_at(LinkList L, int pos)
{
    // pos=0 是头结点；插删寻找前驱时使用 pos-1。
    if (pos < 0)
        return NULL;
    LNode *p = L;
    for (int j = 0; p != NULL && j < pos; ++j)
        p = p->next;
    return p;
}

bool list_get(LinkList L, int pos, ElemType *out)
{
    if (pos < 1)
        return false;
    LNode *p = node_at(L, pos);
    if (p == NULL)
        return false;
    *out = p->data;
    return true;
}

int list_find(LinkList L, ElemType value)
{
    int pos = 1;
    for (LNode *p = L->next; p != NULL; p = p->next, ++pos)
        if (p->data == value)
            return pos;
    return 0;
}

bool list_update(LinkList L, int pos, ElemType value)
{
    if (pos < 1)
        return false;
    LNode *p = node_at(L, pos);
    if (p == NULL)
        return false;
    p->data = value;
    return true;
}

bool list_insert(LinkList L, int pos, ElemType value)
{
    if (pos < 1)
        return false;
    LNode *pre = node_at(L, pos - 1);
    if (pre == NULL)
        return false;
    LNode *s = malloc(sizeof *s);
    if (s == NULL)
        return false;
    s->data = value;

    s->next = pre->next; // 先接原后继，再改前驱。
    pre->next = s;
    return true;
}

bool list_delete(LinkList L, int pos, ElemType *out)
{
    if (pos < 1)
        return false;
    LNode *pre = node_at(L, pos - 1);
    if (pre == NULL || pre->next == NULL)
        return false;
    LNode *q = pre->next;
    *out = q->data;
    pre->next = q->next;
    free(q); // q 的数据和后继已在释放前取出。
    return true;
}

void list_print(LinkList L)
{
    printf("[");
    for (LNode *p = L->next; p != NULL; p = p->next) {
        if (p != L->next)
            printf(", ");
        printf("%d", p->data);
    }
    puts("]");
}

void list_clear(LinkList L)
{
    LNode *p = L->next;
    while (p != NULL) {
        LNode *next = p->next; // 保存后继后，才能释放当前结点。
        free(p);
        p = next;
    }
    L->next = NULL;
}

void list_destroy(LinkList L)
{
    list_clear(L);
    free(L);
}
