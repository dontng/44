#include <assert.h>
#include <stdbool.h>

/*
 * DFS 与 BFS 都依靠 visited 保证每个顶点只“首次发现”一次。
 * 差别在待处理顶点的保存方式：DFS 沿递归栈深入，BFS 按队列逐层展开。
 * 邻接点按编号从小到大扫描，所以本例访问序列是确定的；换存储顺序后
 * 合法遍历序列可能不同，不能把某一串编号当作唯一答案。
 */
#define N 6

static void DfsFrom(const int graph[N][N], int v, bool visited[N], int order[N], int *count)
{
    visited[v] = true; /* 一进入函数就标记，递归邻点不能再次进入 v。 */
    order[(*count)++] = v;
    for (int w = 0; w < N; ++w)
        if (graph[v][w] && !visited[w])
            DfsFrom(graph, w, visited, order, count);
}

/* 外层循环保证非连通图的每个连通分量也会被访问。 */
static void Dfs(const int graph[N][N], int order[N])
{
    bool visited[N] = {false};
    int count = 0;
    for (int v = 0; v < N; ++v)
        if (!visited[v])
            DfsFrom(graph, v, visited, order, &count);
}

static void Bfs(const int graph[N][N], int order[N])
{
    bool visited[N] = {false};
    int queue[N];
    int count = 0;
    for (int start = 0; start < N; ++start) {
        if (visited[start]) continue;
        int front = 0, rear = 0; /* 每个连通分量使用一段新的线性队列。 */
        visited[start] = true;       /* 入队时标记，防止重复入队。 */
        queue[rear++] = start;
        while (front < rear) {
            int v = queue[front++]; /* v 已发现，现在正式展开它的邻接点。 */
            order[count++] = v;
            for (int w = 0; w < N; ++w) {
                if (graph[v][w] && !visited[w]) {
                    visited[w] = true;
                    queue[rear++] = w;
                }
            }
        }
    }
}

int main(void)
{
    /* 0..3 与 4..5 是两个分量，验证外层循环没有漏掉非连通部分。 */
    const int graph[N][N] = {
        {0, 1, 1, 0, 0, 0}, {1, 0, 0, 1, 0, 0}, {1, 0, 0, 0, 0, 0},
        {0, 1, 0, 0, 0, 0}, {0, 0, 0, 0, 0, 1}, {0, 0, 0, 0, 1, 0}
    };
    int dfs[N], bfs[N];
    Dfs(graph, dfs);
    Bfs(graph, bfs);
    const int expected_dfs[N] = {0, 1, 3, 2, 4, 5};
    const int expected_bfs[N] = {0, 1, 2, 3, 4, 5};
    for (int i = 0; i < N; ++i) {
        assert(dfs[i] == expected_dfs[i]);
        assert(bfs[i] == expected_bfs[i]);
    }
    return 0;
}
