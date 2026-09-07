#include <assert.h>
#include <string.h>

static void Swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }

static void SelectionSort(int a[], int n)
{
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
    int saved = a[root];
    for (int child = 2 * root + 1; child <= end; child = 2 * root + 1) {
        if (child < end && a[child] < a[child + 1]) ++child;
        if (saved >= a[child]) break;
        a[root] = a[child];
        root = child;
    }
    a[root] = saved;
}
static void HeapSort(int a[], int n)
{
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
