# src 题链 PDF

本目录保存 `src/0731.md` 至 `src/1002.md` 的逐文件 PDF 导出版。

- 每个日期 Markdown 对应一个同名 PDF。
- 概览页保留能力线/大题线说明与故事梗概或归类依据。
- 每道题独立成页，题图只做等比缩放，不裁剪、不重新压缩文字内容。
- PDF 书签与题目顺序一致，便于在长题链中直接跳转。

重新生成全部 PDF：

```bash
"$CODEX_PRIMARY_RUNTIME_PYTHON" tools/export_src_pdfs.py
```

只预览某一天：

```bash
"$CODEX_PRIMARY_RUNTIME_PYTHON" tools/export_src_pdfs.py --only 0731
```

脚本优先使用 `--font` 或 `SRC_PDF_CJK_FONT` 指定的中文 TrueType 字体；未指定且系统中没有可用字体时，会把 Noto Sans SC 缓存到 `tmp/pdfs/fonts/` 后再导出。
