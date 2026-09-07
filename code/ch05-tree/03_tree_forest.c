#include <assert.h>
#include <stddef.h>

#define MAX_NODES 8
typedef struct {
    char data;
    int parent; /* 根的双亲记为 -1。 */
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
    out[(*n)++] = root->data;
}

/* 森林就是多棵树的根通过 next_sibling 串在一起。 */
static void ForestPreorder(const CSNode *first_root, char out[], int *n)
{
    for (const CSNode *root = first_root; root != NULL; root = root->next_sibling) {
        out[(*n)++] = root->data;
        for (const CSNode *child = root->first_child; child != NULL;
             child = child->next_sibling)
            TreePreorder(child, out, n);
    }
}

int main(void)
{
    ParentTree p = {{{'A', -1}, {'B', 0}, {'C', 0}, {'D', 1}}, 4};
    assert(ParentOf(&p, 'D') == 1 && p.nodes[1].data == 'B');

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
