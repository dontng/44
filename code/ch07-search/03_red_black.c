#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

/*
 * 红黑树先是一棵 BST，再用颜色限制任意根到空叶路径的长度：
 * 1. 根为黑；NULL 视为黑叶；
 * 2. 红结点不能有红孩子；
 * 3. 从任一结点到各 NULL 叶的黑结点数相同。
 *
 * 新结点先按 BST 插入并染红：这样不会立刻改变黑高，只可能产生“红父红子”。
 * 修复循环只围绕新结点、父亲、叔叔和祖父四个角色判断。
 */
typedef enum { BLACK, RED } Color;
typedef struct RBNode {
    int key;
    Color color; /* 颜色用于平衡，不参与 BST 大小关系。 */
    struct RBNode *left, *right, *parent; /* parent 让修复可以向祖父回溯。 */
} RBNode;

static Color ColorOf(const RBNode *p) { return p == NULL ? BLACK : p->color; }

static void RotateLeft(RBNode **root, RBNode *x)
{
    /* x 的右孩子 y 上升。中间子树 y->left 改接到 x->right。 */
    RBNode *y = x->right;
    x->right = y->left;
    if (y->left != NULL) y->left->parent = x;
    y->parent = x->parent;
    if (x->parent == NULL) *root = y;
    else if (x == x->parent->left) x->parent->left = y;
    else x->parent->right = y;
    y->left = x;
    x->parent = y;
}
static void RotateRight(RBNode **root, RBNode *y)
{
    /* 左旋的镜像；四处 parent 关系也必须随父子变化一同更新。 */
    RBNode *x = y->left;
    y->left = x->right;
    if (x->right != NULL) x->right->parent = y;
    x->parent = y->parent;
    if (y->parent == NULL) *root = x;
    else if (y == y->parent->left) y->parent->left = x;
    else y->parent->right = x;
    x->right = y;
    y->parent = x;
}

static void FixAfterInsert(RBNode **root, RBNode *z)
{
    /* 只有父亲为红才违规；父亲为黑时插入已经结束。 */
    while (ColorOf(z->parent) == RED) {
        RBNode *parent = z->parent;
        RBNode *grand = parent->parent;
        if (parent == grand->left) {
            RBNode *uncle = grand->right;
            if (ColorOf(uncle) == RED) {
                /* 父、叔同红：不旋转，只重新着色并把冲突上推到祖父。 */
                parent->color = uncle->color = BLACK;
                grand->color = RED;
                z = grand;                       /* 红冲突向上转移。 */
            } else {
                /* 叔叔为黑：折线先旋成直线，再旋祖父并交换父祖颜色。 */
                if (z == parent->right) {
                    z = parent;
                    RotateLeft(root, z);          /* LR 先转成 LL。 */
                    parent = z->parent;
                    grand = parent->parent;
                }
                parent->color = BLACK;
                grand->color = RED;
                RotateRight(root, grand);
            }
        } else {
            /* 父亲在祖父右侧，下面逻辑与左侧情况完全镜像。 */
            RBNode *uncle = grand->left;
            if (ColorOf(uncle) == RED) {
                parent->color = uncle->color = BLACK;
                grand->color = RED;
                z = grand;
            } else {
                if (z == parent->left) {
                    z = parent;
                    RotateRight(root, z);
                    parent = z->parent;
                    grand = parent->parent;
                }
                parent->color = BLACK;
                grand->color = RED;
                RotateLeft(root, grand);
            }
        }
    }
    (*root)->color = BLACK;
}

static void Insert(RBNode **root, int key)
{
    /* parent 保留 NULL 插入位置的父结点，p 负责沿 BST 向下寻找。 */
    RBNode *parent = NULL, *p = *root;
    while (p != NULL) {
        parent = p;
        if (key == p->key) return;
        p = key < p->key ? p->left : p->right;
    }
    RBNode *z = malloc(sizeof *z);
    if (z == NULL) abort();
    *z = (RBNode){key, RED, NULL, NULL, parent}; /* 新结点染红，黑高暂不改变。 */
    if (parent == NULL) *root = z;
    else if (key < parent->key) parent->left = z;
    else parent->right = z;
    FixAfterInsert(root, z);
}

static int CheckBlackHeight(const RBNode *p)
{
    /* 这个验证函数直接把红黑树定义变成可执行断言。 */
    if (p == NULL) return 1;
    if (p->color == RED)
        assert(ColorOf(p->left) == BLACK && ColorOf(p->right) == BLACK);
    int left = CheckBlackHeight(p->left), right = CheckBlackHeight(p->right);
    assert(left == right);
    return left + (p->color == BLACK);
}
static void Destroy(RBNode *p)
{
    if (p == NULL) return;
    Destroy(p->left); Destroy(p->right); free(p);
}

int main(void)
{
    /* 该序列同时触发直线、折线、叔叔为红和左右镜像情况。 */
    RBNode *root = NULL;
    const int values[] = {10, 20, 30, 15, 5, 1, 7, 25, 40};
    for (int i = 0; i < 9; ++i) Insert(&root, values[i]);
    assert(root != NULL && root->color == BLACK && root->parent == NULL);
    assert(CheckBlackHeight(root) > 0);
    Destroy(root);
    return 0;
}
