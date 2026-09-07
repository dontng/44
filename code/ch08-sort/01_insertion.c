#include <assert.h>
#include <string.h>

/*
 * 插入类排序的共同视角：左边是已经有序的序列，右边是尚未处理的元素。
 * 每一趟取出一个待排元素 saved，在左侧寻找位置并把它插进去。
 *
 * 直接插入逐个比较；折半插入只减少比较次数，元素搬移量没有减少；
 * 希尔排序先让相距 gap 的元素局部有序，最后以 gap=1 收束。
 */
static void DirectInsertion(int a[], int n)
{
    for (int i = 1; i < n; ++i) {
        int saved = a[i]; /* 先保存待插元素，右移时才不会把它覆盖。 */
        int j = i - 1;
        /* 循环开始时 a[j+1..i] 已右移，正在为 saved 扩大空位。 */
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
        int low = 0, high = i; /* 在有序前缀的半开区间 [0,i) 找插入点。 */
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (a[mid] <= saved) low = mid + 1; /* 插到相等元素之后，保持稳定。 */
            else high = mid;
        }
        /* 折半只找到了位置，腾位仍需线性搬移。 */
        for (int j = i; j > low; --j) a[j] = a[j - 1];
        a[low] = saved;
    }
}

static void ShellSort(int a[], int n)
{
    /* gap 逐渐缩小；同一余数类中的元素构成一组插入排序。 */
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
    /* 三种算法处理同一组含重复值的数据，统一核对最终序列。 */
    Check(DirectInsertion); Check(BinaryInsertion); Check(ShellSort);
    return 0;
}
