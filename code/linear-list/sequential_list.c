#include <assert.h>
#include <stdbool.h>
#include <stdio.h>

#define MAXSIZE 100
typedef int ElemType;

typedef struct {
    ElemType data[MAXSIZE];
    int length;
} SqList;

void SqInit(SqList *L)
{
    L->length = 0;
}

int SqLength(const SqList *L)
{
    return L->length;
}

bool SqGet(const SqList *L, int i, ElemType *e)
{
    if (i < 1 || i > L->length)
        return false;

    *e = L->data[i - 1];
    return true;
}

int SqLocate(const SqList *L, ElemType e)
{
    for (int i = 0; i < L->length; ++i) {
        if (L->data[i] == e)
            return i + 1;
    }
    return 0;
}

bool SqInsert(SqList *L, int i, ElemType e)
{
    if (i < 1 || i > L->length + 1)
        return false;
    if (L->length == MAXSIZE)
        return false;

    /* 从后向前腾位，避免覆盖尚未移动的元素。 */
    for (int j = L->length; j >= i; --j)
        L->data[j] = L->data[j - 1];

    L->data[i - 1] = e;
    ++L->length;
    return true;
}

bool SqDelete(SqList *L, int i, ElemType *e)
{
    if (i < 1 || i > L->length)
        return false;

    *e = L->data[i - 1];

    /* 从前向后补位，覆盖被删除元素留下的空位。 */
    for (int j = i; j < L->length; ++j)
        L->data[j - 1] = L->data[j];

    --L->length;
    return true;
}

int main(void)
{
    SqList L;
    ElemType e = 777;

    SqInit(&L);
    assert(SqLength(&L) == 0);
    assert(!SqGet(&L, 1, &e) && e == 777);
    assert(!SqDelete(&L, 1, &e) && e == 777);

    assert(SqInsert(&L, 1, 10));
    assert(SqInsert(&L, 2, 30));
    assert(SqInsert(&L, 2, 20));
    assert(SqLength(&L) == 3);

    assert(SqGet(&L, 1, &e) && e == 10);
    assert(SqGet(&L, 2, &e) && e == 20);
    assert(SqGet(&L, 3, &e) && e == 30);
    assert(SqLocate(&L, 30) == 3);
    assert(SqLocate(&L, 99) == 0);

    assert(SqDelete(&L, 2, &e) && e == 20);
    assert(SqLength(&L) == 2);
    assert(SqGet(&L, 2, &e) && e == 30);
    assert(!SqInsert(&L, 4, 40));

    puts("PASS: sequential list");
    return 0;
}
