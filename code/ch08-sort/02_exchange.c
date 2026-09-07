#include <assert.h>
#include <stdbool.h>
#include <string.h>

static void Swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }

static void BubbleSort(int a[], int n)
{
    for (int end = n - 1; end > 0; --end) {
        bool changed = false;
        for (int i = 0; i < end; ++i) {
            if (a[i] > a[i + 1]) {
                Swap(&a[i], &a[i + 1]);
                changed = true;
            }
        }
        if (!changed) break;
    }
}

static int Partition(int a[], int low, int high)
{
    int pivot = a[low];
    while (low < high) {
        while (low < high && a[high] >= pivot) --high;
        a[low] = a[high];
        while (low < high && a[low] <= pivot) ++low;
        a[high] = a[low];
    }
    a[low] = pivot;
    return low;
}
static void QuickRange(int a[], int low, int high)
{
    if (low >= high) return;
    int pivot = Partition(a, low, high);
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
