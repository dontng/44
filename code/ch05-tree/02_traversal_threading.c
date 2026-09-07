#include <assert.h>
#include <stdlib.h>

/*
 * 本文件把“访问根的时机”与“保存待处理结点的方式”分开观察。
 * 先/中/后序的差别只是根在左右子树之前、中间还是之后访问；
 * 递归版本由系统调用栈保存返回位置，非递归版本把同样的状态显式入栈；
 * 层序遍历改用队列，保证先发现的上层结点先展开。
 */
typedef struct Node {
    char data;
    struct Node *left;
    struct Node *right;
} Node;

static void Put(char out[], int *n, char value) { out[(*n)++] = value; }
static void Preorder(const Node *r, char out[], int *n)
{
    if (r == NULL) return;
    Put(out, n, r->data); /* 根在两棵子树之前访问。 */
    Preorder(r->left, out, n);
    Preorder(r->right, out, n);
}
static void Inorder(const Node *r, char out[], int *n)
{
    if (r == NULL) return;
    Inorder(r->left, out, n);
    Put(out, n, r->data); /* 左子树已经完成，此刻访问根。 */
    Inorder(r->right, out, n);
}
static void Postorder(const Node *r, char out[], int *n)
{
    if (r == NULL) return;
    Postorder(r->left, out, n);
    Postorder(r->right, out, n);
    Put(out, n, r->data); /* 两棵子树都完成后才能访问根。 */
}

static void InorderIterative(Node *root, char out[], int *n)
{
    Node *stack[32];
    int top = 0;
    Node *p = root;
    while (p != NULL || top > 0) {
        /* 沿左链下沉；栈中结点的左子树尚未完成，根也尚未访问。 */
        while (p != NULL) {
            stack[top++] = p;
            p = p->left;
        }
        p = stack[--top]; /* 左边走完，恢复最近一个待访问的根。 */
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
        Node *p = queue[front++]; /* 出队即访问，再把下一层孩子排到队尾。 */
        Put(out, n, p->data);
        if (p->left != NULL) queue[rear++] = p->left;
        if (p->right != NULL) queue[rear++] = p->right;
    }
}

typedef struct ThreadNode {
    char data;
    struct ThreadNode *left;
    struct ThreadNode *right;
    int ltag; /* 0：left 是孩子；1：left 是中序前驱线索。 */
    int rtag; /* 0：right 是孩子；1：right 是中序后继线索。 */
} ThreadNode;

static void InThread(ThreadNode *p, ThreadNode **pre)
{
    if (p == NULL) return;
    /*
     * pre 始终是中序序列中刚访问完的结点。
     * 先递归左子树，回来时 p 与 pre 正好互为当前相邻结点。
     */
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
    /* 有后继线索就直接走；有右孩子则找右子树最左结点。 */
    return p->rtag == 1 ? p->right : First(p->right);
}

int main(void)
{
    /* 同一棵树分别生成四种序列，防止只会背递归模板。 */
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

    /* B-A-C 的中序序列应能在线索化后不借助栈直接走完。 */
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
