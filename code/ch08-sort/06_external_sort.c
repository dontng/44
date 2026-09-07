#include <assert.h>
#include <limits.h>

/*
 * 外部排序处理的数据放不进内存，通常先形成多个有序归并段，再多路归并。
 * 本文件不模拟磁盘，只保留两个决定 I/O 次数的核心机制：
 *
 * 败者树：K 路当前关键字比赛，tree[0] 保存最小者；输出一路的新值后，
 *         只需沿该选手到根的路径重新比赛，选择下一个最小值为 O(log K)。
 * 最优归并树：较短归并段优先合并，减少所有记录被重复读写的总次数。
 */
#define K 3
#define RUN_CAP 4

/* tree[0] 保存当前胜者；内部位置保存比较中落败者。 */
static void AdjustLoserTree(int tree[K], const int key[K + 1], int player)
{
    /* player 是本轮关键字发生变化的归并路，从它的叶位置向根比较。 */
    int parent = (player + K) / 2;
    while (parent > 0) {
        if (key[player] > key[tree[parent]]) {
            /* 较大者落败并留在内部结点，较小者继续向上比赛。 */
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
    /* 让每个真实选手依次从叶走到根，最终 tree[0] 得到全局最小者。 */
    for (int player = K - 1; player >= 0; --player)
        AdjustLoserTree(tree, key, player);
}

static int MergeRuns(const int runs[K][RUN_CAP], const int length[K], int out[K * RUN_CAP])
{
    int pos[K] = {0}; /* 每一路下一个尚未输出元素的位置。 */
    int key[K + 1];   /* key[i] 是第 i 路当前参加比赛的元素。 */
    int tree[K];
    for (int i = 0; i < K; ++i) key[i] = length[i] > 0 ? runs[i][0] : INT_MAX;
    InitLoserTree(tree, key);
    int n = 0;
    while (key[tree[0]] != INT_MAX) {
        int winner = tree[0];
        out[n++] = key[winner]; /* 全局最小者进入最终有序输出。 */
        ++pos[winner];
        key[winner] = pos[winner] < length[winner] ? runs[winner][pos[winner]] : INT_MAX;
        AdjustLoserTree(tree, key, winner); /* 只有胜者关键字改变，只沿它到根的路径调整。 */
    }
    return n;
}

/* 归并段长度不等时，总代价最小的归并次序与 Huffman 合并相同。 */
static int OptimalMergeCost(int length[], int n)
{
    /* 每轮找最短两段；它们的和既是新段长度，也是本轮读写代价。 */
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
    /* 三路长度不等，归并结果故意缺少 11，防止只按连续整数误判。 */
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
