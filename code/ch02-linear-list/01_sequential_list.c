#include <assert.h>
#include <stdbool.h>
#include <stdio.h>

/*
 * 本文件训练顺序表最基本的读法。
 *
 * 统一约定：
 * 1. 题目说的“第 i 个元素”使用 1 基位序；
 * 2. C 数组使用 0 基下标，所以第 i 个元素位于 data[i - 1]；
 * 3. length 是有效元素个数，也恰好是表尾后第一个空闲下标。
 *
 * 阅读插入和删除时，只盯住三件事：检查哪段范围、元素向哪边搬、
 * length 在搬移前还是搬移后改变。
 */
#define MAXSIZE 100
typedef int ElemType;

typedef struct {
    ElemType data[MAXSIZE]; /* 连续存放全部元素。 */
    int length;             /* data[0..length-1] 有效。 */
} SqList;

/* 初始化只需把有效区间变为空，不需要清零整个数组。 */
void SqInit(SqList *L)
{
    L->length = 0;
}

int SqLength(const SqList *L)
{
    return L->length;
}

/* 若位序合法，把第 i 个元素写入 *e；失败时不修改 *e。 */
bool SqGet(const SqList *L, int i, ElemType *e)
{
    if (i < 1 || i > L->length)
        return false;

    *e = L->data[i - 1];
    return true;
}

/* 返回第一次出现的位置（1 基）；0 表示没有找到。 */
int SqLocate(const SqList *L, ElemType e)
{
    for (int i = 0; i < L->length; ++i) {
        if (L->data[i] == e)
            return i + 1;
    }
    return 0;
}

/*
 * 在第 i 个位置插入 e。
 * 函数结束后，原来的 [i..length] 整体后移一位，元素相对次序不变。
 */
bool SqInsert(SqList *L, int i, ElemType e)
{
    if (i < 1 || i > L->length + 1)
        return false;
    if (L->length == MAXSIZE)
        return false;

    /*
     * 循环开始时，data[j..旧 length] 已经腾好。
     * 从后向前搬，才能在覆盖 data[j] 之前先把它保存到 data[j+1]。
     */
    for (int j = L->length; j >= i; --j)
        L->data[j] = L->data[j - 1];

    L->data[i - 1] = e;
    ++L->length;
    return true;
}

/*
 * 删除第 i 个元素并通过 *e 带回被删值。
 * 空位从 i-1 开始，所以后继元素必须从前向后依次补过来。
 */
bool SqDelete(SqList *L, int i, ElemType *e)
{
    if (i < 1 || i > L->length)
        return false;

    *e = L->data[i - 1];

    /* 一轮结束后，空位从 data[j-1] 向右移动到了 data[j]。 */
    for (int j = i; j < L->length; ++j)
        L->data[j - 1] = L->data[j];

    --L->length;
    return true;
}

int main(void)
{
    SqList L;
    ElemType e = 777;

    /* 空表、非法操作：验证失败路径不会偷偷改写输出参数。 */
    SqInit(&L);
    assert(SqLength(&L) == 0);
    assert(!SqGet(&L, 1, &e) && e == 777);
    assert(!SqDelete(&L, 1, &e) && e == 777);

    /* 依次构造 [10, 20, 30]，其中 20 是插入到表中间的。 */
    assert(SqInsert(&L, 1, 10));
    assert(SqInsert(&L, 2, 30));
    assert(SqInsert(&L, 2, 20));
    assert(SqLength(&L) == 3);

    assert(SqGet(&L, 1, &e) && e == 10);
    assert(SqGet(&L, 2, &e) && e == 20);
    assert(SqGet(&L, 3, &e) && e == 30);
    assert(SqLocate(&L, 30) == 3);
    assert(SqLocate(&L, 99) == 0);

    /* 删除中间元素后，30 应向前补位。 */
    assert(SqDelete(&L, 2, &e) && e == 20);
    assert(SqLength(&L) == 2);
    assert(SqGet(&L, 2, &e) && e == 30);
    assert(!SqInsert(&L, 4, 40));

    puts("PASS: sequential list");
    return 0;
}
