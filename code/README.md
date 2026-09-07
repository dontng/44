# 数据结构：在代码里读懂，再按需要修改

第一份：[带头结点的单链表](linear-list/linked_list.c)。定义、创建、增删改查、遍历和清理都在这一个文件；先看定义和 `main` 的完整例子，再回看感兴趣的操作。无需先读其他项目文档，也不要求先默写。

代码中的注释解释字段的意义、操作成立的理由、容易破坏的连接，以及需求变化时要联动修改的位置。末尾保留循环、双向等表示变化的入口，当前只实现一种链表。需要专项算法时，再追加到已能读懂的实现上。

有 C 编译器时，在仓库根目录运行（Windows 的 GCC 也可用，输出文件可改名为 `linked-list.exe`）：

```sh
cc -std=c11 -Wall -Wextra -Wpedantic code/linear-list/linked_list.c -o /tmp/linked-list
/tmp/linked-list
```

运行会打印同一条表从创建、插入、查询、修改、删除到清空重用的变化。不运行也可以沿 `main` 旁的预期结果阅读。要试着修改，可把例子中的中间插入改成首位或末尾插入，观察同一个函数如何处理。

维护者检查：`test_linked_list.c` 检查空表、首尾、非法位序和连续操作后的链表内容，不是新增学习任务。

```sh
cc -std=c11 -Wall -Wextra -Wpedantic code/linear-list/test_linked_list.c -o /tmp/test-linked-list
/tmp/test-linked-list
```

后续内容以实际需求追加：优先保持一份可读、可运行的实现；解释留在发生问题的语句附近，变体说明必须覆盖操作联动。一次新增内容的数量由阅读效果决定，不把目录扩充当成掌握进度。
