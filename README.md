# 408-from-44

> 服务于考研总分 350 冲击中的 408 提分。当前主线：把 2009–2025 年真题组织成能够恢复上下文的能力线，再用 TLDR 完成解析、纠错和迁移验证。

仓库各目录的定位、当前状态和可点击入口见 [项目地图](ARCHITECTURE.md)。

数据结构代码入口：[408 数据结构代码地图](code/README.md)。`ch02—ch08` 已按王道小节建立可运行的 C 实现，用章节覆盖表、动作解释、变体推导和断言检查训练读代码、改代码和写代码。

## 两个层次

题单与解析严格分开：

```text
src/MMDD.md                         能力线题单
tldr/sessions/YYYY-MM/MMDD-tldr.md TLDR 解析与验证
```

`src/` 是学习对象。`0731.md` 至 `0908.md` 是已经封口的 40 条选择题能力线；`0914.md` 起是大题训练线。日期只是链表节点，不是等长配额。选择题按稳定机制归类，大题以不可拆分的完整题为单位，按相同或相通的解题动作成组。

`tldr/` 是原 `speedrun/` 的完整更名。它保留真实首次作答、独立诊断、最小闭合机制、全部选项裁决和可证伪验证，不承担题单存放职责。

## 使用

```bash
./today.sh 0731       # 显示 src/0731.md 对应的能力线和题目
./answer.sh 0731      # 启动该节点答题卡
./tldr.sh 0731        # 从判分结果生成 tldr/sessions/.../0731-tldr.md
./tldr.sh --check 0731
python3 tools/build_written_chain.py          # 重建 0914 起的大题线
python3 tools/slice_written_papers.py --check # 校验 119 个大题题图槽位
python3 tools/build_written_chain.py --check  # 校验题图、唯一主归类和节点
python3 tools/recover_written_questions.py --check  # 核对题图与历史裁剪像素一致
```

完整能力线入口是 [src/README.md](src/README.md)。题单已经一次性生成，`today.sh` 不再临时抽题。

## 关键文件

| 路径 | 作用 |
|---|---|
| `data/ability_lines.json` | 40 条能力线、故事梗概和题目归属 |
| `data/question_chain.json` | 编译后的日期、前驱、后继和文件路径 |
| `data/written_markers.json` | 2009—2025 年大题边界和 15 张历史保留题图 |
| `data/written_historical_seeds.json` | 15 张历史题图的 Git commit 与裁剪来源 |
| `data/written_lines.json` | 119 道完整大题的唯一主归类 |
| `data/written_chain.json` | 编译后的大题日期、前驱、后继和文件路径 |
| `src/MMDD.md` | 人看的能力线题单 |
| `data/rosters/MMDD.json` | 答题卡读取的机器题单 |
| `tldr/README.md` | TLDR 执行协议与质量门槛 |
| `tldr/TEMPLATE.md` | 每题不可降级的解析骨架 |
| `tldr/sessions/YYYY-MM/MMDD-tldr.md` | 完整解析与验证 |
| `tools/build_question_chain.py` | 生成并校验整条能力线链 |
| `tools/build_written_chain.py` | 生成并校验 0914 起的大题线 |
| `tools/slice_written_papers.py` | 按相邻题号边界切图并自动拼接跨页题 |
| `tools/recover_written_questions.py` | 直接从记录的 Git commit 恢复完整大题图 |

## 完整性

- 2009–2025 年 680 道选择题全部至少归入一条能力线。
- 40 条能力线对应 40 个连续日期节点。
- 题目在每条能力线内按年份递增。
- 24 道跨机制接口题会在两条或三条能力线中出现；第二次出现只检查接口，不计作新的刷题配额。
- 大题库覆盖 2009—2025 年每年的 41—47 题，共 119 道。15 张已经从 Git 历史确认的题图原样保留，其余题按相邻题号闭合并自动拼接跨页内容；每题只进入一个主组，编成 19 条线、119 次引用。
- 原等长日题单和动态调度系统已经切出当前主线；需要追溯时请查阅 Git 历史。

TLDR 的状态仍只描述证据强度：

```text
diagnosed → grounded → explained → verified → transferred → automatic
```
