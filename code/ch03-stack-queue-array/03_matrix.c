#include <assert.h>
#include <stdlib.h>

static int RowMajorIndex(int i, int j, int cols) { return i * cols + j; }
static int ColumnMajorIndex(int i, int j, int rows) { return j * rows + i; }

static int SymmetricIndex(int i, int j)
{
    int row = i > j ? i : j; /* 把上三角坐标折到已保存的下三角。 */
    int col = i > j ? j : i;
    return row * (row + 1) / 2 + col;
}

/* n 阶下三角矩阵按行保存；上三角的共同常量放在最后一格。 */
static int LowerTriangularIndex(int i, int j, int n)
{
    return i >= j ? i * (i + 1) / 2 + j : n * (n + 1) / 2;
}

/* 0 基、按行保存三对角非零元；不在带内返回 -1。 */
static int TridiagonalIndex(int i, int j, int n)
{
    if (i < 0 || j < 0 || i >= n || j >= n || abs(i - j) > 1)
        return -1;
    return 2 * i + j;
}

typedef struct {
    int row;
    int col;
    int value;
} Triple;
typedef struct {
    int rows;
    int cols;
    int terms;
    Triple data[16];
} SparseMatrix;

static void FastTranspose(const SparseMatrix *a, SparseMatrix *b)
{
    int count[16] = {0};
    int start[16] = {0};
    b->rows = a->cols;
    b->cols = a->rows;
    b->terms = a->terms;
    for (int k = 0; k < a->terms; ++k)
        ++count[a->data[k].col];
    for (int col = 1; col < a->cols; ++col)
        start[col] = start[col - 1] + count[col - 1];
    for (int k = 0; k < a->terms; ++k) {
        int col = a->data[k].col;
        int pos = start[col]++;
        b->data[pos] = (Triple){a->data[k].col, a->data[k].row, a->data[k].value};
    }
}

int main(void)
{
    assert(RowMajorIndex(2, 1, 4) == 9);
    assert(ColumnMajorIndex(2, 1, 3) == 5);
    assert(SymmetricIndex(3, 1) == 7);
    assert(SymmetricIndex(1, 3) == 7);
    assert(LowerTriangularIndex(3, 1, 4) == 7);
    assert(LowerTriangularIndex(1, 3, 4) == 10);
    assert(TridiagonalIndex(0, 0, 4) == 0);
    assert(TridiagonalIndex(1, 2, 4) == 4);
    assert(TridiagonalIndex(0, 2, 4) == -1);

    SparseMatrix a = {3, 4, 4, {{0, 1, 5}, {1, 0, 2}, {1, 3, 7}, {2, 1, 9}}};
    SparseMatrix b;
    FastTranspose(&a, &b);
    assert(b.rows == 4 && b.cols == 3 && b.terms == 4);
    assert(b.data[0].row == 0 && b.data[0].col == 1 && b.data[0].value == 2);
    assert(b.data[1].row == 1 && b.data[1].col == 0 && b.data[1].value == 5);
    return 0;
}
