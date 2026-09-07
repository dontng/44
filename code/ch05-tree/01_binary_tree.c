#include <assert.h>
#include <stdlib.h>

/*
 * 二叉树代码最适合从递归定义进入：一棵非空树 = 根 + 左子树 + 右子树。
 * 因此建树、计数、求高和销毁都使用相同骨架：
 * 先处理当前根，再把同一个问题交给规模更小的左右子树。
 *
 * 本例约定空树高度为 0，叶结点高度为 1。
 */
typedef struct BiNode {
    char data;             /* 当前根保存的数据。 */
    struct BiNode *left;   /* NULL 表示没有左孩子。 */
    struct BiNode *right;  /* NULL 表示没有右孩子。 */
} BiNode;

/* 先序序列中 # 表示空子树；这段代码把递归定义直接变成存储结构。 */
static BiNode *BuildPreorder(const char *serial, int *cursor)
{
    /* cursor 由所有递归层共享，每读一个符号就永久向后推进。 */
    char value = serial[(*cursor)++];
    if (value == '#')
        return NULL;
    BiNode *node = malloc(sizeof *node);
    if (node == NULL)
        abort();
    node->data = value;
    node->left = BuildPreorder(serial, cursor);  /* 先序：根之后完整描述左子树。 */
    node->right = BuildPreorder(serial, cursor); /* 左子树结束后才轮到右子树。 */
    return node;
}

static int Count(const BiNode *root)
{
    /* 当前根贡献 1，其余结点全部落在两棵子树中。 */
    return root == NULL ? 0 : 1 + Count(root->left) + Count(root->right);
}

static int LeafCount(const BiNode *root)
{
    if (root == NULL)
        return 0;
    if (root->left == NULL && root->right == NULL) /* 没有孩子才是叶结点。 */
        return 1;
    return LeafCount(root->left) + LeafCount(root->right);
}

static int DegreeTwoCount(const BiNode *root)
{
    if (root == NULL)
        return 0;
    int self = root->left != NULL && root->right != NULL;
    return self + DegreeTwoCount(root->left) + DegreeTwoCount(root->right);
}

static int Height(const BiNode *root)
{
    if (root == NULL)
        return 0;
    int left = Height(root->left);
    int right = Height(root->right);
    return 1 + (left > right ? left : right); /* 最深子树高度再加当前层。 */
}

static void Destroy(BiNode *root)
{
    if (root == NULL)
        return;
    /* 必须先释放两棵子树，最后释放根；否则会丢掉访问孩子的入口。 */
    Destroy(root->left);
    Destroy(root->right);
    free(root);
}

int main(void)
{
    /* ABD###C## 描述的树有 4 个结点、2 个叶子、高度 3。 */
    int cursor = 0;
    BiNode *root = BuildPreorder("ABD###C##", &cursor);
    assert(Count(root) == 4);
    assert(LeafCount(root) == 2);
    assert(DegreeTwoCount(root) == 1);
    assert(LeafCount(root) == DegreeTwoCount(root) + 1);
    assert(Height(root) == 3);
    Destroy(root);
    return 0;
}
