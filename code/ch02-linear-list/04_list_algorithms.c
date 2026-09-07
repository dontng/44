#include <assert.h>
#include <stdlib.h>

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
    Node *tail = head;
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
        Node *next = p->next; /* 改箭头前保留旧路。 */
        p->next = pre;
        pre = p;
        p = next;
    }
    head->next = pre;
}

/* 复用原结点归并；tail 始终指向结果链最后一个结点。 */
static Node *MergeSorted(Node *a, Node *b)
{
    Node *pa = a->next;
    Node *pb = b->next;
    Node *tail = a;
    while (pa != NULL && pb != NULL) {
        if (pa->data <= pb->data) {
            tail->next = pa;
            pa = pa->next;
        } else {
            tail->next = pb;
            pb = pb->next;
        }
        tail = tail->next;
    }
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
