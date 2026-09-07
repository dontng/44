/*
 * 线性表 · 带头结点的单链表（C11）
 *
 * 阅读入口：先看下面的定义，再跳到 main 看同一条表怎样变化；
 * 想弄清某一步，再回到同名函数。注释中的“怎样写 / 怎样改”留作回查。
 *
 * 全文约定：元素位序从 1 开始，头结点是第 0 个结点，不存有效元素。
 * L 指向头结点；L->next 指向首元结点；最后一个结点的 next 是 NULL。
 * 空表也有头结点。NULL 表示没有创建成功，和“已创建的空表”不同。
 * 各操作要求传入有效的 L；get/delete 的 out 须指向可写的 ElemType 变量。
 * 非法位序返回 false，不改变链表，也不改 out 指向的值。
 */
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef int ElemType;            // 要存别的简单数值类型，从这里改。

typedef struct LNode {
    ElemType data;              // 元素本身。头结点也有这个字段，但不使用它。
    struct LNode *next;         // 后继的地址，不是后继元素的值。
} LNode, *LinkList;
// LNode 是结点类型；LinkList 是 LNode * 的别名，不是另一种结构。
// LNode *p 只声明一个存地址的变量，不会自动创建结点。
// p->next 等价于 (*p).next：找到 p 指向的结点，再访问它的 next 字段。
// p = p->next 只移动观察位置；p->next = s 才会改变链上的连接。

LinkList list_create(void)
{
    LinkList L = malloc(sizeof *L); // 按“一个结点”申请，不是 sizeof(L) 的指针大小。
    if (L != NULL)
        L->next = NULL;             // 新表没有首元结点；头结点 data 不必赋值。
    return L;                      // 调用者保存这个地址，后续都操作同一条表。
}

bool list_empty(LinkList L)
{
    return L->next == NULL;
}

int list_length(LinkList L)
{
    int n = 0;
    for (LNode *p = L->next; p != NULL; p = p->next)
        ++n;
    return n;
}
// 这里不另存 length 字段：少维护一个状态，代价是求长度需要 O(n)。
// 怎样改：若增加长度字段，初始化、成功插入、成功删除、清空都要同步维护。

static LNode *node_at(LinkList L, int pos)
{
    // 共用的定位：从头结点走 pos 步。pos=0 返回头结点，供插删找前驱。
    // 怎样写：先确定“p 当前是第几个”，再写移动条件；不用背循环。
    if (pos < 0)
        return NULL;
    LNode *p = L;
    for (int j = 0; p != NULL && j < pos; ++j)
        p = p->next;
    return p;                      // 走出链尾则返回 NULL；不能再解引用它。
}

bool list_get(LinkList L, int pos, ElemType *out)
{
    if (pos < 1)
        return false;              // 第 0 个是头结点，不是一个可读取的元素。
    LNode *p = node_at(L, pos);
    if (p == NULL)
        return false;
    *out = p->data;                 // out 指向调用者的变量；成功时才写入它。
    return true;                   // 状态和值分开，0、-1 都可以是正常元素。
}

int list_find(LinkList L, ElemType value)
{
    int pos = 1;
    for (LNode *p = L->next; p != NULL; p = p->next, ++pos)
        if (p->data == value)
            return pos;            // 有重复值时，返回第一次出现的位序。
    return 0;                      // 元素从 1 编号，所以 0 可表示未找到。
}
// 查：get 是“给位置取值”，find 是“给值找位置”；链表两者最坏均为 O(n)。
// 怎样改：想找最后一次出现，命中时记录 pos，遍历结束再返回记录。

bool list_update(LinkList L, int pos, ElemType value)
{
    if (pos < 1)
        return false;
    LNode *p = node_at(L, pos);
    if (p == NULL)
        return false;
    p->data = value;                // 改数据不改 next，因此元素次序没有变化。
    return true;
}

bool list_insert(LinkList L, int pos, ElemType value)
{
    // 在第 pos 个位置插入：旧的第 pos 个及以后元素的位序增加 1。
    // 合法范围是 1..n+1。找第 pos-1 个结点即可，不必先遍历求 n。
    if (pos < 1)
        return false;
    LNode *pre = node_at(L, pos - 1);
    if (pre == NULL)
        return false;
    LNode *s = malloc(sizeof *s);
    if (s == NULL)
        return false;              // 申请失败时还没改链，原表保持完整。
    s->data = value;

    s->next = pre->next;            // 先让 s 保存原后继的地址。
    pre->next = s;                  // 再让前驱连接 s；两句不能直接互换。
    // 若先改 pre->next，再从它取原后继，取到的已是 s，造成 s 指向自身。
    // 插在末尾时原后继是 NULL，这两句照样成立；空表插入也一样。
    return true;
}

bool list_delete(LinkList L, int pos, ElemType *out)
{
    if (pos < 1)
        return false;
    LNode *pre = node_at(L, pos - 1);
    if (pre == NULL || pre->next == NULL)
        return false;              // 前驱存在还不够：其后必须有待删元素。
    LNode *q = pre->next;
    *out = q->data;                 // 必须在释放 q 之前取出数据和后继。
    pre->next = q->next;            // 前驱越过 q，直接连接 q 的后继。
    free(q);                       // 只断链会泄漏内存；释放后不能再访问 q。
    return true;
}
// 插删：已知前驱时接线是 O(1)；按位序寻找前驱使整个函数最坏为 O(n)。
// 怎样写：先圈出前驱、目标和后继，再写保留数据、接线、释放这几个动作。
// 怎样改：按值删除，可用 find 得到位置再 delete，虽遍历两遍仍为 O(n)。
// 需要一遍时，让 pre 停在首个满足 pre->next->data == value 的结点之前，
// 然后复用本函数从 q 的定义开始的部分。先判断 pre->next 非空才能读 data。

void list_print(LinkList L)
{
    printf("[");
    for (LNode *p = L->next; p != NULL; p = p->next) {
        if (p != L->next)
            printf(", ");
        printf("%d", p->data);
    }
    puts("]");
}
// 遍历的核心是起点、终点、下一步；打印只是到达结点后做的一件事。
// 怎样改：保留循环，换循环体，就能计数、求和、逐个修改元素。
// 若 ElemType 改了，打印格式和 find 的相等判断也要检查是否适配。

void list_clear(LinkList L)
{
    LNode *p = L->next;
    while (p != NULL) {
        LNode *next = p->next;      // 释放前保存去下一个结点的路。
        free(p);
        p = next;                  // 不能写成 free(p) 后再 p = p->next。
    }
    L->next = NULL;                 // 保留头结点：这条表还能继续插入。
}

void list_destroy(LinkList L)
{
    list_clear(L);
    free(L);                       // 连头结点也释放；调用者随后把自己的 L 置空。
}

/*
 * 定义变了，操作怎样跟着变？需要时再读这一段。
 *
 * 循环单链表：结点定义不变。空表 L->next=L，链尾 next 指回 L。
 * 判空改成 L->next==L；遍历、清空的终点改成 p==L，清空后恢复自环。
 * node_at 要防止绕回 L 后继续计数；delete 要拒绝 pre->next==L。
 * insert 的两句接线可以保留。仅修改链尾，其他函数不改，会造成死循环。
 *
 * 双链表：定义增加 struct LNode *prior，初始化头结点 prior=NULL。
 * 插入时在改 pre->next 之前增加 s->prior=pre，
 * 并在 s->next!=NULL 时令 s->next->prior=s。
 * 删除时还要在 q->next!=NULL 时令 q->next->prior=pre，再释放 q。
 * next 方向遍历保留；反向遍历要先拿到尾结点，再沿 prior 走到头结点。
 *
 * 无头结点：L 直接指向首元结点，空表 L=NULL。首位插删会改变 L 本身，
 * 不能只改函数里那个地址副本；需返回新表头，或用 LNode ** 接收 &L。
 * 静态链表：用数组槽位存结点、下标表示 next，另管空闲槽；不是改一个类型名。
 * 这些是修改入口，当前可运行版本始终是上面约定的单链表。
 */

#ifndef LINKED_LIST_NO_MAIN
// 演示中的失败检查只负责及时报告错误，不属于链表算法。
static void require(bool ok)
{
    if (!ok) {
        fputs("操作失败：检查位序或内存分配。\n", stderr);
        exit(EXIT_FAILURE);
    }
}

int main(void)
{
    LinkList L = list_create();
    require(L != NULL);
    ElemType value = 0;

    printf("创建空表："); list_print(L);                    // []
    require(list_insert(L, 1, 10));
    require(list_insert(L, 2, 30));
    require(list_insert(L, 2, 20));
    printf("中间插入："); list_print(L);                    // [10, 20, 30]
    require(list_get(L, 2, &value));                        // &value 把变量地址交给 out。
    printf("第2个元素=%d，30的位序=%d\n", value, list_find(L, 30));
    require(list_update(L, 2, 25));
    printf("修改第2个："); list_print(L);                   // [10, 25, 30]
    require(list_delete(L, 1, &value));
    printf("删除首元%d后：", value); list_print(L);         // [25, 30]
    printf("长度=%d，查找99的结果=%d\n", list_length(L), list_find(L, 99));
    printf("删除第0个成功吗？%s\n", list_delete(L, 0, &value) ? "是" : "否");
    printf("失败后原表："); list_print(L);                  // [25, 30]
    list_clear(L);
    printf("清空后为空吗？%s\n", list_empty(L) ? "是" : "否");
    require(list_insert(L, 1, 40));
    printf("清空后还能插入："); list_print(L);              // [40]
    list_destroy(L);
    L = NULL;                                             // 原地址已失效，不再使用。
    return 0;
}
#endif
