#include <assert.h>
#include <string.h>

static void DirectInsertion(int a[], int n)
{
    for (int i = 1; i < n; ++i) {
        int saved = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > saved) {
            a[j + 1] = a[j];
            --j;
        }
        a[j + 1] = saved; /* a[0..i] 再次有序。 */
    }
}

static void BinaryInsertion(int a[], int n)
{
    for (int i = 1; i < n; ++i) {
        int saved = a[i];
        int low = 0, high = i;
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (a[mid] <= saved) low = mid + 1; /* 插到相等元素之后，保持稳定。 */
            else high = mid;
        }
        for (int j = i; j > low; --j) a[j] = a[j - 1];
        a[low] = saved;
    }
}

static void ShellSort(int a[], int n)
{
    for (int gap = n / 2; gap > 0; gap /= 2) {
        for (int i = gap; i < n; ++i) {
            int saved = a[i], j = i;
            while (j >= gap && a[j - gap] > saved) {
                a[j] = a[j - gap];
                j -= gap;
            }
            a[j] = saved;
        }
    }
}

static void Check(void (*sort)(int *, int))
{
    int a[] = {5, 2, 4, 2, 1, 3};
    const int expected[] = {1, 2, 2, 3, 4, 5};
    sort(a, 6);
    assert(memcmp(a, expected, sizeof a) == 0);
}

int main(void)
{
    Check(DirectInsertion); Check(BinaryInsertion); Check(ShellSort);
    return 0;
}
