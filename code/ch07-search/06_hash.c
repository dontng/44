#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

/*
 * 散列表先用 Hash(key) 算出理想桶位，再解决多个关键字落到同一位置的冲突。
 *
 * 开放定址：元素都在 slot 数组内，冲突后继续探测其他格子；
 * 链地址法：每个桶保存一条链，冲突元素仍留在同一个桶。
 *
 * 查找效率依赖装填因子和冲突分布，不是无条件 O(1)。
 */
#define CAP 11
#define EMPTY 0
#define USED 1
#define DELETED 2
typedef struct {
    int key;
    int state; /* EMPTY 从未使用；USED 有效；DELETED 曾使用后被删除。 */
} Slot;
typedef struct { Slot slot[CAP]; } OpenHash;

static int Hash(int key) { return (key % CAP + CAP) % CAP; }
static bool OpenInsert(OpenHash *table, int key)
{
    int first_deleted = -1; /* 记住第一个墓碑，但继续探测以排除重复键。 */
    for (int step = 0; step < CAP; ++step) {
        int pos = (Hash(key) + step) % CAP;
        if (table->slot[pos].state == USED && table->slot[pos].key == key) return true;
        if (table->slot[pos].state == DELETED && first_deleted == -1) first_deleted = pos;
        if (table->slot[pos].state == EMPTY) {
            /* EMPTY 表明这条探测链到此结束；优先复用前面遇到的墓碑。 */
            if (first_deleted != -1) pos = first_deleted;
            table->slot[pos] = (Slot){key, USED};
            return true;
        }
    }
    if (first_deleted != -1) {
        table->slot[first_deleted] = (Slot){key, USED};
        return true;
    }
    return false;
}
static int OpenSearch(const OpenHash *table, int key)
{
    for (int step = 0; step < CAP; ++step) {
        int pos = (Hash(key) + step) % CAP;
        if (table->slot[pos].state == EMPTY) return -1; /* 后面不可能再有同簇元素。 */
        if (table->slot[pos].state == USED && table->slot[pos].key == key) return pos;
    }
    return -1;
}
static bool OpenDelete(OpenHash *table, int key)
{
    int pos = OpenSearch(table, key);
    if (pos == -1) return false;
    table->slot[pos].state = DELETED; /* 不能改成 EMPTY，否则会截断同簇元素的查找。 */
    return true;
}

typedef struct HashNode { int key; struct HashNode *next; } HashNode;
typedef struct { HashNode *bucket[CAP]; } ChainHash;
static void ChainInsert(ChainHash *table, int key)
{
    int pos = Hash(key);
    HashNode *p = malloc(sizeof *p);
    if (p == NULL) abort();
    *p = (HashNode){key, table->bucket[pos]}; /* 头插到对应桶，不探测其他桶。 */
    table->bucket[pos] = p;
}
static bool ChainSearch(const ChainHash *table, int key)
{
    for (HashNode *p = table->bucket[Hash(key)]; p != NULL; p = p->next)
        if (p->key == key) return true;
    return false;
}
static void ChainDestroy(ChainHash *table)
{
    for (int i = 0; i < CAP; ++i) {
        HashNode *p = table->bucket[i];
        while (p != NULL) { HashNode *next = p->next; free(p); p = next; }
    }
}

int main(void)
{
    /* 1、12、23 哈希值相同，专门验证冲突链和删除墓碑。 */
    OpenHash open = {0};
    assert(OpenInsert(&open, 1) && OpenInsert(&open, 12) && OpenInsert(&open, 23));
    assert(OpenSearch(&open, 23) >= 0);
    assert(OpenDelete(&open, 12));
    assert(OpenSearch(&open, 23) >= 0);
    ChainHash chain = {0};
    ChainInsert(&chain, 1); ChainInsert(&chain, 12);
    assert(ChainSearch(&chain, 12) && !ChainSearch(&chain, 2));
    ChainDestroy(&chain);
    return 0;
}
