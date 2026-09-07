#!/usr/bin/env bash
set -euo pipefail

lesson_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
lesson_cc="${CC:-cc}"

if ! command -v "$lesson_cc" >/dev/null 2>&1; then
    printf '未找到 C 编译器：%s\n' "$lesson_cc" >&2
    exit 127
fi

lesson_tmp="$(mktemp -d)"
trap 'rm -rf -- "$lesson_tmp"' EXIT

lesson_flags=(-std=c11 -Wall -Wextra -Wpedantic -Werror -UNDEBUG)

for lesson_source in sequential_list singly_linked_list; do
    "$lesson_cc" "${lesson_flags[@]}" \
        "$lesson_root/${lesson_source}.c" \
        -o "$lesson_tmp/$lesson_source"
    "$lesson_tmp/$lesson_source"
done

puts_result='PASS: all linear-list checks'
printf '%s\n' "$puts_result"
