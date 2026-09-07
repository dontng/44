#include <assert.h>
#include <stdlib.h>
#include <string.h>

static void Merge(int a[], int temp[], int left, int mid, int right)
{
    int i = left, j = mid + 1, k = left;
    while (i <= mid && j <= right)
        temp[k++] = a[i] <= a[j] ? a[i++] : a[j++];
    while (i <= mid) temp[k++] = a[i++];
    while (j <= right) temp[k++] = a[j++];
    for (i = left; i <= right; ++i) a[i] = temp[i];
}
static void MergeRange(int a[], int temp[], int left, int right)
{
    if (left >= right) return;
    int mid = left + (right - left) / 2;
    MergeRange(a, temp, left, mid);
    MergeRange(a, temp, mid + 1, right);
    Merge(a, temp, left, mid, right);
}
static void MergeSort(int a[], int n)
{
    int *temp = malloc((size_t)n * sizeof *temp);
    if (temp == NULL && n > 0) abort();
    MergeRange(a, temp, 0, n - 1);
    free(temp);
}

static void RadixSort(int a[], int n)
{
    int output[64];
    int max = 0;
    assert(n <= 64);
    for (int i = 0; i < n; ++i) { assert(a[i] >= 0); if (a[i] > max) max = a[i]; }
    for (int exp = 1; max / exp > 0; exp *= 10) {
        int count[10] = {0};
        for (int i = 0; i < n; ++i) ++count[(a[i] / exp) % 10];
        for (int d = 1; d < 10; ++d) count[d] += count[d - 1];
        for (int i = n - 1; i >= 0; --i) { /* 逆向放置保持本趟稳定。 */
            int digit = (a[i] / exp) % 10;
            output[--count[digit]] = a[i];
        }
        memcpy(a, output, (size_t)n * sizeof *a);
        if (exp > max / 10) break; /* 避免 exp *= 10 溢出。 */
    }
}

static void CountingSort(int a[], int n)
{
    if (n < 2) return;
    int min = a[0], max = a[0];
    for (int i = 1; i < n; ++i) { if (a[i] < min) min = a[i]; if (a[i] > max) max = a[i]; }
    int range = max - min + 1;
    int *count = calloc((size_t)range, sizeof *count);
    if (count == NULL) abort();
    for (int i = 0; i < n; ++i) ++count[a[i] - min];
    int k = 0;
    for (int value = min; value <= max; ++value)
        while (count[value - min]-- > 0) a[k++] = value;
    free(count);
}

static void Check(void (*sort)(int *, int), const int source[], int n)
{
    int a[16];
    const int expected[] = {1, 2, 2, 3, 4, 5};
    memcpy(a, source, (size_t)n * sizeof *a);
    sort(a, n);
    assert(memcmp(a, expected, (size_t)n * sizeof *a) == 0);
}
int main(void)
{
    const int source[] = {5, 2, 4, 2, 1, 3};
    Check(MergeSort, source, 6); Check(RadixSort, source, 6); Check(CountingSort, source, 6);
    return 0;
}
