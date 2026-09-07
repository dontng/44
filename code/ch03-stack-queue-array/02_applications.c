#include <assert.h>
#include <stdbool.h>
#include <ctype.h>

#define CAP 64

static bool BracketsMatch(const char *text)
{
    char stack[CAP];
    int top = 0; /* 指向下一个可写位置。 */
    for (; *text != '\0'; ++text) {
        if (*text == '(' || *text == '[' || *text == '{') {
            if (top == CAP)
                return false;
            stack[top++] = *text;
        } else if (*text == ')' || *text == ']' || *text == '}') {
            if (top == 0)
                return false;
            char left = stack[--top];
            if ((*text == ')' && left != '(') || (*text == ']' && left != '[') ||
                (*text == '}' && left != '{'))
                return false;
        }
    }
    return top == 0;
}

/* 为突出出栈次序，只处理一位非负整数和四则运算。 */
static bool EvalPostfix(const char *expr, int *result)
{
    int stack[CAP];
    int top = 0;
    for (; *expr != '\0'; ++expr) {
        if (isspace((unsigned char)*expr))
            continue;
        if (isdigit((unsigned char)*expr)) {
            stack[top++] = *expr - '0';
            continue;
        }
        if (top < 2)
            return false;
        int right = stack[--top];
        int left = stack[--top];
        if (*expr == '+') stack[top++] = left + right;
        else if (*expr == '-') stack[top++] = left - right;
        else if (*expr == '*') stack[top++] = left * right;
        else if (*expr == '/' && right != 0) stack[top++] = left / right;
        else return false;
    }
    if (top != 1)
        return false;
    *result = stack[0];
    return true;
}

static int Priority(char op)
{
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

static bool InfixToPostfix(const char *infix, char postfix[CAP])
{
    char operators[CAP];
    int top = 0, out = 0;
    for (; *infix != '\0'; ++infix) {
        if (isspace((unsigned char)*infix)) continue;
        if (isalnum((unsigned char)*infix)) {
            postfix[out++] = *infix;
        } else if (*infix == '(') {
            operators[top++] = *infix;
        } else if (*infix == ')') {
            while (top > 0 && operators[top - 1] != '(')
                postfix[out++] = operators[--top];
            if (top == 0) return false;
            --top; /* 左括号只控制边界，不进入后缀表达式。 */
        } else if (Priority(*infix) > 0) {
            while (top > 0 && Priority(operators[top - 1]) >= Priority(*infix))
                postfix[out++] = operators[--top];
            operators[top++] = *infix;
        } else {
            return false;
        }
    }
    while (top > 0) {
        if (operators[top - 1] == '(') return false;
        postfix[out++] = operators[--top];
    }
    postfix[out] = '\0';
    return true;
}

/* 无权图的距离就是 BFS 层数；队列保存已发现但尚未展开的顶点。 */
static void UnweightedDistance(const int graph[5][5], int start, int distance[5])
{
    int queue[5];
    int front = 0, rear = 0;
    for (int i = 0; i < 5; ++i)
        distance[i] = -1;
    distance[start] = 0;
    queue[rear++] = start;
    while (front < rear) {
        int v = queue[front++];
        for (int w = 0; w < 5; ++w) {
            if (graph[v][w] && distance[w] == -1) {
                distance[w] = distance[v] + 1;
                queue[rear++] = w;
            }
        }
    }
}

int main(void)
{
    assert(BracketsMatch("a*(b+[c])"));
    assert(!BracketsMatch("([)]"));
    int value = 0;
    assert(EvalPostfix("82/3-", &value) && value == 1);
    char postfix[CAP];
    assert(InfixToPostfix("(a+b)*c", postfix));
    assert(postfix[0] == 'a' && postfix[1] == 'b' && postfix[2] == '+' &&
           postfix[3] == 'c' && postfix[4] == '*' && postfix[5] == '\0');
    const int graph[5][5] = {
        {0, 1, 1, 0, 0}, {1, 0, 0, 1, 0}, {1, 0, 0, 0, 0},
        {0, 1, 0, 0, 1}, {0, 0, 0, 1, 0}
    };
    int distance[5];
    UnweightedDistance(graph, 0, distance);
    assert(distance[0] == 0 && distance[3] == 2 && distance[4] == 3);
    return 0;
}
