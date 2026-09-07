#include <assert.h>
#include <stdlib.h>

typedef struct BiNode {
    char data;
    struct BiNode *left;
    struct BiNode *right;
} BiNode;

/* 先序序列中 # 表示空子树；这段代码把递归定义直接变成存储结构。 */
static BiNode *BuildPreorder(const char *serial, int *cursor)
{
    char value = serial[(*cursor)++];
    if (value == '#')
        return NULL;
    BiNode *node = malloc(sizeof *node);
    if (node == NULL)
        abort();
    node->data = value;
    node->left = BuildPreorder(serial, cursor);
    node->right = BuildPreorder(serial, cursor);
    return node;
}

static int Count(const BiNode *root)
{
    return root == NULL ? 0 : 1 + Count(root->left) + Count(root->right);
}

static int LeafCount(const BiNode *root)
{
    if (root == NULL)
        return 0;
    if (root->left == NULL && root->right == NULL)
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
    return 1 + (left > right ? left : right);
}

static void Destroy(BiNode *root)
{
    if (root == NULL)
        return;
    Destroy(root->left);
    Destroy(root->right);
    free(root);
}

int main(void)
{
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
