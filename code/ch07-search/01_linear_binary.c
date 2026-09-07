#include <assert.h>

/*
 * 本文件对比三种“循环边界”：
 * 哨兵顺序查找把失败位置预先放在 a[0]，循环内无需反复判断越界；
 * 普通折半查找维护闭区间 [low, high]，所以继续条件是 low <= high；
 * lower_bound 维护半开区间 [low, high)，结束时 low 就是插入位置。
 */
/* a[0] 是哨兵，实际元素放在 a[1..n]；失败时返回 0。 */
static int SentinelSearch(int a[], int n, int key)
{
    a[0] = key;
    int i = n;
    while (a[i] != key) --i; /* 不写 i>=1，因为 a[0] 保证循环必停。 */
    return i;
}

static int BinarySearch(const int a[], int n, int key)
{
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == key) return mid;
        if (a[mid] < key) low = mid + 1; /* mid 及左侧都不可能。 */
        else high = mid - 1;             /* mid 及右侧都不可能。 */
    }
    return -1;
}

/* 找第一个 >= key 的位置，展示折半边界怎样改变。 */
static int LowerBound(const int a[], int n, int key)
{
    /* 不变量：答案始终位于 [low, high]，high 可以等于 n。 */
    int low = 0, high = n;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (a[mid] < key) low = mid + 1; /* mid 太小，答案严格在右边。 */
        else high = mid;                 /* mid 可能正是第一个合格位置。 */
    }
    return low;
}

int main(void)
{
    /* 命中、失败、精确下界和不存在值的插入位置都分别验证。 */
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
