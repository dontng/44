#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <stdbool.h>

typedef int ElemType;
typedef struct LNode {
    ElemType data;          // 结点中的元素值。
    struct LNode *next;     // 后继结点的地址，链尾为 NULL。
} LNode, *LinkList;

/* 带头结点：L 指向不计入元素的头结点；空表 L->next == NULL。
 * 元素位序从 1 开始。除 create 外，各操作要求 L 已成功创建且未销毁。
 * get/delete 的 out 必须指向可写变量；失败不改表，也不改 *out。
 */
LinkList list_create(void);                         // 申请失败返回 NULL。
bool list_empty(LinkList L);
int list_length(LinkList L);
bool list_get(LinkList L, int pos, ElemType *out);   // 按位取值。
int list_find(LinkList L, ElemType value);           // 首次命中的位序；未找到为 0。
bool list_update(LinkList L, int pos, ElemType value);
bool list_insert(LinkList L, int pos, ElemType value); // 位序 1..n+1。
bool list_delete(LinkList L, int pos, ElemType *out);  // 位序 1..n。
void list_print(LinkList L);
void list_clear(LinkList L);                        // 保留头结点，可继续使用。
void list_destroy(LinkList L);                      // 释放头结点，L 随即失效。

#endif
