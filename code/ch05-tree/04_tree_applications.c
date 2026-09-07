#include <assert.h>
#include <limits.h>

/*
 * 本文件展示两种看似不同、实际都在“合并集合”的树应用。
 *
 * Huffman：反复合并当前权值最小的两棵树，使带权路径长度最小；
 * 并查集：把互不相交集合表示为父指针树，支持判断连通与合并集合。
 */
#define HUFF_MAX 15
typedef struct {
    int weight; /* 叶结点是原权值，非叶结点是左右子树权值和。 */
    int parent; /* -1 表示当前仍是一棵独立树的根。 */
    int left;   /* 左孩子在 tree 数组中的下标。 */
    int right;
} HuffNode;

static void SelectTwo(const HuffNode tree[], int end, int *a, int *b)
{
    /* 只在 parent==-1 的当前树根中选两个最小者。 */
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
        /* a、b 不再独立，它们共同归到新结点 i 下面。 */
        tree[a].parent = tree[b].parent = i;
        tree[i].left = a;
        tree[i].right = b;
        tree[i].weight = tree[a].weight + tree[b].weight;
    }
    return 2 * n - 2;
}

static int Wpl(const HuffNode tree[], int root, int depth)
{
    /* 只有原始叶结点计入 WPL：权值 × 从根到它的边数。 */
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
    /* 路径压缩：以后从 x 查根可以直接跳到集合代表。 */
    return parent[x] = Find(parent, parent[x]);
}
static void Union(int parent[], int a, int b)
{
    int ra = Find(parent, a), rb = Find(parent, b);
    if (ra == rb) return;
    /* 负值绝对值越大，树所含元素越多；小树接到大树下面。 */
    if (parent[ra] > parent[rb]) { int t = ra; ra = rb; rb = t; }
    parent[ra] += parent[rb];
    parent[rb] = ra;
}

int main(void)
{
    /* 1,2,3,4 的 Huffman 根权为 10，最优 WPL 为 19。 */
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
