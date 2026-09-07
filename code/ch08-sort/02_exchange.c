#include <assert.h>
#include <stdbool.h>
#include <string.h>

/*
 * 交换类排序通过比较元素后改变相对位置。
 *
 * 冒泡排序每趟把当前最大值逐步交换到区间末尾；
 * 快速排序选一个枢轴，使左侧不大于它、右侧不小于它，再递归处理两侧。
 * 快排的关键不是递归模板，而是 Partition 结束时枢轴已经最终归位。
 */
static void Swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }

static void BubbleSort(int a[], int n)
{
    /* 每趟结束后 a[end] 是未排序区最大值，之后不再参与比较。 */
    for (int end = n - 1; end > 0; --end) {
        bool changed = false;
        for (int i = 0; i < end; ++i) {
            if (a[i] > a[i + 1]) {
                Swap(&a[i], &a[i + 1]);
                changed = true;
            }
        }
        if (!changed) break; /* 一趟没有逆序交换，整个数组已经有序。 */
    }
}

static int Partition(int a[], int low, int high)
{
    int pivot = a[low]; /* 先保存枢轴，a[low] 暂时成为可覆盖的空位。 */
    while (low < high) {
        /* 右侧找到小于 pivot 的元素，填入左侧空位。 */
        while (low < high && a[high] >= pivot) --high;
        a[low] = a[high];
        /* 空位转到右侧；再从左找大于 pivot 的元素填过去。 */
        while (low < high && a[low] <= pivot) ++low;
        a[high] = a[low];
    }
    a[low] = pivot; /* 两个游标相遇处就是枢轴最终位置。 */
    return low;
}
static void QuickRange(int a[], int low, int high)
{
    if (low >= high) return;
    int pivot = Partition(a, low, high);
    /* 枢轴无需再排，只递归处理它两侧的子区间。 */
    QuickRange(a, low, pivot - 1);
    QuickRange(a, pivot + 1, high);
}
static void QuickSort(int a[], int n) { QuickRange(a, 0, n - 1); }

static void Check(void (*sort)(int *, int))
{
    int a[] = {5, 1, 4, 2, 8, 2};
    const int expected[] = {1, 2, 2, 4, 5, 8};
    sort(a, 6);
    assert(memcmp(a, expected, sizeof a) == 0);
}
int main(void) { Check(BubbleSort); Check(QuickSort); return 0; }
