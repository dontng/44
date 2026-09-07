#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

#define MAX_V 8

typedef struct {
    int vertex_count;
    bool directed;
    int edge[MAX_V][MAX_V];
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
    int to;
    int weight;
    struct ArcNode *next;
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
