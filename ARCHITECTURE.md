# 项目地图

## 当前学习链

[真题题单](src/README.md)与相邻的 `MMDD-answer.md` 是唯一真题教学主线。[计网每日一题](daily-network/README.md)是补充训练；[代码](code/README.md)用于追踪和实现，不额外制造一套必读课程。解析生产完成不等于个人掌握。

## 保留的基础

| 路径 | 职责 |
| --- | --- |
| `src/` | 59份题单、59份教学稿与少量已完成的专项验收 |
| `src/answer-quality/` | 真实教学纠偏、质量约束、已教能力账本 |
| `src/pdf/` | 59份题单PDF；题面不重复裁剪 |
| `daily-network/` | 原视频题图、来源、解析与闭卷复盘 |
| `code/` | 27个独立C程序；用 `bash code/check.sh` 验证样例 |
| `bank/` | 680张选择题图、119张完整大题图；不能移动导致引用断裂 |
| `past_papers/` | 原卷，校验题面与裁图的依据 |
| `data/ability_lines.json`、`question_chain.json` | 选择题归类与编译后题链 |
| `data/written_lines.json`、`written_chain.json` | 完整大题归类与题链 |
| `data/written_markers.json`等 | 大题边界、历史题图来源与裁图审计 |
| `data/answers/`、`results/`、`progress/` | 历史作答证据；不覆盖，不据此假定当前掌握 |
| `data/reference/answers/` | 选择题参考答案；2025年文件仍标待核，不能冒充官方复核 |
| `data/rosters/` | 构建所得题号清单及历史题单，保留来源关系 |
| `tools/`、`tests/` | 内容构建和必要校验；不是用户的学习任务 |

## 历史内容

`navigator/`、`draft/` 在 [archive/pre-review-20261004](https://github.com/dontng/44/tree/archive/pre-review-20261004) 保留原貌，当前分支不再执行其中的计划。旧TLDR解析保留用于查证首次作答、旧解释与验证，不再承担现行规范。

题链索引和页面有人工作业，重建工具必须保护已有入口与手工内容。普通学习不需要重建题库、切图或重新导出全部PDF；只有对应材料改变时才处理必要输出。
