#include <assert.h>
#include <stdlib.h>

/*
 * BST 的核心不变量：任一结点左子树关键字更小，右子树关键字更大。
 * AVL 在此基础上增加：任一结点左右子树高度差绝对值不超过 1。
 *
 * 旋转不是交换几个数，而是在保持中序有序的前提下重新安排父子关系。
 * 阅读 AVL 插入时先按 BST 找位置，再沿返回路径更新高度、修复首个失衡。
 */
typedef struct Node {
    int key;
    int height;          /* 以该结点为根的树高；叶结点为 1。 */
    struct Node *left;
    struct Node *right;
} Node;

static int Height(const Node *p) { return p == NULL ? 0 : p->height; }
static int Max(int a, int b) { return a > b ? a : b; }
static void Update(Node *p) { p->height = 1 + Max(Height(p->left), Height(p->right)); }
static Node *NewNode(int key)
{
    Node *p = malloc(sizeof *p);
    if (p == NULL) abort();
    *p = (Node){key, 1, NULL, NULL};
    return p;
}

static Node *BstInsert(Node *root, int key)
{
    /* 递归返回的新根必须重新接回父结点，否则新结点会丢失。 */
    if (root == NULL) return NewNode(key);
    if (key < root->key) root->left = BstInsert(root->left, key);
    else if (key > root->key) root->right = BstInsert(root->right, key);
    Update(root);
    return root;
}
static Node *Search(Node *root, int key)
{
    while (root != NULL && root->key != key)
        root = key < root->key ? root->left : root->right; /* 每次排除一整棵子树。 */
    return root;
}
static Node *BstDelete(Node *root, int key)
{
    if (root == NULL) return NULL;
    if (key < root->key) root->left = BstDelete(root->left, key);
    else if (key > root->key) root->right = BstDelete(root->right, key);
    else if (root->left == NULL || root->right == NULL) {
        /* 0/1 个孩子：让唯一孩子直接接替被删结点的位置。 */
        Node *child = root->left != NULL ? root->left : root->right;
        free(root);
        return child;
    } else {
        /* 两个孩子：用右子树最小者替换，再删除那个重复关键字。 */
        Node *successor = root->right;
        while (successor->left != NULL) successor = successor->left;
        root->key = successor->key;
        root->right = BstDelete(root->right, successor->key);
    }
    Update(root);
    return root;
}

static Node *RotateRight(Node *old_root)
{
    /* old_root 的左孩子上升；它原来的右子树落到 old_root 左侧。 */
    Node *new_root = old_root->left;
    old_root->left = new_root->right;
    new_root->right = old_root;
    Update(old_root); Update(new_root);
    return new_root;
}
static Node *RotateLeft(Node *old_root)
{
    /* 与右旋完全镜像：右孩子上升，中间子树换边但中序次序不变。 */
    Node *new_root = old_root->right;
    old_root->right = new_root->left;
    new_root->left = old_root;
    Update(old_root); Update(new_root);
    return new_root;
}

static Node *AvlInsert(Node *root, int key)
{
    if (root == NULL) return NewNode(key);
    if (key < root->key) root->left = AvlInsert(root->left, key);
    else if (key > root->key) root->right = AvlInsert(root->right, key);
    else return root;
    Update(root);
    int balance = Height(root->left) - Height(root->right);
    if (balance > 1) {
        /* 新结点在“左孩子的右侧”是 LR，先把折线拉直；随后统一右旋。 */
        if (key > root->left->key) root->left = RotateLeft(root->left); /* LR */
        return RotateRight(root);                                      /* LL 或已转直的 LR */
    }
    if (balance < -1) {
        /* 右侧情况镜像处理：RL 先右旋右孩子，再左旋失衡根。 */
        if (key < root->right->key) root->right = RotateRight(root->right); /* RL */
        return RotateLeft(root);                                           /* RR 或已转直的 RL */
    }
    return root;
}

static void Destroy(Node *root)
{
    if (root == NULL) return;
    Destroy(root->left); Destroy(root->right); free(root);
}

int main(void)
{
    /* BST 删除根 5 时，右子树最小者 7 接替它。 */
    Node *bst = NULL;
    const int values[] = {5, 2, 8, 1, 3, 7, 9};
    for (int i = 0; i < 7; ++i) bst = BstInsert(bst, values[i]);
    assert(Search(bst, 7) != NULL && Search(bst, 6) == NULL);
    bst = BstDelete(bst, 5);
    assert(bst->key == 7 && Search(bst, 5) == NULL);
    Destroy(bst);

    /* 30,10,20 刻意制造 LR；40,50 又继续检验右侧修复。 */
    Node *avl = NULL;
    const int unbalanced[] = {30, 10, 20, 40, 50};
    for (int i = 0; i < 5; ++i) avl = AvlInsert(avl, unbalanced[i]);
    assert(avl->key == 20);
    assert(abs(Height(avl->left) - Height(avl->right)) <= 1);
    Destroy(avl);
    return 0;
}
