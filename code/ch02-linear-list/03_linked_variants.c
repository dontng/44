#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct DNode {
    int data;
    struct DNode *prior;
    struct DNode *next;
} DNode;

/* 双链表的新增约束：p->next == q 时，q->prior 也必须等于 p。 */
static DNode *DInit(void)
{
    DNode *head = malloc(sizeof *head);
    if (head != NULL) {
        head->prior = NULL;
        head->next = NULL;
    }
    return head;
}

static bool DInsertAfter(DNode *p, int value)
{
    DNode *s = malloc(sizeof *s);
    if (s == NULL)
        return false;
    s->data = value;
    s->next = p->next;               /* 先接住原后继。 */
    if (p->next != NULL)
        p->next->prior = s;          /* 原后继改认新前驱。 */
    s->prior = p;
    p->next = s;
    return true;
}

static bool DDeleteAfter(DNode *p, int *value)
{
    DNode *q = p->next;
    if (q == NULL)
        return false;
    *value = q->data;
    p->next = q->next;
    if (q->next != NULL)
        q->next->prior = p;
    free(q);
    return true;
}

static void DDestroy(DNode *head)
{
    while (head != NULL) {
        DNode *next = head->next;
        free(head);
        head = next;
    }
}

typedef struct CNode {
    int data;
    struct CNode *next;
} CNode;

/* 带头结点循环链表：空表和遍历终点都是 head，而不是 NULL。 */
static CNode *CInit(void)
{
    CNode *head = malloc(sizeof *head);
    if (head != NULL)
        head->next = head;
    return head;
}

static bool CInsertAfter(CNode *p, int value)
{
    CNode *s = malloc(sizeof *s);
    if (s == NULL)
        return false;
    s->data = value;
    s->next = p->next;
    p->next = s;
    return true;
}

static int CLength(const CNode *head)
{
    int n = 0;
    for (const CNode *p = head->next; p != head; p = p->next)
        ++n;
    return n;
}

static void CDestroy(CNode *head)
{
    CNode *p = head->next;
    while (p != head) {
        CNode *next = p->next;
        free(p);
        p = next;
    }
    free(head);
}

#define STATIC_CAP 8
typedef struct {
    int data;
    int next;
} SNode;

typedef struct {
    SNode node[STATIC_CAP];
    int free_head;
} StaticList;

/* node[0] 是头结点；0 同时充当空下标。其余格子先串成备用链。 */
static void StaticInit(StaticList *list)
{
    list->node[0].next = 0;
    list->free_head = 1;
    for (int i = 1; i < STATIC_CAP - 1; ++i)
        list->node[i].next = i + 1;
    list->node[STATIC_CAP - 1].next = 0;
}

static bool StaticInsert(StaticList *list, int position, int value)
{
    if (position < 1 || list->free_head == 0)
        return false;
    int pre = 0;
    for (int j = 1; j < position; ++j) {
        pre = list->node[pre].next;
        if (pre == 0)
            return false;
    }

    int fresh = list->free_head;
    list->free_head = list->node[fresh].next;
    list->node[fresh].data = value;
    list->node[fresh].next = list->node[pre].next;
    list->node[pre].next = fresh;
    return true;
}

static int StaticLength(const StaticList *list)
{
    int n = 0;
    for (int i = list->node[0].next; i != 0; i = list->node[i].next)
        ++n;
    return n;
}

int main(void)
{
    DNode *d = DInit();
    assert(d != NULL);
    assert(DInsertAfter(d, 10));
    assert(DInsertAfter(d->next, 30));
    assert(DInsertAfter(d->next, 20));
    assert(d->next->data == 10 && d->next->next->data == 20);
    assert(d->next->next->prior == d->next);
    int removed = 0;
    assert(DDeleteAfter(d->next, &removed) && removed == 20);
    DDestroy(d);

    CNode *c = CInit();
    assert(c != NULL && c->next == c);
    assert(CInsertAfter(c, 2));
    assert(CInsertAfter(c, 1));
    assert(CLength(c) == 2);
    CDestroy(c);

    StaticList s;
    StaticInit(&s);
    assert(StaticInsert(&s, 1, 10));
    assert(StaticInsert(&s, 2, 30));
    assert(StaticInsert(&s, 2, 20));
    assert(StaticLength(&s) == 3);
    assert(s.node[s.node[0].next].data == 10);
    return 0;
}
