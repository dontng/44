# 408 数据结构代码地图

这里是 `draft/data-structures/ch02—ch08` 的可执行版本。章节骨架负责防止遗漏考点；每份源码负责讲清一种结构、基本操作或应用机制，而不是堆积互不相干的“标准答案”。

## 统一约定

- 使用 C11，元素默认取 `int`，让注意力落在结构和算法上。
- 教材位序从 1 开始，C 数组下标从 0 开始。
- 可能失败的操作返回 `bool`，结果通过指针参数带回。
- 动态内存必须检查申请结果，并在测试结束后释放。
- 每个 `.c` 都是独立的最小程序，末尾 `main` 用断言给出可验证样例。

## 章节覆盖

| 王道小节 | 代码入口 | 覆盖内容 |
|---|---|---|
| 2.1—2.2 | `ch02-linear-list/01_sequential_list.c` | 线性表接口、顺序表增删查长 |
| 2.3 | `ch02-linear-list/02_singly_linked_list.c`、`03_linked_variants.c`、`04_list_algorithms.c` | 单/双/循环/静态链表、逆置与归并 |
| 3.1—3.2 | `ch03-stack-queue-array/01_stack_queue.c` | 顺序/链栈、循环/链队列、双端队列 |
| 3.3 | `ch03-stack-queue-array/02_applications.c` | 括号匹配、中缀转后缀、后缀求值、层次处理 |
| 3.4 | `ch03-stack-queue-array/03_matrix.c` | 特殊矩阵下标、三元组快速转置 |
| 4.2 | `ch04-string/01_pattern_matching.c` | BF、`next`、KMP |
| 5.1—5.2 | `ch05-tree/01_binary_tree.c` | 二叉树定义、结点计数与高度 |
| 5.3 | `ch05-tree/02_traversal_threading.c` | 递归/非递归/层序遍历、线索化 |
| 5.4 | `ch05-tree/03_tree_forest.c` | 双亲表示、孩子兄弟表示、森林遍历 |
| 5.5 | `ch05-tree/04_tree_applications.c` | Huffman、并查集 |
| 6.1—6.2 | `ch06-graph/01_storage.c` | 邻接矩阵、邻接表及增边 |
| 6.3 | `ch06-graph/02_traversal.c` | DFS、BFS |
| 6.4 | `ch06-graph/03_applications.c` | Prim、Kruskal、Dijkstra、Floyd、拓扑排序、关键路径 |
| 7.2 | `ch07-search/01_linear_binary.c` | 哨兵顺序查找、折半查找 |
| 7.3 | `ch07-search/02_bst_avl.c`、`03_red_black.c` | BST、AVL、红黑树的旋转与插入修复 |
| 7.4 | `ch07-search/04_b_tree.c`、`05_b_plus_tree.c` | B 树与 B+ 树的查找、插入、分裂和叶链范围查找 |
| 7.5 | `ch07-search/06_hash.c` | 开放定址、链地址法 |
| 8.1—8.4 | `ch08-sort/01_insertion.c`、`02_exchange.c`、`03_selection.c` | 插入/希尔、冒泡/快排、选择/堆排 |
| 8.5—8.6 | `ch08-sort/04_merge_radix_counting.c`、`05_compare.c` | 归并、基数、计数及性质对比 |
| 8.7 | `ch08-sort/06_external_sort.c` | 多路归并、败者树和最优归并树机制 |

## 运行和训练

在仓库根目录执行：

```bash
bash code/check.sh
```

检查通过只说明样例正确。学习一份代码时依次完成：指出状态由哪些字段保存；逐轮写出游标或容器内容；遮住核心循环补写；改变一个条件后重新通过断言。考题给出陌生写法时，按字段含义、初始化、循环终点和状态修改判断，不能按函数名猜作用。
