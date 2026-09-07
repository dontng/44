#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef int ElemType;

typedef struct LNode {
    ElemType data;
    struct LNode *next;
} LNode, *LinkList;

bool LinkInit(LinkList *L)
{
    *L = malloc(sizeof **L);
    if (*L == NULL)
        return false;

    (*L)->next = NULL;
    return true;
}

int LinkLength(LinkList L)
{
    int length = 0;
    for (LNode *p = L->next; p != NULL; p = p->next)
        ++length;
    return length;
}

bool LinkGet(LinkList L, int i, ElemType *e)
{
    if (i < 1)
        return false;

    int j = 1;
    LNode *p = L->next;
    while (p != NULL && j < i) {
        p = p->next;
        ++j;
    }

    if (p == NULL)
        return false;

    *e = p->data;
    return true;
}

LNode *LinkLocate(LinkList L, ElemType e)
{
    LNode *p = L->next;
    while (p != NULL && p->data != e)
        p = p->next;
    return p;
}

bool LinkInsert(LinkList L, int i, ElemType e)
{
    if (i < 1)
        return false;

    /* 从头结点出发，寻找第 i 个位置的前驱。 */
    int j = 0;
    LNode *p = L;
    while (p != NULL && j < i - 1) {
        p = p->next;
        ++j;
    }
    if (p == NULL)
        return false;

    LNode *s = malloc(sizeof *s);
    if (s == NULL)
        return false;

    s->data = e;
    s->next = p->next; /* 先保存原后继。 */
    p->next = s;       /* 再让前驱接入新结点。 */
    return true;
}

bool LinkDelete(LinkList L, int i, ElemType *e)
{
    if (i < 1)
        return false;

    int j = 0;
    LNode *p = L;
    while (p != NULL && j < i - 1) {
        p = p->next;
        ++j;
    }
    if (p == NULL || p->next == NULL)
        return false;

    LNode *q = p->next;
    *e = q->data;
    p->next = q->next;
    free(q);
    return true;
}

void LinkDestroy(LinkList *L)
{
    LNode *p = *L;
    while (p != NULL) {
        LNode *next = p->next;
        free(p);
        p = next;
    }
    *L = NULL;
}

int main(void)
{
    LinkList L;
    ElemType e = 777;

    assert(LinkInit(&L));
    assert(L != NULL && L->next == NULL);
    assert(LinkLength(L) == 0);
    assert(!LinkGet(L, 1, &e) && e == 777);
    assert(!LinkDelete(L, 1, &e) && e == 777);

    assert(LinkInsert(L, 1, 10));
    assert(LinkInsert(L, 2, 30));
    assert(LinkInsert(L, 2, 20));
    assert(LinkLength(L) == 3);

    assert(LinkGet(L, 1, &e) && e == 10);
    assert(LinkGet(L, 2, &e) && e == 20);
    assert(LinkGet(L, 3, &e) && e == 30);
    assert(LinkLocate(L, 30) != NULL);
    assert(LinkLocate(L, 99) == NULL);

    assert(LinkDelete(L, 1, &e) && e == 10);
    assert(LinkDelete(L, 2, &e) && e == 30);
    assert(LinkLength(L) == 1);
    assert(LinkGet(L, 1, &e) && e == 20);
    assert(!LinkInsert(L, 3, 40));

    LinkDestroy(&L);
    assert(L == NULL);

    puts("PASS: singly linked list");
    return 0;
}
