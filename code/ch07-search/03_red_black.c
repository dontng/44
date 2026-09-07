#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

typedef enum { BLACK, RED } Color;
typedef struct RBNode {
    int key;
    Color color;
    struct RBNode *left, *right, *parent;
} RBNode;

static Color ColorOf(const RBNode *p) { return p == NULL ? BLACK : p->color; }

static void RotateLeft(RBNode **root, RBNode *x)
{
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
    while (ColorOf(z->parent) == RED) {
        RBNode *parent = z->parent;
        RBNode *grand = parent->parent;
        if (parent == grand->left) {
            RBNode *uncle = grand->right;
            if (ColorOf(uncle) == RED) {
                parent->color = uncle->color = BLACK;
                grand->color = RED;
                z = grand;                       /* 红冲突向上转移。 */
            } else {
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
    RBNode *parent = NULL, *p = *root;
    while (p != NULL) {
        parent = p;
        if (key == p->key) return;
        p = key < p->key ? p->left : p->right;
    }
    RBNode *z = malloc(sizeof *z);
    if (z == NULL) abort();
    *z = (RBNode){key, RED, NULL, NULL, parent};
    if (parent == NULL) *root = z;
    else if (key < parent->key) parent->left = z;
    else parent->right = z;
    FixAfterInsert(root, z);
}

static int CheckBlackHeight(const RBNode *p)
{
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
    RBNode *root = NULL;
    const int values[] = {10, 20, 30, 15, 5, 1, 7, 25, 40};
    for (int i = 0; i < 9; ++i) Insert(&root, values[i]);
    assert(root != NULL && root->color == BLACK && root->parent == NULL);
    assert(CheckBlackHeight(root) > 0);
    Destroy(root);
    return 0;
}
