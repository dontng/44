#include <assert.h>

/*
 * “排序算法比较”不能只背表格，本文件把两个性质变成可运行证据：
 * 稳定性：相等关键字排序后仍保持原输入次序；
 * 选择问题：只求第 k 小时，快速选择只需让一个枢轴位置正确，
 * 不必把其余元素全部排好。
 */
typedef struct { int key; char original; } Record;

static void StableInsertion(Record a[], int n)
{
    for (int i = 1; i < n; ++i) {
        Record saved = a[i];
        int j = i - 1;
        /* 只移动严格更大的记录；相等记录不越过，所以保持稳定。 */
        while (j >= 0 && a[j].key > saved.key) { a[j + 1] = a[j]; --j; }
        a[j + 1] = saved;
    }
}

/* 快速选择只保证第 k 个元素归位，不负责排好其余元素。 */
static int KthSmallest(int a[], int left, int right, int k)
{
    /* k 使用 0 基下标；每轮分区后，只保留包含 k 的那一侧。 */
    while (left <= right) {
        int pivot = a[left];
        int i = left, j = right;
        while (i < j) {
            while (i < j && a[j] >= pivot) --j;
            a[i] = a[j];
            while (i < j && a[i] <= pivot) ++i;
            a[j] = a[i];
        }
        a[i] = pivot;
        if (i == k) return a[i]; /* 枢轴恰好落在第 k 位，立即结束。 */
        if (i < k) left = i + 1;
        else right = i - 1;
    }
    return 0;
}

int main(void)
{
    /* A/C 与 B/D 分别同键，用 original 检查内部先后次序。 */
    Record records[] = {{2,'A'}, {1,'B'}, {2,'C'}, {1,'D'}};
    StableInsertion(records, 4);
    assert(records[0].original == 'B' && records[1].original == 'D');
    assert(records[2].original == 'A' && records[3].original == 'C');
    int values[] = {8, 3, 1, 7, 4, 6, 2, 5};
    assert(KthSmallest(values, 0, 7, 3) == 4);
    return 0;
}
