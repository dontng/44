#include <assert.h>

/* a[0] 是哨兵，实际元素放在 a[1..n]；失败时返回 0。 */
static int SentinelSearch(int a[], int n, int key)
{
    a[0] = key;
    int i = n;
    while (a[i] != key) --i; /* 必然会在真实元素或哨兵处停下。 */
    return i;
}

static int BinarySearch(const int a[], int n, int key)
{
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == key) return mid;
        if (a[mid] < key) low = mid + 1;
        else high = mid - 1;
    }
    return -1;
}

/* 找第一个 >= key 的位置，展示折半边界怎样改变。 */
static int LowerBound(const int a[], int n, int key)
{
    int low = 0, high = n;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (a[mid] < key) low = mid + 1;
        else high = mid;
    }
    return low;
}

int main(void)
{
    int sentinel[] = {0, 4, 8, 15, 16, 23, 42};
    assert(SentinelSearch(sentinel, 6, 15) == 3);
    assert(SentinelSearch(sentinel, 6, 99) == 0);
    const int sorted[] = {4, 8, 15, 16, 23, 42};
    assert(BinarySearch(sorted, 6, 16) == 3);
    assert(BinarySearch(sorted, 6, 9) == -1);
    assert(LowerBound(sorted, 6, 16) == 3);
    assert(LowerBound(sorted, 6, 17) == 4);
    return 0;
}
