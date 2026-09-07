#include <assert.h>
#include <limits.h>

#define K 3
#define RUN_CAP 4

/* tree[0] 保存当前胜者；内部位置保存比较中落败者。 */
static void AdjustLoserTree(int tree[K], const int key[K + 1], int player)
{
    int parent = (player + K) / 2;
    while (parent > 0) {
        if (key[player] > key[tree[parent]]) {
            int loser = player;
            player = tree[parent];
            tree[parent] = loser;
        }
        parent /= 2;
    }
    tree[0] = player;
}

static void InitLoserTree(int tree[K], int key[K + 1])
{
    key[K] = INT_MIN;             /* 虚拟选手保证初始化比较成立。 */
    for (int i = 0; i < K; ++i) tree[i] = K;
    for (int player = K - 1; player >= 0; --player)
        AdjustLoserTree(tree, key, player);
}

static int MergeRuns(const int runs[K][RUN_CAP], const int length[K], int out[K * RUN_CAP])
{
    int pos[K] = {0};
    int key[K + 1];
    int tree[K];
    for (int i = 0; i < K; ++i) key[i] = length[i] > 0 ? runs[i][0] : INT_MAX;
    InitLoserTree(tree, key);
    int n = 0;
    while (key[tree[0]] != INT_MAX) {
        int winner = tree[0];
        out[n++] = key[winner];
        ++pos[winner];
        key[winner] = pos[winner] < length[winner] ? runs[winner][pos[winner]] : INT_MAX;
        AdjustLoserTree(tree, key, winner); /* 只有胜者关键字改变，只沿它到根的路径调整。 */
    }
    return n;
}

/* 归并段长度不等时，总代价最小的归并次序与 Huffman 合并相同。 */
static int OptimalMergeCost(int length[], int n)
{
    int total = 0;
    for (int remaining = n; remaining > 1; --remaining) {
        int first = 0, second = 1;
        if (length[first] > length[second]) { int t = first; first = second; second = t; }
        for (int i = 2; i < remaining; ++i) {
            if (length[i] < length[first]) { second = first; first = i; }
            else if (length[i] < length[second]) second = i;
        }
        int merged = length[first] + length[second];
        total += merged;
        if (first > second) { int t = first; first = second; second = t; }
        length[first] = merged;
        length[second] = length[remaining - 1];
    }
    return total;
}

int main(void)
{
    const int runs[K][RUN_CAP] = {{1, 4, 7, 10}, {2, 5, 8, 0}, {3, 6, 9, 12}};
    const int length[K] = {4, 3, 4};
    int out[K * RUN_CAP];
    int n = MergeRuns(runs, length, out);
    const int expected[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12};
    assert(n == 11);
    for (int i = 0; i < n; ++i) assert(out[i] == expected[i]);
    int lengths[] = {2, 3, 7, 8};
    assert(OptimalMergeCost(lengths, 4) == 37);
    return 0;
}
