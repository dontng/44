#!/usr/bin/env bash
set -euo pipefail

code_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
lesson_cc="${CC:-cc}"

if ! command -v "$lesson_cc" >/dev/null 2>&1; then
    printf '未找到 C 编译器：%s\n' "$lesson_cc" >&2
    exit 127
fi

lesson_tmp="$(mktemp -d)"
trap 'rm -rf -- "$lesson_tmp"' EXIT
lesson_flags=(-std=c11 -Wall -Wextra -Wpedantic -Werror -UNDEBUG)
lesson_count=0

while IFS= read -r lesson_source; do
    lesson_name="${lesson_source#"$code_root/"}"
    lesson_binary="$lesson_tmp/${lesson_name//\//_}"
    lesson_binary="${lesson_binary%.c}"
    "$lesson_cc" "${lesson_flags[@]}" "$lesson_source" -o "$lesson_binary"
    "$lesson_binary"
    lesson_count=$((lesson_count + 1))
done < <(find "$code_root" -mindepth 2 -type f -name '*.c' | sort)

printf 'PASS: compiled and ran %d data-structure lessons\n' "$lesson_count"
