#include <assert.h>

typedef struct { int key; char original; } Record;

static void StableInsertion(Record a[], int n)
{
    for (int i = 1; i < n; ++i) {
        Record saved = a[i];
        int j = i - 1;
        while (j >= 0 && a[j].key > saved.key) { a[j + 1] = a[j]; --j; }
        a[j + 1] = saved;
    }
}

/* 快速选择只保证第 k 个元素归位，不负责排好其余元素。 */
static int KthSmallest(int a[], int left, int right, int k)
{
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
        if (i == k) return a[i];
        if (i < k) left = i + 1;
        else right = i - 1;
    }
    return 0;
}

int main(void)
{
    Record records[] = {{2,'A'}, {1,'B'}, {2,'C'}, {1,'D'}};
    StableInsertion(records, 4);
    assert(records[0].original == 'B' && records[1].original == 'D');
    assert(records[2].original == 'A' && records[3].original == 'C');
    int values[] = {8, 3, 1, 7, 4, 6, 2, 5};
    assert(KthSmallest(values, 0, 7, 3) == 4);
    return 0;
}
