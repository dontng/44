#include <assert.h>
#include <string.h>

/*
 * 本文件把 BF 与 KMP 放在一起，方便观察唯一关键差别：
 * 失配后 BF 更换起点并重新比较；KMP 保持主串游标 i 不回退，
 * 只利用模式串自己的前后缀信息移动 j。
 *
 * 返回值统一为匹配起点的 0 基下标，-1 表示失败。
 * KMP 采用 next[0] = -1 的版本；遇到别的教材写法，应先核对定义。
 */
static int BruteForce(const char *text, const char *pattern)
{
    int n = (int)strlen(text);
    int m = (int)strlen(pattern);
    /* start 是本轮假设的匹配起点；每次失败后 start 只右移一格。 */
    for (int start = 0; start <= n - m; ++start) {
        int j = 0;
        while (j < m && text[start + j] == pattern[j])
            ++j;
        if (j == m)
            return start;
    }
    return -1;
}

/* 0 基版本：next[j] 表示 pattern[j] 失配后，j 应回到哪里。 */
static void BuildNext(const char *pattern, int next[])
{
    int j = 0;
    int k = -1;
    next[0] = -1;
    int m = (int)strlen(pattern);
    /*
     * 已知 next[0..j]。k 表示当前可复用前缀的长度，
     * 比较 pattern[j] 与 pattern[k] 来推导 next[j+1]。
     */
    while (j < m - 1) {
        if (k == -1 || pattern[j] == pattern[k]) {
            ++j;
            ++k;
            next[j] = k;
        } else {
            k = next[k]; /* 模式串自己利用已知前后缀继续匹配。 */
        }
    }
}

static int KmpSearch(const char *text, const char *pattern)
{
    int n = (int)strlen(text);
    int m = (int)strlen(pattern);
    if (m == 0)
        return 0;
    int next[128];
    assert(m <= (int)(sizeof next / sizeof next[0]));
    BuildNext(pattern, next);
    int i = 0, j = 0;
    /* 循环开始时，text[i-j..i-1] 已与 pattern[0..j-1] 匹配。 */
    while (i < n && j < m) {
        if (j == -1 || text[i] == pattern[j]) {
            ++i;
            ++j;
        } else {
            j = next[j]; /* 丢掉不可能成功的前缀，主串 i 不回退。 */
        }
    }
    return j == m ? i - m : -1;
}

int main(void)
{
    const char *text = "ababcabcacbab";
    const char *pattern = "abcac";
    int next[5];
    /* next 数组和最终匹配位置分开检查，避免“碰巧搜对”掩盖构造错误。 */
    BuildNext(pattern, next);
    const int expected[5] = {-1, 0, 0, 0, 1};
    for (int i = 0; i < 5; ++i)
        assert(next[i] == expected[i]);
    assert(BruteForce(text, pattern) == 5);
    assert(KmpSearch(text, pattern) == 5);
    assert(KmpSearch(text, "xyz") == -1);
    return 0;
}
