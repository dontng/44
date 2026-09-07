#include <assert.h>
#include <stdbool.h>

#define N 6

static void DfsFrom(const int graph[N][N], int v, bool visited[N], int order[N], int *count)
{
    visited[v] = true;
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
        int front = 0, rear = 0;
        visited[start] = true;       /* 入队时标记，防止重复入队。 */
        queue[rear++] = start;
        while (front < rear) {
            int v = queue[front++];
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
