#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

/*
 * 图应用代码统一按三种状态来读：
 * 1. 已确定：结果不会再改变；
 * 2. 候选：根据已知信息得到的当前最好值；
 * 3. 未到达：还没有足够信息，常用 INF 表示。
 *
 * Prim 确定生成树顶点，Dijkstra 确定最短距离；
 * Kruskal 确定不会成环的边；拓扑排序确定当前入度为 0 的顶点。
 */
#define MAX_V 8
#define INF 1000000

static int Prim(const int graph[MAX_V][MAX_V], int n)
{
    int low[MAX_V]; /* 每个树外顶点连接当前生成树的最小边权。 */
    bool in_tree[MAX_V] = {false};
    for (int v = 0; v < n; ++v) low[v] = graph[0][v];
    in_tree[0] = true;
    int total = 0;
    for (int count = 1; count < n; ++count) {
        /* 从树外选 low 最小者；它与树的连接现在可以确定。 */
        int next = -1;
        /* 新顶点入树后，可能为其他树外顶点提供更便宜的连接。 */
        for (int v = 0; v < n; ++v)
            if (!in_tree[v] && (next == -1 || low[v] < low[next])) next = v;
        if (next == -1 || low[next] == INF) return -1;
        in_tree[next] = true;
        total += low[next];
        for (int v = 0; v < n; ++v)
            if (!in_tree[v] && graph[next][v] < low[v]) low[v] = graph[next][v];
    }
    return total;
}

typedef struct { int from, to, weight; } Edge;
static int CompareEdge(const void *a, const void *b)
{
    const Edge *x = a, *y = b;
    return (x->weight > y->weight) - (x->weight < y->weight);
}
static int Root(int parent[], int x)
{
    while (parent[x] >= 0) x = parent[x];
    return x;
}
static int Kruskal(Edge edges[], int edge_count, int n)
{
    int parent[MAX_V];
    for (int i = 0; i < n; ++i) parent[i] = -1;
    qsort(edges, (size_t)edge_count, sizeof edges[0], CompareEdge); /* 先按边权递增。 */
    int selected = 0, total = 0;
    for (int i = 0; i < edge_count && selected < n - 1; ++i) {
        int a = Root(parent, edges[i].from), b = Root(parent, edges[i].to);
        if (a == b) continue;        /* 会成环的边跳过。 */
        parent[b] = a;
        total += edges[i].weight;
        ++selected;
    }
    return selected == n - 1 ? total : -1;
}

static void Dijkstra(const int graph[MAX_V][MAX_V], int n, int source, int dist[MAX_V])
{
    bool fixed[MAX_V] = {false};
    for (int v = 0; v < n; ++v) dist[v] = graph[source][v];
    dist[source] = 0;
    for (int count = 0; count < n; ++count) {
        /* 非负边权下，未确定顶点中 dist 最小者不可能再被绕路改小。 */
        int next = -1;
        /* 松弛：尝试用 source -> next -> v 改善当前候选距离。 */
        for (int v = 0; v < n; ++v)
            if (!fixed[v] && (next == -1 || dist[v] < dist[next])) next = v;
        if (next == -1 || dist[next] == INF) break;
        fixed[next] = true;
        for (int v = 0; v < n; ++v)
            if (!fixed[v] && graph[next][v] < INF &&
                dist[next] + graph[next][v] < dist[v])
                dist[v] = dist[next] + graph[next][v];
    }
}

static void Floyd(int dist[MAX_V][MAX_V], int n)
{
    /* 第 k 轮结束后，只使用 0..k 作中间点的最短路已经确定。 */
    for (int k = 0; k < n; ++k)        /* 允许 0..k 作为中间点。 */
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                if (dist[i][k] < INF && dist[k][j] < INF &&
                    dist[i][k] + dist[k][j] < dist[i][j])
                    dist[i][j] = dist[i][k] + dist[k][j];
}

static bool TopologicalOrder(const int dag[MAX_V][MAX_V], int n, int order[MAX_V])
{
    int indegree[MAX_V] = {0};
    int stack[MAX_V], top = 0, count = 0;
    for (int u = 0; u < n; ++u)
        for (int v = 0; v < n; ++v)
            if (dag[u][v] > 0) ++indegree[v];
    for (int v = 0; v < n; ++v)
        if (indegree[v] == 0) stack[top++] = v;
    /* 删除一个入度为 0 的顶点，相当于删除它发出的全部边。 */
    while (top > 0) {
        int u = stack[--top];
        order[count++] = u;
        for (int v = 0; v < n; ++v)
            if (dag[u][v] > 0 && --indegree[v] == 0) stack[top++] = v;
    }
    return count == n;              /* 少于 n 说明存在有向环。 */
}

static int CriticalEdgeCount(const int dag[MAX_V][MAX_V], int n)
{
    int order[MAX_V];
    assert(TopologicalOrder(dag, n, order));
    int earliest[MAX_V] = {0}; /* 事件最早发生时间：沿拓扑序向前取最大。 */
    for (int i = 0; i < n; ++i) {
        int u = order[i];
        for (int v = 0; v < n; ++v)
            if (dag[u][v] > 0 && earliest[u] + dag[u][v] > earliest[v])
                earliest[v] = earliest[u] + dag[u][v];
    }
    int duration = 0;
    for (int i = 0; i < n; ++i)
        if (earliest[i] > duration) duration = earliest[i];
    int latest[MAX_V];         /* 事件最迟发生时间：沿逆拓扑序向后取最小。 */
    for (int i = 0; i < n; ++i) latest[i] = duration;
    for (int i = n - 1; i >= 0; --i) {
        int u = order[i];
        for (int v = 0; v < n; ++v)
            if (dag[u][v] > 0 && latest[v] - dag[u][v] < latest[u])
                latest[u] = latest[v] - dag[u][v];
    }
    int critical = 0;
    for (int u = 0; u < n; ++u)
        for (int v = 0; v < n; ++v)
            /* 活动最早开始 == 最迟开始，说明没有机动时间。 */
            if (dag[u][v] > 0 && earliest[u] == latest[v] - dag[u][v]) ++critical;
    return critical;
}

int main(void)
{
    /* 同一无向网分别交给 Prim、Kruskal 和最短路算法，便于对照状态含义。 */
    int g[MAX_V][MAX_V];
    for (int i = 0; i < MAX_V; ++i)
        for (int j = 0; j < MAX_V; ++j) g[i][j] = i == j ? 0 : INF;
    const Edge base[] = {{0,1,2},{0,2,3},{1,2,1},{1,3,4},{2,3,2}};
    Edge edges[5];
    for (int i = 0; i < 5; ++i) {
        edges[i] = base[i];
        g[base[i].from][base[i].to] = g[base[i].to][base[i].from] = base[i].weight;
    }
    assert(Prim((const int (*)[MAX_V])g, 4) == 5);
    assert(Kruskal(edges, 5, 4) == 5);
    int dist[MAX_V];
    Dijkstra((const int (*)[MAX_V])g, 4, 0, dist);
    assert(dist[3] == 5);
    Floyd(g, 4);
    assert(g[0][3] == 5);

    int dag[MAX_V][MAX_V] = {{0}};
    dag[0][1] = 3; dag[0][2] = 2; dag[1][3] = 2; dag[2][3] = 4;
    int order[MAX_V];
    assert(TopologicalOrder((const int (*)[MAX_V])dag, 4, order));
    assert(CriticalEdgeCount((const int (*)[MAX_V])dag, 4) == 2);
    return 0;
}
