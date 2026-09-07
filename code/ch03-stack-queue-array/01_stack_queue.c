#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>

/*
 * 本文件把栈和队列的常见存储集中对照。
 *
 * 最先确认的不是函数名，而是游标约定：
 * - SqStack.top 指向当前栈顶，因此空栈为 -1；
 * - CircularQueue.front 指向队头，rear 指向下一个可写位置；
 * - Deque 用 front + size 表示状态，所有下标都通过取模回绕；
 * - LinkQueue.front 指向头结点，rear 指向最后一个数据结点。
 */
#define CAP 8

typedef struct {
    int data[CAP];
    int top; /* 指向当前栈顶；-1 表示空栈。 */
} SqStack;

static void SqStackInit(SqStack *s) { s->top = -1; }
static bool SqPush(SqStack *s, int x)
{
    if (s->top == CAP - 1)
        return false;
    s->data[++s->top] = x; /* top 指当前元素，所以先上移、再写入。 */
    return true;
}
static bool SqPop(SqStack *s, int *x)
{
    if (s->top == -1)
        return false;
    *x = s->data[s->top--]; /* 先读当前栈顶，再让 top 下移。 */
    return true;
}

typedef struct StackNode {
    int data;
    struct StackNode *next;
} StackNode;

static bool LinkPush(StackNode **top, int x)
{
    StackNode *s = malloc(sizeof *s);
    if (s == NULL)
        return false;
    s->data = x;
    s->next = *top; /* 新结点接住旧栈顶。 */
    *top = s;       /* 调用者的 top 改指向新栈顶。 */
    return true;
}
static bool LinkPop(StackNode **top, int *x)
{
    if (*top == NULL)
        return false;
    StackNode *p = *top;
    *x = p->data;
    *top = p->next;
    free(p);
    return true;
}

typedef struct {
    int data[CAP];
    int front; /* 当前队头。 */
    int rear;  /* 下一个可写位置。 */
} CircularQueue;

typedef struct {
    int data[CAP];
    int front;
    int size; /* 显式记录元素数后，双端操作不必牺牲数组格子。 */
} Deque;

static void DequeInit(Deque *q) { q->front = q->size = 0; }
static bool PushFront(Deque *q, int x)
{
    if (q->size == CAP) return false;
    q->front = (q->front - 1 + CAP) % CAP;
    q->data[q->front] = x;
    ++q->size;
    return true;
}
static bool PushBack(Deque *q, int x)
{
    if (q->size == CAP) return false;
    /* 队尾空位位于“队头向后数 size 格”的位置。 */
    q->data[(q->front + q->size) % CAP] = x;
    ++q->size;
    return true;
}
static bool PopFront(Deque *q, int *x)
{
    if (q->size == 0) return false;
    *x = q->data[q->front];
    q->front = (q->front + 1) % CAP;
    --q->size;
    return true;
}
static bool PopBack(Deque *q, int *x)
{
    if (q->size == 0) return false;
    *x = q->data[(q->front + q->size - 1) % CAP];
    --q->size;
    return true;
}

static void CQueueInit(CircularQueue *q) { q->front = q->rear = 0; }
static int CQueueLength(const CircularQueue *q)
{
    return (q->rear - q->front + CAP) % CAP;
}
static bool EnQueue(CircularQueue *q, int x)
{
    if ((q->rear + 1) % CAP == q->front) /* 牺牲一个格子区分空与满。 */
        return false;
    q->data[q->rear] = x;          /* 在 rear 所指空位写入。 */
    q->rear = (q->rear + 1) % CAP;
    return true;
}
static bool DeQueue(CircularQueue *q, int *x)
{
    if (q->front == q->rear)
        return false;
    *x = q->data[q->front];        /* front 所指元素最早入队。 */
    q->front = (q->front + 1) % CAP;
    return true;
}

typedef struct QueueNode {
    int data;
    struct QueueNode *next;
} QueueNode;
typedef struct {
    QueueNode *front; /* 头结点。 */
    QueueNode *rear;  /* 最后一个结点；空时也指向头结点。 */
} LinkQueue;

static bool LinkQueueInit(LinkQueue *q)
{
    q->front = malloc(sizeof *q->front);
    if (q->front == NULL)
        return false;
    q->front->next = NULL;
    q->rear = q->front; /* 空队列时两个指针共同指向头结点。 */
    return true;
}
static bool LinkEnQueue(LinkQueue *q, int x)
{
    QueueNode *s = malloc(sizeof *s);
    if (s == NULL)
        return false;
    s->data = x;
    s->next = NULL;
    q->rear->next = s;
    q->rear = s;
    return true;
}
static bool LinkDeQueue(LinkQueue *q, int *x)
{
    QueueNode *p = q->front->next;
    if (p == NULL)
        return false;
    *x = p->data;
    q->front->next = p->next;
    if (q->rear == p)             /* 删除最后一个数据结点时，rear 不能悬空。 */
        q->rear = q->front;
    free(p);
    return true;
}

int main(void)
{
    /* 每组断言不仅测正常结果，也刻意触发满、回绕和删空边界。 */
    int x = 0;
    SqStack s;
    SqStackInit(&s);
    assert(SqPush(&s, 1) && SqPush(&s, 2));
    assert(SqPop(&s, &x) && x == 2);
    StackNode *top = NULL;
    assert(LinkPush(&top, 3) && LinkPop(&top, &x) && x == 3);

    CircularQueue cq;
    CQueueInit(&cq);
    for (int i = 0; i < CAP - 1; ++i)
        assert(EnQueue(&cq, i));
    assert(!EnQueue(&cq, 99) && CQueueLength(&cq) == CAP - 1);
    assert(DeQueue(&cq, &x) && x == 0);
    assert(EnQueue(&cq, 7));       /* rear 已经取模回绕。 */

    Deque dq;
    DequeInit(&dq);
    assert(PushFront(&dq, 2) && PushFront(&dq, 1) && PushBack(&dq, 3));
    assert(PopFront(&dq, &x) && x == 1);
    assert(PopBack(&dq, &x) && x == 3);

    LinkQueue lq;
    assert(LinkQueueInit(&lq));
    assert(LinkEnQueue(&lq, 10));
    assert(LinkDeQueue(&lq, &x) && x == 10);
    assert(lq.front == lq.rear);
    free(lq.front);
    return 0;
}
