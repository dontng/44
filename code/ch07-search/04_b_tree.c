#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

/* 4 阶 B 树（2-3-4 树）：至多 4 个孩子、3 个关键字。 */
#define T 2
#define MAX_KEYS (2 * T - 1)
typedef struct BNode {
    int n;
    bool leaf;
    int key[MAX_KEYS];
    struct BNode *child[2 * T];
} BNode;

static BNode *NewNode(bool leaf)
{
    BNode *p = calloc(1, sizeof *p);
    if (p == NULL) abort();
    p->leaf = leaf;
    return p;
}

static BNode *Search(BNode *p, int key)
{
    int i = 0;
    while (i < p->n && key > p->key[i]) ++i;
    if (i < p->n && key == p->key[i]) return p;
    return p->leaf ? NULL : Search(p->child[i], key);
}

static void SplitChild(BNode *parent, int pos)
{
    BNode *full = parent->child[pos];
    BNode *right = NewNode(full->leaf);
    right->n = T - 1;
    for (int j = 0; j < T - 1; ++j) right->key[j] = full->key[j + T];
    if (!full->leaf)
        for (int j = 0; j < T; ++j) right->child[j] = full->child[j + T];
    full->n = T - 1;
    for (int j = parent->n; j > pos; --j) parent->child[j + 1] = parent->child[j];
    parent->child[pos + 1] = right;
    for (int j = parent->n - 1; j >= pos; --j) parent->key[j + 1] = parent->key[j];
    parent->key[pos] = full->key[T - 1]; /* 中间关键字上升，左右各留一半。 */
    ++parent->n;
}

static void InsertNonFull(BNode *p, int key)
{
    int i = p->n - 1;
    if (p->leaf) {
        while (i >= 0 && key < p->key[i]) {
            p->key[i + 1] = p->key[i];
            --i;
        }
        if (i >= 0 && p->key[i] == key) return;
        p->key[i + 1] = key;
        ++p->n;
    } else {
        while (i >= 0 && key < p->key[i]) --i;
        ++i;
        if (p->child[i]->n == MAX_KEYS) {
            SplitChild(p, i);
            if (key > p->key[i]) ++i;
            else if (key == p->key[i]) return;
        }
        InsertNonFull(p->child[i], key);
    }
}

static void Insert(BNode **root, int key)
{
    if (Search(*root, key) != NULL) return;
    if ((*root)->n == MAX_KEYS) {
        BNode *new_root = NewNode(false);
        new_root->child[0] = *root;
        SplitChild(new_root, 0);
        *root = new_root;
    }
    InsertNonFull(*root, key);
}

static void Destroy(BNode *p)
{
    if (!p->leaf)
        for (int i = 0; i <= p->n; ++i) Destroy(p->child[i]);
    free(p);
}

int main(void)
{
    BNode *root = NewNode(true);
    const int values[] = {10, 20, 5, 6, 12, 30, 7, 17};
    for (int i = 0; i < 8; ++i) Insert(&root, values[i]);
    assert(!root->leaf && root->n == 2);
    assert(Search(root, 6) != NULL && Search(root, 99) == NULL);
    Destroy(root);
    return 0;
}
