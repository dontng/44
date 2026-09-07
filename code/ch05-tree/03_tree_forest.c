#include <assert.h>
#include <stddef.h>

/*
 * 普通树的孩子数不固定，本文件对比两种保存关系的方法：
 *
 * 双亲表示：每个结点只记“我的父亲是谁”，向上查找快；
 * 孩子兄弟表示：first_child 指第一个孩子，next_sibling 串起其他孩子。
 *
 * 孩子兄弟表示仍只有两个指针，因此也能按二叉树方式存储树和森林。
 */
#define MAX_NODES 8
typedef struct {
    char data;
    int parent; /* 双亲在 nodes 数组中的下标；根记为 -1。 */
} ParentNode;
typedef struct {
    ParentNode nodes[MAX_NODES];
    int count;
} ParentTree;

static int ParentOf(const ParentTree *tree, char value)
{
    for (int i = 0; i < tree->count; ++i)
        if (tree->nodes[i].data == value)
            return tree->nodes[i].parent;
    return -2;
}

/* 左指针指向第一个孩子，右指针指向下一个兄弟。 */
typedef struct CSNode {
    char data;
    struct CSNode *first_child;
    struct CSNode *next_sibling;
} CSNode;

static void TreePreorder(const CSNode *root, char out[], int *n)
{
    if (root == NULL) return;
    out[(*n)++] = root->data;
    /* 从第一个孩子开始，沿兄弟链依次递归每棵孩子子树。 */
    for (const CSNode *child = root->first_child; child != NULL;
         child = child->next_sibling)
        TreePreorder(child, out, n);
}

static void TreePostorder(const CSNode *root, char out[], int *n)
{
    if (root == NULL) return;
    for (const CSNode *child = root->first_child; child != NULL;
         child = child->next_sibling)
        TreePostorder(child, out, n);
    out[(*n)++] = root->data; /* 所有孩子完成后才访问父结点。 */
}

/* 森林就是多棵树的根通过 next_sibling 串在一起。 */
static void ForestPreorder(const CSNode *first_root, char out[], int *n)
{
    /* 一片森林的各棵树根，也用 next_sibling 串成同一层。 */
    for (const CSNode *root = first_root; root != NULL; root = root->next_sibling) {
        out[(*n)++] = root->data;
        for (const CSNode *child = root->first_child; child != NULL;
             child = child->next_sibling)
            TreePreorder(child, out, n);
    }
}

int main(void)
{
    /* 双亲数组中 D 的 parent=1，对应 nodes[1] 中的 B。 */
    ParentTree p = {{{'A', -1}, {'B', 0}, {'C', 0}, {'D', 1}}, 4};
    assert(ParentOf(&p, 'D') == 1 && p.nodes[1].data == 'B');

    /* A 的孩子是 B、C，B 的孩子是 D。 */
    CSNode d = {'D', NULL, NULL}, b = {'B', &d, NULL};
    CSNode c = {'C', NULL, NULL}, a = {'A', &b, NULL};
    b.next_sibling = &c;
    char out[8]; int n = 0;
    TreePreorder(&a, out, &n);
    assert(n == 4 && out[0] == 'A' && out[1] == 'B' && out[2] == 'D');
    n = 0; TreePostorder(&a, out, &n);
    assert(out[0] == 'D' && out[3] == 'A');

    CSNode y = {'Y', NULL, NULL}, x = {'X', &y, NULL};
    a.next_sibling = &x;
    n = 0; ForestPreorder(&a, out, &n);
    assert(n == 6 && out[4] == 'X' && out[5] == 'Y');
    return 0;
}
