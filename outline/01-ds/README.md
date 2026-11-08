# 数据结构（408 考纲知识库分册）

> 📍 **导航**：[返回知识库总目录](../README.md)
>
> 本分册共收录 **29 个细粒度专题**，覆盖基本概念与复杂度、线性表、栈、队列和数组、树与二叉树、图、查找、排序。

---

## 目录索引

### 基本概念与复杂度
- [数据结构基本概念：逻辑结构、物理结构与运算关系](01-concepts/01-data-structures-basics.md)
- [算法复杂度分析：大O渐进分析、递归栈分析与循环累加模型](01-concepts/02-algorithm-complexity.md)

### 线性表
- [顺序表：物理连续分配、随机存取与增删搬迁代价](02-linear-list/01-sequential-list.md)
- [链表：单链表、双链表、循环链表与头结点作用](02-linear-list/02-linked-list.md)

### 栈、队列和数组
- [栈：LIFO特性、表达式求值与括号匹配](03-stack-queue-array/01-stack.md)
- [队列：FIFO特性、循环队列判空判满与双端队列](03-stack-queue-array/02-queue.md)
- [特殊矩阵压缩存储：对称矩阵、三角矩阵与三对角矩阵下标映射](03-stack-queue-array/03-matrix-compression.md)

### 树与二叉树
- [二叉树性质与存储：满二叉树、完全二叉树与节点计算公式](04-tree/01-binary-tree-properties.md)
- [二叉树遍历：先序、中序、后序与层次遍历递归与非递归](04-tree/02-tree-traversal.md)
- [线索二叉树：线索化定义、空指针利用与前驱后继寻找](04-tree/03-threaded-binary-tree.md)
- [树与森林：孩子兄弟表示法与森林-二叉树互转](04-tree/04-forest-conversion.md)
- [哈夫曼树与编码：带权路径长度WPL与前缀编码构建](04-tree/05-huffman-tree.md)
- [并查集与堆：双亲表示法、路径压缩与大根堆维护](04-tree/06-heap-and-union-find.md)

### 图
- [图的存储结构：邻接矩阵、邻接表、十字链表与邻接多重表](05-graph/01-graph-storage.md)
- [图的遍历：深度优先搜索DFS与广度优先搜索BFS](05-graph/02-graph-traversal.md)
- [最小生成树：Prim算法与Kruskal算法权衡](05-graph/03-minimum-spanning-tree.md)
- [最短路径：Dijkstra单源算法与Floyd全源算法](05-graph/04-shortest-path.md)
- [拓扑排序与关键路径：AOV网环路检测与AOE网关键活动](05-graph/05-topo-and-critical-path.md)

### 查找
- [线性查找与折半查找：顺序查找、分块查找与二分查找判定树](06-search/01-linear-and-binary-search.md)
- [二叉搜索树BST：查找、插入、删除与中序有序性](06-search/02-binary-search-tree.md)
- [平衡二叉树与红黑树：AVL旋转调整与红黑树五大特性](06-search/03-balanced-trees.md)
- [B树与B+树：多路平衡查找树、节点分裂合并与索引应用](06-search/04-b-trees.md)
- [散列表：散列函数构造、冲突解决与装填因子分析](06-search/05-hash-tables.md)
- [字符串模式匹配与KMP算法：朴素匹配回溯缺陷、主串不回溯推导、next与nextval数组手算轨迹](06-search/06-string-matching-kmp.md)

### 排序
- [简单插入、冒泡与选择：稳定排序与就地排序基础](07-sort/01-simple-sorts.md)
- [快速排序与归并排序：分治思想、轴点划分与二路归并](07-sort/02-efficient-sorts.md)
- [堆排序：堆调整建堆、筛选下沉与原地堆排](07-sort/03-heap-sort.md)
- [外部排序：多路平衡归并、败者树与置换-选择排序](07-sort/04-external-sort.md)
- [希尔排序与基数排序：增量序列分组插入、稳定性反例与多关键字LSD分配收集轨迹](07-sort/05-shell-and-radix-sort.md)
