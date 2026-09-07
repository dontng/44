#include <assert.h>
#include <stdlib.h>

typedef struct Node {
    int key;
    int height;
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
    if (root == NULL) return NewNode(key);
    if (key < root->key) root->left = BstInsert(root->left, key);
    else if (key > root->key) root->right = BstInsert(root->right, key);
    Update(root);
    return root;
}
static Node *Search(Node *root, int key)
{
    while (root != NULL && root->key != key)
        root = key < root->key ? root->left : root->right;
    return root;
}
static Node *BstDelete(Node *root, int key)
{
    if (root == NULL) return NULL;
    if (key < root->key) root->left = BstDelete(root->left, key);
    else if (key > root->key) root->right = BstDelete(root->right, key);
    else if (root->left == NULL || root->right == NULL) {
        Node *child = root->left != NULL ? root->left : root->right;
        free(root);
        return child;
    } else {
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
    Node *new_root = old_root->left;
    old_root->left = new_root->right;
    new_root->right = old_root;
    Update(old_root); Update(new_root);
    return new_root;
}
static Node *RotateLeft(Node *old_root)
{
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
        if (key > root->left->key) root->left = RotateLeft(root->left); /* LR */
        return RotateRight(root);                                      /* LL */
    }
    if (balance < -1) {
        if (key < root->right->key) root->right = RotateRight(root->right); /* RL */
        return RotateLeft(root);                                           /* RR */
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
    Node *bst = NULL;
    const int values[] = {5, 2, 8, 1, 3, 7, 9};
    for (int i = 0; i < 7; ++i) bst = BstInsert(bst, values[i]);
    assert(Search(bst, 7) != NULL && Search(bst, 6) == NULL);
    bst = BstDelete(bst, 5);
    assert(bst->key == 7 && Search(bst, 5) == NULL);
    Destroy(bst);

    Node *avl = NULL;
    const int unbalanced[] = {30, 10, 20, 40, 50};
    for (int i = 0; i < 5; ++i) avl = AvlInsert(avl, unbalanced[i]);
    assert(avl->key == 20);
    assert(abs(Height(avl->left) - Height(avl->right)) <= 1);
    Destroy(avl);
    return 0;
}
