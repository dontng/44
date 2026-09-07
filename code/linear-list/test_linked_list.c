/* 维护者验证；学习入口是 linked_list.c。 */
#define LINKED_LIST_NO_MAIN
#include "linked_list.c"
#include <assert.h>
#include <limits.h>

static void check(LinkList L, const int *expected, int n)
{
    assert(list_length(L) == n);
    assert(list_empty(L) == (n == 0));
    LNode *p = L->next;
    for (int i = 0; i < n; ++i) {
        assert(p != NULL);
        assert(p->data == expected[i]);
        p = p->next;
        int value;
        assert(list_get(L, i + 1, &value));
        assert(value == expected[i]);
    }
    assert(p == NULL);
    int out = 777;
    assert(!list_get(L, 0, &out) && out == 777);
    assert(!list_get(L, n + 1, &out) && out == 777);
}

int main(void)
{
    LinkList L = list_create();
    assert(L != NULL);
    int model[128], n = 0, out = 777;
    check(L, model, n);
    assert(!list_delete(L, 1, &out) && out == 777);
    assert(!list_insert(L, 2, 9));
    assert(!list_insert(L, INT_MIN, 9));
    assert(!list_insert(L, INT_MAX, 9));
    assert(!list_update(L, 1, 9));
    list_clear(L);
    check(L, model, n);

    // 固定种子的连续操作，与顺序数组模型对照，检查完整内容而非只看返回值。
    srand(44);
    for (int step = 0; step < 2000; ++step) {
        int op = rand() % 5;
        int value = rand() % 11 - 5; // 包含 0、负值、重复值。
        if (op == 0 && n < 128) {
            int i = rand() % (n + 1);
            assert(list_insert(L, i + 1, value));
            for (int j = n; j > i; --j)
                model[j] = model[j - 1];
            model[i] = value;
            ++n;
        } else if (op == 1 && n > 0) {
            int i = rand() % n;
            assert(list_delete(L, i + 1, &out));
            assert(out == model[i]);
            for (int j = i; j < n - 1; ++j)
                model[j] = model[j + 1];
            --n;
        } else if (op == 2 && n > 0) {
            int i = rand() % n;
            assert(list_update(L, i + 1, value));
            model[i] = value;
        } else if (op == 3) {
            int first = 0;
            for (int i = 0; i < n; ++i)
                if (model[i] == value) {
                    first = i + 1;
                    break;
                }
            assert(list_find(L, value) == first);
        } else {
            out = 777;
            assert(!list_delete(L, n + 1, &out) && out == 777);
            assert(!list_insert(L, n + 2, value));
            assert(!list_update(L, 0, value));
        }
        check(L, model, n);
    }
    list_clear(L);
    check(L, model, 0);
    assert(list_insert(L, 1, 42));
    assert(list_delete(L, 1, &out) && out == 42);
    check(L, model, 0);
    list_destroy(L);
    L = list_create();
    assert(L != NULL);
    assert(list_insert(L, 1, 1));
    assert(list_insert(L, 2, 2));
    list_destroy(L); // 验证非空表的销毁。
    puts("PASS: boundaries, reuse, 2000 model-checked operations");
    return 0;
}
