#!/usr/bin/env bash
set -euo pipefail
lesson_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
lesson_cc="${CC:-cc}"
lesson_name="${1:-help}"
case "$lesson_name" in
    help|-h|--help)
        printf '%s\n' '选择一个问题：' \
            '  definition   结点、表头和空表是什么关系？' \
            '  move         移动指针会改变链表吗？' \
            '  insert       插入为什么先接后继？' \
            '  insert-wrong 交换两句插入代码，观察失败（退出码1）' \
            '  delete       首位和末位删除怎样统一？' \
            '  demo         查看完整增删改查示例' \
            '  check        维护者回归检查'
        exit 0 ;;
    definition|move|insert|insert-wrong|delete|demo|check) ;;
    *) printf '未知实验：%s；不带参数运行可查看入口。\n' "$lesson_name" >&2; exit 2 ;;
esac
if ! command -v "$lesson_cc" >/dev/null 2>&1; then
    printf '未找到C编译器%s；需要cc、gcc或clang（可用CC指定）。也可先阅读LESSON.md的预期结果。\n' "$lesson_cc" >&2
    exit 127
fi
lesson_tmp="$(mktemp -d)"
trap 'rm -rf -- "$lesson_tmp"' EXIT
lesson_flags=(-std=c11 -Wall -Wextra -Wpedantic -Werror -UNDEBUG)
case "$lesson_name" in
    demo) lesson_sources=("$lesson_root/demo.c" "$lesson_root/linked_list.c") ;;
    check) lesson_sources=("$lesson_root/test_linked_list.c" "$lesson_root/linked_list.c") ;;
    insert-wrong)
        lesson_sources=("$lesson_root/experiments/insert.c")
        lesson_flags+=(-DWRONG_ORDER) ;;
    *) lesson_sources=("$lesson_root/experiments/$lesson_name.c") ;;
esac
"$lesson_cc" "${lesson_flags[@]}" "${lesson_sources[@]}" -o "$lesson_tmp/run"
"$lesson_tmp/run"
