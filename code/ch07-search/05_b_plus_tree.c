#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX_KEYS 3
typedef struct BPNode {
    bool leaf;
    int n;
    int key[MAX_KEYS + 1];       /* 多留一格承接分裂前的临时溢出。 */
    struct BPNode *child[MAX_KEYS + 2];
    struct BPNode *next;         /* 只有叶结点使用，支持顺序/范围查找。 */
} BPNode;
typedef struct { bool split; int separator; BPNode *right; } Split;

static BPNode *NewNode(bool leaf)
{
    BPNode *p = calloc(1, sizeof *p);
    if (p == NULL) abort();
    p->leaf = leaf;
    return p;
}

static Split InsertRec(BPNode *p, int key)
{
    if (p->leaf) {
        int pos = 0;
        while (pos < p->n && p->key[pos] < key) ++pos;
        if (pos < p->n && p->key[pos] == key) return (Split){0};
        for (int i = p->n; i > pos; --i) p->key[i] = p->key[i - 1];
        p->key[pos] = key;
        if (++p->n <= MAX_KEYS) return (Split){0};
        BPNode *right = NewNode(true);
        int left_count = p->n / 2;
        right->n = p->n - left_count;
        for (int i = 0; i < right->n; ++i) right->key[i] = p->key[left_count + i];
        p->n = left_count;
        right->next = p->next;
        p->next = right;
        return (Split){true, right->key[0], right};
    }

    int pos = 0;
    while (pos < p->n && key >= p->key[pos]) ++pos;
    Split child_split = InsertRec(p->child[pos], key);
    if (!child_split.split) return child_split;
    for (int i = p->n; i > pos; --i) p->key[i] = p->key[i - 1];
    for (int i = p->n + 1; i > pos + 1; --i) p->child[i] = p->child[i - 1];
    p->key[pos] = child_split.separator;
    p->child[pos + 1] = child_split.right;
    if (++p->n <= MAX_KEYS) return (Split){0};

    BPNode *right = NewNode(false);
    int middle = p->n / 2;
    int separator = p->key[middle];
    right->n = p->n - middle - 1;
    for (int i = 0; i < right->n; ++i) right->key[i] = p->key[middle + 1 + i];
    for (int i = 0; i <= right->n; ++i) right->child[i] = p->child[middle + 1 + i];
    p->n = middle;
    return (Split){true, separator, right};
}

static void Insert(BPNode **root, int key)
{
    Split split = InsertRec(*root, key);
    if (!split.split) return;
    BPNode *new_root = NewNode(false);
    new_root->n = 1;
    new_root->key[0] = split.separator;
    new_root->child[0] = *root;
    new_root->child[1] = split.right;
    *root = new_root;
}

static BPNode *FindLeaf(BPNode *p, int key)
{
    while (!p->leaf) {
        int i = 0;
        while (i < p->n && key >= p->key[i]) ++i;
        p = p->child[i];
    }
    return p;
}
static bool Search(BPNode *root, int key)
{
    BPNode *leaf = FindLeaf(root, key);
    for (int i = 0; i < leaf->n; ++i)
        if (leaf->key[i] == key) return true;
    return false;
}
static int Range(BPNode *root, int low, int high, int out[], int cap)
{
    BPNode *leaf = FindLeaf(root, low);
    int n = 0;
    for (; leaf != NULL; leaf = leaf->next) {
        for (int i = 0; i < leaf->n; ++i) {
            if (leaf->key[i] > high) return n;
            if (leaf->key[i] >= low && n < cap) out[n++] = leaf->key[i];
        }
    }
    return n;
}
static void Destroy(BPNode *p)
{
    if (!p->leaf)
        for (int i = 0; i <= p->n; ++i) Destroy(p->child[i]);
    free(p);
}

int main(void)
{
    BPNode *root = NewNode(true);
    const int values[] = {10, 20, 5, 6, 12, 30, 7, 17, 3, 4, 2,
                          1, 8, 9, 11, 13, 14, 15, 16, 18, 19};
    for (int i = 0; i < 21; ++i) Insert(&root, values[i]);
    for (int key = 1; key <= 20; ++key) assert(Search(root, key));
    assert(!Search(root, 21));
    int out[24];
    int n = Range(root, 4, 9, out, 8);
    assert(n == 6);
    for (int i = 0; i < n; ++i) assert(out[i] == i + 4);
    Destroy(root);
    return 0;
}
