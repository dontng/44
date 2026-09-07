#include <assert.h>
#include <string.h>

static int BruteForce(const char *text, const char *pattern)
{
    int n = (int)strlen(text);
    int m = (int)strlen(pattern);
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
    while (i < n && j < m) {
        if (j == -1 || text[i] == pattern[j]) {
            ++i;
            ++j;
        } else {
            j = next[j]; /* 主串 i 不回退。 */
        }
    }
    return j == m ? i - m : -1;
}

int main(void)
{
    const char *text = "ababcabcacbab";
    const char *pattern = "abcac";
    int next[5];
    BuildNext(pattern, next);
    const int expected[5] = {-1, 0, 0, 0, 1};
    for (int i = 0; i < 5; ++i)
        assert(next[i] == expected[i]);
    assert(BruteForce(text, pattern) == 5);
    assert(KmpSearch(text, pattern) == 5);
    assert(KmpSearch(text, "xyz") == -1);
    return 0;
}
