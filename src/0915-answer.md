[« 0914-answer](0914-answer.md)　　[0916-answer »](0916-answer.md)

# 0915 Answer｜树上的递归究竟传什么

> [5 道完整原题](0915.md) · [0914 的扫描状态](0914-answer.md) · [能力账本](answer-quality/learning-ledger.md)
>
> 树形只是外壳：每道题分别要传深度、分支数量、括号边界、终止标记或中序前驱。讲解已核原题，限时独立作答未验。

<details><summary><strong>考场起手</strong></summary>

| 题 | 草稿第一行 | 检查边界 |
| --- | --- | --- |
| 01 | 根深度 0；叶子才累加 `weight×depth` | 根本身是叶子 |
| 02 | k 条子边：`km=N−1` | 高度从 1 算 |
| 03 | 子树输出时在运算符外包括号 | 一元减只有一子树 |
| 04 | 编码树遇终点标记后不能再向下 | 某码是另一码前缀 |
| 05 | 中序遍历每个非 `−1`，与前一个真结点比较 | 空位不是数值 −1 |

</details>

<a id="q01"></a>
## 01｜2014-41：WPL 累加的是叶子的深度

![2014-41 原题](../bank/2014/q41.png)

**（1）思路。** 根到根的边数为 0；沿边下探时深度加 1；只有左右孩子均空的叶子贡献 `weight×depth`，非叶结点的权值虽存在但不计 WPL。

**（2）结点定义。**

```c
typedef struct Node {
    struct Node *left;
    int weight;
    struct Node *right;
} Node;
```

**（3）实现。**

```c
long long wpl(const Node *p, int depth) {
    if (!p) return 0;
    if (!p->left && !p->right) return (long long)p->weight*depth;
    return wpl(p->left,depth+1)+wpl(p->right,depth+1);
}
/* 从 wpl(root,0) 调用 */
```

每结点访问一次，时间 `O(N)`；递归栈 `O(h)`，链状树最坏 `O(N)`。根为唯一叶子时深度 0，WPL 为 0。

<details open><summary>为什么不能在入结点时就累加</summary>题目明说所有**叶**的带权路径长度之和；内部结点权虽非负，不参加求和。若按层数从1乘权，所有叶子都会多算一个权重。</details>

<a id="q02"></a>
## 02｜2016-42：正则 k 叉树的叶子和高度边界

![2016-42 原题](../bank/2016/q42.png)

**（1）已知 m 个非叶结点。** 每个非叶结点发出 k 条边，共 `km`；树总边数是 `N−1`。所以 `N=km+1`，叶数 `N−m=(k−1)m+1`。不必预先假设每一层都填满。

**（2）高度 h。** 最多每层全展开，结点数 `1+k+...+k^(h−1)=(k^h−1)/(k−1)`。最少则在前 h−1 层各只留**一个**内部结点延长主干，每个内部结点依然必须生 k 个孩子：`1+k(h−1)` 个结点。h=1 时两端都为1；h=3、k=2 的最少形状为根和下一层各有一个内部结点，共5个。

<details open><summary>挡住两个直觉错法</summary>最少不是 h 个（那是一条单链，违反每个非叶都有 k 孩子）；最多不是 `k^h`（那只是下一层的满层规模）。从边数下手可立即拿到第（1）问的分。</details>

<a id="q03"></a>
## 03｜2017-41：树的中序遍历必须保护运算顺序

![2017-41 原题](../bank/2017/q41.png)

**（1）思路。** 普通中序只输出符号会把 `a+b` 接着 `*` 误读为 `a+b*c`。每个运算符子树先输出左括号，递归左子树、运算符、右子树，再输出右括号；叶子直接打印操作数。一元减仅有右孩子时，括号内先打印 `-` 再打印孩子。

**（2）代码。**

```c
#include <stdio.h>
typedef struct node {
    char data[10];
    struct node *left,*right;
} BTree;
void printExpr(const BTree *p) {
    if (!p) return;
    if (!p->left && !p->right) { printf("%s",p->data); return; }
    putchar('(');
    if (p->left) printExpr(p->left);
    printf("%s",p->data);               // 一元减在唯一右子树之前
    if (p->right) printExpr(p->right);
    putchar(')');
}
```

外层多一对括号不影响等价性：例一为 `((a+b)*(c*(-d)))`，例二为 `((a*b)+(-(c-d)))`。若要求与题面示例的打印完全一致，只需在根层省去最外括号，内层继续保持；`O(N)` 时间、`O(h)` 栈空间。

<details open><summary>一元和二元减怎样辨认</summary>观察孩子数量，不只看字符 `-`：图一减结点仅右孩子 d，输出 `(-d)`；图二右侧外减结点仅右孩子为另一个二元减，输出 `(-(c-d))`。若树约定唯一孩子在左边，需按数据定义调整分支，而非把右孩子假装为左操作数。</details>

<a id="q04"></a>
## 04｜2020-42：前缀码作为一棵带终点的二叉树

![2020-42 原题](../bank/2020/q42.png)

**（1）结构。** 用二叉字典树（Trie）：每位 0 走左边、1 走右边；字符保存在码字路径终点。最长码长 L，则根到终点的深度不超过 L。至少两个字符的前缀码不应把某字符放在根。

**（2）译码。** 从根读位并移动；到带字符的终点就输出该字符，指针回根继续读。若边不存在或输入结束时停在非终点，这串输入不是该码集可完整译出的串。前缀性质保证抵达终点即完成当前码字，不需猜是否继续向下。

**（3）判定。** 逐个插入码字：若走位途中遇到已经标为终点的结点，旧码是新码的前缀；到新码终点时若已有字符或已有后代，分别是重复编码或新码为旧码前缀。出现任一种冲突便不具备前缀特性；全插完无冲突才合格。处理所有位的时间 `O(码字总长度)`，树空间同阶；译码时间 `O(输入位数)`。

<details open><summary>为何不能只比相同长度的码</summary>`0` 与 `01` 长度不同，读到 0 时已无法知道该停还是继续；根到 0 的结点同时作“终点”和“内结点”就是冲突信号。不同字符也不能共用完全相同的码字。</details>

<a id="q05"></a>
## 05｜2022-41：顺序存储树验证 BST

![2022-41 原题](../bank/2022/q41.png)

**（1）思路。** 数组下标 i 的左右孩子分别为 `2i+1`、`2i+2`；`-1` 表示**没有结点**，即使其下标小于 `ElemNum` 也要跳过。二叉搜索树中序遍历真实结点应严格递增（题给结点值均为正整数，本解采用无重复键的 BST 约定）。只保留前一真结点值即可。

**（2）代码。**

```c
typedef struct { int SqBiTNode[MAX_SIZE]; int ElemNum; } SqBiTree;
int check(const SqBiTree *T, size_t i, int *prev, int *have) {
    if (i >= (size_t)T->ElemNum || T->SqBiTNode[i] == -1) return 1;
    if (!check(T,2*i+1,prev,have)) return 0;
    if (*have && T->SqBiTNode[i] <= *prev) return 0;
    *prev=T->SqBiTNode[i]; *have=1;
    return check(T,2*i+2,prev,have);
}
int isBST(const SqBiTree *T) {
    int prev=0, have=0;
    return T && T->ElemNum>0 && check(T,0,&prev,&have);
}
```

T1 的中序为 `25,27,30,40,60,80`，返回 true；T2 左子树含 50，根为 40，中序出现 `50,30,...,40`，返回 false。实际访问 `ElemNum` 范围内下标，每个真实结点一次，时间 `O(ElemNum)` 上界；额外递归栈 `O(h)`（顺序存储的最大有效深度）。

<details open><summary>为何不能只比较父子</summary>某个结点可能小于自己的父亲，却大于更上层的祖先，违反整棵左子树都小于根的条件。中序严格递增将所有祖先约束一次检查完。数组空位 -1 不是可比较的负值，先过滤再比较。</details>

## 延迟练习

遮住解答给这五题各写一句“递归/遍历必须带着什么”：深度、边数、括号、终点、前驱。随后独立完成代码和边界例，按实际用时记熟练度；讲解完成不等于通关。
