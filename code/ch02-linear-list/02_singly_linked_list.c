#include <assert.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

/*
 * 本文件采用“带头结点”的单链表。
 *
 * L 始终指向一个真实存在但不保存有效数据的头结点：
 *     L -> [head] -> [10] -> [20] -> NULL
 * 空表不是 L == NULL，而是 L->next == NULL。
 *
 * 头结点让第一个数据结点也拥有前驱。因此按位插入、删除时，可以统一
 * 寻找“第 i 个位置的前驱”，无需为表头另外写一套改链代码。
 */
typedef int ElemType;

typedef struct LNode {
    ElemType data;          /* 数据域；头结点的 data 不使用。 */
    struct LNode *next;     /* 后继结点地址；NULL 表示链尾。 */
} LNode, *LinkList;

/* 通过二级指针修改调用者手中的头指针。 */
bool LinkInit(LinkList *L)
{
    *L = malloc(sizeof **L);
    if (*L == NULL)
        return false;

    (*L)->next = NULL;
    return true;
}

/* 从首元结点开始计数；头结点不属于表长。 */
int LinkLength(LinkList L)
{
    int length = 0;
    for (LNode *p = L->next; p != NULL; p = p->next)
        ++length;
    return length;
}

/* 找第 i 个数据结点。p 是当前候选，j 是 p 的位序。 */
bool LinkGet(LinkList L, int i, ElemType *e)
{
    if (i < 1)
        return false;

    int j = 1;
    LNode *p = L->next;
    /* 循环结束有两种原因：到达第 i 个结点，或提前走到链尾。 */
    while (p != NULL && j < i) {
        p = p->next;
        ++j;
    }

    if (p == NULL)
        return false;

    *e = p->data;
    return true;
}

/* 顺着 next 找第一个值为 e 的结点；失败自然得到 NULL。 */
LNode *LinkLocate(LinkList L, ElemType e)
{
    LNode *p = L->next;
    while (p != NULL && p->data != e)
        p = p->next;
    return p;
}

/*
 * 在第 i 个位置插入：先找到第 i-1 个结点 p，再把新结点接到 p 后面。
 * p 从头结点、j 从 0 开始，正是为了让 i==1 也落入同一套逻辑。
 */
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
    s->next = p->next; /* 新结点先接住原后继，后半条链仍有入口。 */
    p->next = s;       /* 前驱再改指向新结点，插入完成。 */
    return true;
}

/*
 * 删除第 i 个结点仍先找其前驱 p。q 单独保存待删结点，
 * 因为 p->next 被改写以后，不能再靠 p 找到 q。
 */
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
    p->next = q->next; /* p 越过 q，直接连接 q 的后继。 */
    free(q);
    return true;
}

/* 销毁包含头结点在内的整条链，并把调用者的指针置空。 */
void LinkDestroy(LinkList *L)
{
    LNode *p = *L;
    while (p != NULL) {
        LNode *next = p->next; /* free 前先保存旧后继，否则余链会失去入口。 */
        free(p);
        p = next;
    }
    *L = NULL;
}

int main(void)
{
    LinkList L;
    ElemType e = 777;

    /* 先验证带头结点空表的表示。 */
    assert(LinkInit(&L));
    assert(L != NULL && L->next == NULL);
    assert(LinkLength(L) == 0);
    assert(!LinkGet(L, 1, &e) && e == 777);
    assert(!LinkDelete(L, 1, &e) && e == 777);

    /* 构造 10 -> 20 -> 30，覆盖首位、尾部和中间插入。 */
    assert(LinkInsert(L, 1, 10));
    assert(LinkInsert(L, 2, 30));
    assert(LinkInsert(L, 2, 20));
    assert(LinkLength(L) == 3);

    assert(LinkGet(L, 1, &e) && e == 10);
    assert(LinkGet(L, 2, &e) && e == 20);
    assert(LinkGet(L, 3, &e) && e == 30);
    assert(LinkLocate(L, 30) != NULL);
    assert(LinkLocate(L, 99) == NULL);

    /* 头结点使删除首元结点与普通删除使用同一函数。 */
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
