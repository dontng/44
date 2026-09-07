#include <assert.h>
#include <string.h>

/*
 * 选择类排序先找“这一趟应该归位的元素”，再一次性放到目标位置。
 * 简单选择排序每趟扫描未排序区找最小值；
 * 堆排序用大根堆持续维护最大值，使选最大者从 O(n) 降到 O(log n) 调整。
 *
 * 数组按 0 基存堆：结点 i 的左孩子是 2*i+1，右孩子是 2*i+2。
 */
static void Swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }

static void SelectionSort(int a[], int n)
{
    /* 循环开始时 a[0..i-1] 已是全局最小的 i 个元素。 */
    for (int i = 0; i < n - 1; ++i) {
        int min = i;
        for (int j = i + 1; j < n; ++j)
            if (a[j] < a[min]) min = j;
        if (min != i) Swap(&a[i], &a[min]);
    }
}

/* a[root..end] 中，只有 root 可能破坏大根堆。 */
static void SiftDown(int a[], int root, int end)
{
    int saved = a[root]; /* root 暂时形成空位，沿较大孩子方向向下寻找归宿。 */
    for (int child = 2 * root + 1; child <= end; child = 2 * root + 1) {
        if (child < end && a[child] < a[child + 1]) ++child; /* 选更大的孩子上移。 */
        if (saved >= a[child]) break;
        a[root] = a[child]; /* 孩子上移填空，空位随 root 下沉。 */
        root = child;
    }
    a[root] = saved;
}
static void HeapSort(int a[], int n)
{
    /* 最后一个非叶结点是 n/2-1，自底向上筛成大根堆。 */
    for (int root = n / 2 - 1; root >= 0; --root) SiftDown(a, root, n - 1);
    for (int end = n - 1; end > 0; --end) {
        Swap(&a[0], &a[end]);       /* 当前最大值归位。 */
        SiftDown(a, 0, end - 1);
    }
}

static void Check(void (*sort)(int *, int))
{
    int a[] = {6, 3, 8, 2, 7, 1};
    const int expected[] = {1, 2, 3, 6, 7, 8};
    sort(a, 6);
    assert(memcmp(a, expected, sizeof a) == 0);
}
int main(void) { Check(SelectionSort); Check(HeapSort); return 0; }
