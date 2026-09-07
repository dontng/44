#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

/*
 * 同一张图可以用矩阵或邻接表保存，算法读法取决于“怎样枚举邻接点”。
 *
 * 邻接矩阵：edge[u][v] 直接回答 u 到 v 是否有边，查边 O(1)，空间 O(V²)；
 * 邻接表：first[u] 串起 u 的全部出边，枚举邻接点只访问真实存在的边。
 * 无向边在存储上要写成两个方向，但逻辑上仍只是一条边。
 */
#define MAX_V 8

typedef struct {
    int vertex_count;          /* 实际使用顶点编号 0..vertex_count-1。 */
    bool directed;             /* false 时增边必须同时写反方向。 */
    int edge[MAX_V][MAX_V];    /* 0 表示本例中没有边。 */
} MatrixGraph;

static void MatrixInit(MatrixGraph *g, int n, bool directed)
{
    *g = (MatrixGraph){.vertex_count = n, .directed = directed};
}
static void MatrixAddEdge(MatrixGraph *g, int from, int to, int weight)
{
    g->edge[from][to] = weight;
    if (!g->directed)
        g->edge[to][from] = weight;
}

typedef struct ArcNode {
    int to;                 /* 这条出边到达哪个顶点。 */
    int weight;
    struct ArcNode *next;   /* 同一起点的下一条出边。 */
} ArcNode;
typedef struct {
    int vertex_count;
    bool directed;
    ArcNode *first[MAX_V];
} ListGraph;

static void ListInit(ListGraph *g, int n, bool directed)
{
    *g = (ListGraph){.vertex_count = n, .directed = directed};
}
static void AddOneArc(ListGraph *g, int from, int to, int weight)
{
    ArcNode *arc = malloc(sizeof *arc);
    if (arc == NULL) abort();
    /* 头插不会影响图的正确性，只会改变遍历邻接点的先后次序。 */
    *arc = (ArcNode){to, weight, g->first[from]};
    g->first[from] = arc;
}
static void ListAddEdge(ListGraph *g, int from, int to, int weight)
{
    AddOneArc(g, from, to, weight);
    if (!g->directed)
        AddOneArc(g, to, from, weight);
}
static int OutDegree(const ListGraph *g, int vertex)
{
    int degree = 0;
    for (ArcNode *p = g->first[vertex]; p != NULL; p = p->next)
        ++degree;
    return degree;
}
static void ListDestroy(ListGraph *g)
{
    for (int v = 0; v < g->vertex_count; ++v) {
        ArcNode *p = g->first[v];
        /* 每个链表结点代表一条已分配的弧，必须逐个释放。 */
        while (p != NULL) {
            ArcNode *next = p->next;
            free(p);
            p = next;
        }
        g->first[v] = NULL;
    }
}

int main(void)
{
    /* 同一条无向边在矩阵中对称，在邻接表中出现为两条弧。 */
    MatrixGraph matrix;
    MatrixInit(&matrix, 4, false);
    MatrixAddEdge(&matrix, 0, 2, 7);
    assert(matrix.edge[0][2] == 7 && matrix.edge[2][0] == 7);

    ListGraph list;
    ListInit(&list, 4, false);
    ListAddEdge(&list, 0, 1, 5);
    ListAddEdge(&list, 0, 2, 7);
    assert(OutDegree(&list, 0) == 2 && OutDegree(&list, 1) == 1);
    ListDestroy(&list);
    return 0;
}
