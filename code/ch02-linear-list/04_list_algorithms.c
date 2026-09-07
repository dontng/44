#include <assert.h>
#include <stdlib.h>

/*
 * 本文件只保留两种 408 高频链表动作：原地逆置、有序归并。
 * 两个算法都不新建数据结点，改变的是旧结点之间的 next 关系。
 *
 * 逆置要同时维护“已反转部分”和“未处理部分”；
 * 归并要同时维护“两条未处理输入链”和“结果链尾”。
 */
typedef struct Node {
    int data;
    struct Node *next;
} Node;

static Node *Build(const int values[], int n)
{
    Node *head = malloc(sizeof *head);
    if (head == NULL)
        return NULL;
    head->next = NULL;
    Node *tail = head; /* tail 永远指向当前链尾，尾插无需重复遍历。 */
    for (int i = 0; i < n; ++i) {
        Node *s = malloc(sizeof *s);
        if (s == NULL)
            abort();
        s->data = values[i];
        s->next = NULL;
        tail->next = s;
        tail = s;
    }
    return head;
}

/* 不变量：pre 是已反转链的表头，p 是尚未处理部分的表头。 */
static void Reverse(Node *head)
{
    Node *pre = NULL;
    Node *p = head->next;
    while (p != NULL) {
        Node *next = p->next; /* 1. 改箭头前保留未处理余链入口。 */
        p->next = pre;        /* 2. 当前结点并入已反转链。 */
        pre = p;              /* 3. 已反转链表头前移。 */
        p = next;             /* 4. 回到旧路，处理下一个结点。 */
    }
    head->next = pre;
}

/* 复用原结点归并；tail 始终指向结果链最后一个结点。 */
static Node *MergeSorted(Node *a, Node *b)
{
    Node *pa = a->next;
    Node *pb = b->next;
    Node *tail = a;
    /*
     * 循环开始时：a 的头结点后面已经接好结果，tail 指向结果末尾；
     * pa、pb 分别指向两条链中尚未处理的最小结点。
     */
    while (pa != NULL && pb != NULL) {
        if (pa->data <= pb->data) {
            tail->next = pa;
            pa = pa->next;
        } else {
            tail->next = pb;
            pb = pb->next;
        }
        tail = tail->next; /* 本轮只接走一个结点，所以只前进一步。 */
    }
    /* 一条链耗尽后，另一条余链本来就有序，可以整体接上。 */
    tail->next = pa != NULL ? pa : pb;
    free(b);
    return a;
}

static void Destroy(Node *head)
{
    while (head != NULL) {
        Node *next = head->next;
        free(head);
        head = next;
    }
}

int main(void)
{
    const int x[] = {1, 3, 5};
    const int y[] = {2, 4, 6};
    Node *a = Build(x, 3);
    Node *b = Build(y, 3);
    assert(a != NULL && b != NULL);
    /* 先验证升序归并，再在同一批结点上验证原地逆置。 */
    Node *m = MergeSorted(a, b);
    int expected = 1;
    for (Node *p = m->next; p != NULL; p = p->next)
        assert(p->data == expected++);
    Reverse(m);
    expected = 6;
    for (Node *p = m->next; p != NULL; p = p->next)
        assert(p->data == expected--);
    Destroy(m);
    return 0;
}
