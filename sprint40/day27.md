# Day 27｜树与图攻坚｜BST 区间、相邻候选

[← Day 26](day26.md) · [总入口](README.md) · [Day 28 →](day28.md)

**今日判断。** 用BST的顺序丢掉整棵无关子树。最近关键字最多来自 k 两侧各一个候选，等距时必须同时输出。

## 今天按这个顺序做

1. **0–10分钟｜回收。** 闭卷重写昨天的一处断点，写不出就标U。
2. **10–35分钟｜前置题。** 先做 [0805 模块](modules/0805.md) 的BST与B树题，再用 [Day 11 前缀树](day11.md) 对比两个结构向下走时各凭什么选分支。
3. **35–100分钟｜整题。** 两道题各给约30分钟，先完整写出步骤，剩余时间修正关键一步。先尝试5分钟，再开提示。
4. **100–120分钟｜验收。** 回答下方条件变化，订正后闭卷再写一次。到120分钟停止。

## 大题1｜2026-41 · 沿BST查找路径保留前驱与后继

[原题单 0915](../src/0915.md)

<img src="../bank/2026/q41.png" alt="2026-41" style="display: block; width: 46.5em; max-width: 100%; height: auto; margin: 12px 0;">

<details>
<summary>没有入口时的第一步</summary>

遇到 x<k 时记录候选 x 并向右，否则向左。命中 k 时最小差已是0。

</details>

<details>
<summary>完整解法与必要补学</summary>

（1）按严格BST约定，关键字互异。若当前值小于 k，当前结点及其左子树都不大于当前值，保留当前值后可以舍弃左子树。大于 k 时对称。未命中时只比较小于 k 的最大值和大于 k 的最小值。可能只有一侧，也可能两侧等距。

（2）下面用 long long 先扩宽再相减，避免32位 int 边界处的差值溢出。时间 O(h)，辅助空间 O(1)。

```c
#include <stdio.h>

void searchX(BTree root, int k) {
    BTree lo = NULL, hi = NULL;
    for (BTree p = root; p != NULL; ) {
        if (p->data == k) {
            printf("0 %d\n", k);
            return;
        }
        if (p->data < k) {
            lo = p;
            p = p->right;
        } else {
            hi = p;
            p = p->left;
        }
    }
    if (lo == NULL && hi == NULL) return;
    long long dl = lo ? (long long)k - lo->data : -1;
    long long dh = hi ? (long long)hi->data - k : -1;
    long long best = (dl >= 0 && (dh < 0 || dl <= dh)) ? dl : dh;
    printf("%lld", best);
    if (dl == best) printf(" %d", lo->data);
    if (dh == best) printf(" %d", hi->data);
    putchar('\n');
}
```

</details>

<details>
<summary>重做后检查</summary>

用键值{2,6}分别查4、1、6，应得到差2且输出2和6、差1只输出2、差0只输出6。

</details>

## 大题2｜2022-41 · 顺序存储BST判定（闭卷重做）

[Day 01 原图与折叠讲解](day01.md)。只做原页大题2。先检查整棵树满足区间约束，再解释为什么此前提成立时新题只走一条路径。

## 闭卷变式

查 k=4 时，候选2和6同时存在。能在首次遇到差2的结点就停止吗？

<details>
<summary>检查答案</summary>

不能。另一侧可能还有差更小或等距的结点。只有命中 k 才能立即结束。

</details>

记录：实际用时__；两次作答状态 I／H／U__；卡住的题号与第一处断点__。
