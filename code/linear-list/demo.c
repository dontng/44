#include "linked_list.h"
#include <stdio.h>
#include <stdlib.h>

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
