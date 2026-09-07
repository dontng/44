#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

#define CAP 11
#define EMPTY 0
#define USED 1
#define DELETED 2
typedef struct { int key; int state; } Slot;
typedef struct { Slot slot[CAP]; } OpenHash;

static int Hash(int key) { return (key % CAP + CAP) % CAP; }
static bool OpenInsert(OpenHash *table, int key)
{
    int first_deleted = -1;
    for (int step = 0; step < CAP; ++step) {
        int pos = (Hash(key) + step) % CAP;
        if (table->slot[pos].state == USED && table->slot[pos].key == key) return true;
        if (table->slot[pos].state == DELETED && first_deleted == -1) first_deleted = pos;
        if (table->slot[pos].state == EMPTY) {
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
        if (table->slot[pos].state == EMPTY) return -1;
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
    *p = (HashNode){key, table->bucket[pos]};
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
