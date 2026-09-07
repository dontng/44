#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

/*
 * 本文件不再重复完整单链表，而是专门展示三种“变体到底多了什么”：
 *
 * 双链表：多维护一条 prior 反向关系；
 * 循环链表：遍历终点从 NULL 改成重新遇到头结点；
 * 静态链表：用数组下标代替真实地址，next 仍然表达逻辑后继。
 *
 * 读变体代码时先找新增的不变量，再看哪些语句专门维护它。
 */
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
    /* 改链顺序按“先接外侧、再接内侧”读，任何旧地址都不能提前丢失。 */
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
    p->next = q->next;             /* 修复正向关系。 */
    if (q->next != NULL)
        q->next->prior = p;        /* 若存在后继，再修复反向关系。 */
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
    /* 从首元结点出发；再次遇到 head 说明完整绕了一圈。 */
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
    SNode node[STATIC_CAP]; /* node[0] 作头结点，其余格子可分配。 */
    int free_head;          /* 备用链第一个空闲格子的下标。 */
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
    int pre = 0; /* 下标 0 对应头结点；沿 next 寻找插入位置的前驱。 */
    for (int j = 1; j < position; ++j) {
        pre = list->node[pre].next;
        if (pre == 0)
            return false;
    }

    /* 先从备用链摘一个格子，再把它接入数据链。 */
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
    /* 双链表：正向和反向关系必须同时通过。 */
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

    /* 循环链表：空表自环，插入后仍能回到头结点。 */
    CNode *c = CInit();
    assert(c != NULL && c->next == c);
    assert(CInsertAfter(c, 2));
    assert(CInsertAfter(c, 1));
    assert(CLength(c) == 2);
    CDestroy(c);

    /* 静态链表：物理下标没有移动，但 next 下标组成了 10,20,30。 */
    StaticList s;
    StaticInit(&s);
    assert(StaticInsert(&s, 1, 10));
    assert(StaticInsert(&s, 2, 30));
    assert(StaticInsert(&s, 2, 20));
    assert(StaticLength(&s) == 3);
    assert(s.node[s.node[0].next].data == 10);
    return 0;
}
