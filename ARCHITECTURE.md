# 项目地图

## 当前学习链

从[真题题单](src/README.md)开始，按当前要求独立解题。`src/answer/` 与 `src/answer-quality/` 为可选参考存档，代理默认不读、不检索；仅在用户明确要求或同意提议后参考指定内容。[计网每日一题](daily-network/README.md)是补充训练（2026年待观望）；[代码](code/README.md)用于追踪和实现，不额外制造一套必读课程。解析生产完成不等于个人掌握。

## 保留的基础

| 路径 | 职责 |
| --- | --- |
| `src/` | 59份题单；原有解析与专项材料集中保存在 `answer/` |
| `src/answer/` | 旧解析、专项材料与写作规则存档；默认不读取或用于评判新稿 |
| `src/answer-quality/` | 旧教学结论与上下文存档；保留但不作为默认约束 |
| `plan/` | 40天多学科并行冲刺计划、全景题单映射、大题前置介入与三阶段课表（含 65 天归档） |
| `27outline.md` | 2027年408考试大纲原文与层级结构 |
| `daily-network/` | 2026年每日一题原视频题图与解析（观望中） |
| `code/` | 27个独立C程序；用 `bash code/check.sh` 验证样例 |
| `bank/` | 680张选择题图、119张完整大题图；不能移动导致引用断裂 |
| `past_papers/` | 原卷，校验题面与裁图的依据 |
| `data/ability_lines.json`、`question_chain.json` | 选择题归类与编译后题链 |
| `data/written_lines.json`、`written_chain.json` | 完整大题归类与题链 |
| `data/written_markers.json`等 | 大题边界、历史题图来源与裁图审计 |
| `data/answers/`、`results/`、`progress/` | 历史作答证据；不覆盖，不据此假定当前掌握 |
| `data/reference/answers/` | 选择题参考答案；2025年文件仍标待核，不能冒充官方复核 |
| `data/rosters/` | 构建所得题号清单及历史题单，保留来源关系 |
| `tools/`、`tests/` | 核心内容构建和必要校验；不是用户的学习任务 |

## 历史归档与清理

以下半途而废、过度工程或未启用的历史内容已彻底移出当前工作树，完整保存在 Git 历史中：
- `draft/` 与 `navigator/`：在分支 `archive/pre-review-20261004` 及提交历史中保留原貌。
- `review/` 及相关调度脚本（`tools/review.py`、`tools/build_review.py`、`tools/check_review.py`、`tests/test_review.py`、`data/review_prompts.json`、`data/network_lessons.json`、`data/review_events/`）：荒废的复盘卡片系统。
- `paper_html/`：HTML 字体与排版复刻实验。
- `tldr/`：7月早期教学记录。
- `src/gpt/`：题单备份副本。
- `src/0731_gemini.md` 与 `src/408_深度研题与AI思维建模协议.md`：未推广的单日 Prompt 实验。
- `daily-network/2025/`：2025年计网题目。
- 10月历史切图与 PDF 审计过程废料。

## 当前任务边界

内容入口已收束。接下来以真实作答推进当前真题线，把错误断点带回对应解析；不再另写草稿课程或分散精力搞排版工程。参考答案2025文件的待核状态继续保留，不能擅自升级。
