#include <assert.h>
#include <limits.h>

#define HUFF_MAX 15
typedef struct {
    int weight;
    int parent;
    int left;
    int right;
} HuffNode;

static void SelectTwo(const HuffNode tree[], int end, int *a, int *b)
{
    *a = *b = -1;
    for (int i = 0; i < end; ++i) {
        if (tree[i].parent != -1) continue;
        if (*a == -1 || tree[i].weight < tree[*a].weight) {
            *b = *a;
            *a = i;
        } else if (*b == -1 || tree[i].weight < tree[*b].weight) {
            *b = i;
        }
    }
}

/* 每轮合并两个当前最小权根，生成一个新的父结点。 */
static int BuildHuffman(const int weight[], int n, HuffNode tree[])
{
    for (int i = 0; i < 2 * n - 1; ++i)
        tree[i] = (HuffNode){i < n ? weight[i] : 0, -1, -1, -1};
    for (int i = n; i < 2 * n - 1; ++i) {
        int a, b;
        SelectTwo(tree, i, &a, &b);
        tree[a].parent = tree[b].parent = i;
        tree[i].left = a;
        tree[i].right = b;
        tree[i].weight = tree[a].weight + tree[b].weight;
    }
    return 2 * n - 2;
}

static int Wpl(const HuffNode tree[], int root, int depth)
{
    if (tree[root].left == -1 && tree[root].right == -1)
        return tree[root].weight * depth;
    return Wpl(tree, tree[root].left, depth + 1) +
           Wpl(tree, tree[root].right, depth + 1);
}

/* parent[root] 保存负的集合大小；非根保存双亲下标。 */
static void SetInit(int parent[], int n)
{
    for (int i = 0; i < n; ++i) parent[i] = -1;
}
static int Find(int parent[], int x)
{
    if (parent[x] < 0) return x;
    return parent[x] = Find(parent, parent[x]);
}
static void Union(int parent[], int a, int b)
{
    int ra = Find(parent, a), rb = Find(parent, b);
    if (ra == rb) return;
    if (parent[ra] > parent[rb]) { int t = ra; ra = rb; rb = t; }
    parent[ra] += parent[rb];
    parent[rb] = ra;
}

int main(void)
{
    const int weight[] = {1, 2, 3, 4};
    HuffNode tree[HUFF_MAX];
    int root = BuildHuffman(weight, 4, tree);
    assert(tree[root].weight == 10);
    assert(Wpl(tree, root, 0) == 19);

    int parent[6];
    SetInit(parent, 6);
    Union(parent, 0, 1); Union(parent, 1, 2); Union(parent, 3, 4);
    assert(Find(parent, 0) == Find(parent, 2));
    assert(Find(parent, 0) != Find(parent, 4));
    Union(parent, 2, 4);
    assert(Find(parent, 3) == Find(parent, 0));
    return 0;
}
