#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

/*
 * 本文件实现 4 阶 B 树（2-3-4 树）的查找与插入。
 *
 * 一个结点最多 3 个关键字、4 个孩子；结点内关键字递增。
 * key[i] 左边的 child[i] 保存更小区间，右边的 child[i+1] 保存更大区间。
 * B 树通过“一个磁盘结点容纳多个关键字”降低树高，代码难点在结点分裂。
 */
#define T 2
#define MAX_KEYS (2 * T - 1)
typedef struct BNode {
    int n;                         /* 当前实际关键字个数。 */
    bool leaf;                     /* 叶结点没有有效 child。 */
    int key[MAX_KEYS];             /* 只使用 key[0..n-1]。 */
    struct BNode *child[2 * T];    /* 非叶结点使用 child[0..n]。 */
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
    /* 先在当前结点内找到第一个 >= key 的位置 i。 */
    int i = 0;
    while (i < p->n && key > p->key[i]) ++i;
    if (i < p->n && key == p->key[i]) return p;
    return p->leaf ? NULL : Search(p->child[i], key); /* 未命中则只进入一个区间。 */
}

static void SplitChild(BNode *parent, int pos)
{
    /*
     * parent->child[pos] 已满：
     * [k0 k1 k2] -> 左边保留 [k0]，k1 上升到 parent，右边新建 [k2]。
     * 必须先为 parent 的孩子和关键字腾位，再写入新关系。
     */
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
        /* 叶结点尚未满：较大关键字右移，给 key 腾出有序位置。 */
        while (i >= 0 && key < p->key[i]) {
            p->key[i + 1] = p->key[i];
            --i;
        }
        if (i >= 0 && p->key[i] == key) return;
        p->key[i + 1] = key;
        ++p->n;
    } else {
        /* 在当前结点确定下降区间；若目标孩子已满，下降前先分裂。 */
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
        /* 根满时只能新建更高一层；这是 B 树高度增加的唯一位置。 */
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
    /* 插入序列会让叶结点和根先后分裂，并检查命中与失败路径。 */
    BNode *root = NewNode(true);
    const int values[] = {10, 20, 5, 6, 12, 30, 7, 17};
    for (int i = 0; i < 8; ++i) Insert(&root, values[i]);
    assert(!root->leaf && root->n == 2);
    assert(Search(root, 6) != NULL && Search(root, 99) == NULL);
    Destroy(root);
    return 0;
}
