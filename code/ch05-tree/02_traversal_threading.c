#include <assert.h>
#include <stdlib.h>

typedef struct Node {
    char data;
    struct Node *left;
    struct Node *right;
} Node;

static void Put(char out[], int *n, char value) { out[(*n)++] = value; }
static void Preorder(const Node *r, char out[], int *n)
{
    if (r == NULL) return;
    Put(out, n, r->data);
    Preorder(r->left, out, n);
    Preorder(r->right, out, n);
}
static void Inorder(const Node *r, char out[], int *n)
{
    if (r == NULL) return;
    Inorder(r->left, out, n);
    Put(out, n, r->data);
    Inorder(r->right, out, n);
}
static void Postorder(const Node *r, char out[], int *n)
{
    if (r == NULL) return;
    Postorder(r->left, out, n);
    Postorder(r->right, out, n);
    Put(out, n, r->data);
}

static void InorderIterative(Node *root, char out[], int *n)
{
    Node *stack[32];
    int top = 0;
    Node *p = root;
    while (p != NULL || top > 0) {
        while (p != NULL) {
            stack[top++] = p;
            p = p->left;
        }
        p = stack[--top];
        Put(out, n, p->data);
        p = p->right;
    }
}

static void Levelorder(Node *root, char out[], int *n)
{
    if (root == NULL) return;
    Node *queue[32];
    int front = 0, rear = 0;
    queue[rear++] = root;
    while (front < rear) {
        Node *p = queue[front++];
        Put(out, n, p->data);
        if (p->left != NULL) queue[rear++] = p->left;
        if (p->right != NULL) queue[rear++] = p->right;
    }
}

typedef struct ThreadNode {
    char data;
    struct ThreadNode *left;
    struct ThreadNode *right;
    int ltag; /* 0: child，1: thread。 */
    int rtag;
} ThreadNode;

static void InThread(ThreadNode *p, ThreadNode **pre)
{
    if (p == NULL) return;
    InThread(p->left, pre);
    if (p->left == NULL) {
        p->ltag = 1;
        p->left = *pre;             /* 空左链域改存中序前驱。 */
    }
    if (*pre != NULL && (*pre)->right == NULL) {
        (*pre)->rtag = 1;
        (*pre)->right = p;          /* 前驱的空右链域改存中序后继。 */
    }
    *pre = p;
    InThread(p->right, pre);
}

static ThreadNode *First(ThreadNode *p)
{
    while (p != NULL && p->ltag == 0)
        p = p->left;
    return p;
}
static ThreadNode *Next(ThreadNode *p)
{
    return p->rtag == 1 ? p->right : First(p->right);
}

int main(void)
{
    Node d = {'D', NULL, NULL}, e = {'E', NULL, NULL};
    Node b = {'B', &d, &e}, c = {'C', NULL, NULL}, a = {'A', &b, &c};
    char out[8];
    int n = 0;
    Preorder(&a, out, &n);
    assert(n == 5 && out[0] == 'A' && out[4] == 'C');
    n = 0; Inorder(&a, out, &n);
    assert(out[0] == 'D' && out[2] == 'E');
    n = 0; Postorder(&a, out, &n);
    assert(out[4] == 'A');
    n = 0; InorderIterative(&a, out, &n);
    assert(out[0] == 'D' && out[4] == 'C');
    n = 0; Levelorder(&a, out, &n);
    assert(out[0] == 'A' && out[1] == 'B' && out[2] == 'C');

    ThreadNode t1 = {'B', NULL, NULL, 0, 0};
    ThreadNode t3 = {'C', NULL, NULL, 0, 0};
    ThreadNode t2 = {'A', &t1, &t3, 0, 0};
    ThreadNode *pre = NULL;
    InThread(&t2, &pre);
    if (pre != NULL) pre->rtag = 1;
    char threaded[3]; n = 0;
    for (ThreadNode *p = First(&t2); p != NULL; p = Next(p))
        threaded[n++] = p->data;
    assert(n == 3 && threaded[0] == 'B' && threaded[1] == 'A' && threaded[2] == 'C');
    return 0;
}
