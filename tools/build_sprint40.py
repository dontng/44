"""Build only the already-authored daily routes and standalone teaching modules.

Only sprint40 is written. src, archived answers and historical attempts are never read
for explanations or modified. Question images are referenced, not regenerated.
"""
import json
import re
from pathlib import Path
from format_q_img import get_image_tag

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'sprint40'


def load_questions(node, first_only=True):
    text = (ROOT / 'src' / f'{node}.md').read_text()
    if first_only:
        text = text.split('## 二、')[0]
    result = []
    for number, year, q in re.findall(r'^### (\d+)\s*·\s*(\d{4})-(\d+)', text, re.M):
        result.append((number, f'{year}-{int(q):02d}'))
    return result


def image(qid, prefix='../../', alt=None):
    year, q = qid.split('-')
    return get_image_tag(year, q, alt_text=alt or qid, prefix=prefix)


def fold(title, body):
    return f'<details>\n<summary>{title}</summary>\n\n{body.strip()}\n\n</details>\n'


def build():
    modules = json.loads((OUT / 'content' / 'modules.json').read_text())
    for node, item in modules.items():
        questions = load_questions(node)
        assert [q for _, q in questions] == list(item['answers']), node
        text = f"# {node}｜{item['title']}\n\n"
        if item.get('delivery') == 'standalone':
            text += f"[← 模块入口](../README.md) · [原题单](../../src/{node}.md)\n\n"
            text += '本页是已写草稿收尾后的独立模块，未据此新增每日安排。\n\n'
        else:
            text += f"[← 当天安排](../day{item['day']:02d}.md) · [原题单](../../src/{node}.md)\n\n"
        text += f"**本轮范围：{len(questions)}道快速题。** 先尝试，卡住再展开讲解；原题前的旧提示不作为依据。本页答案与说明按原图独立核对。\n\n"
        text += fold('卡住先读：完成本组所需的最少知识', item['lesson'])
        text += '\n'
        for number, qid in questions:
            a = item['answers'][qid]
            text += f'## {number} · {qid}\n\n{image(qid)}\n\n'
            text += '先写选项和一句依据；概念题尝试45秒、计算题尝试90秒仍无入口，就展开下面的讲解。学习后遮住讲解，重新作答，保留真实状态。\n\n'
            text += fold('核对与补学（作答后展开）', f"**答案：{a[0]}。** {a[1]}") + '\n'
        text += '## 离开前的一个检查\n\n' + item['test'][0] + '\n\n'
        text += fold('检查答案', item['test'][1])
        (OUT / 'modules' / f'{node}.md').write_text(text)
    days = json.loads((OUT / 'content' / 'days.json').read_text())
    for number, day in days.items():
        n = int(number)
        nodes = day['modules']
        count = sum(len(load_questions(node)) for node in nodes)
        nav = ([f'[← Day {n-1:02d}](day{n-1:02d}.md)'] if str(n-1) in days else [])
        nav += ['[总入口](README.md)']
        if str(n+1) in days:
            nav += [f'[Day {n+1:02d} →](day{n+1:02d}.md)']
        text = f'# Day {n:02d}｜120分钟以题带学\n\n' + ' · '.join(nav) + '\n\n'
        text += '**总时间上限120分钟，补学、核对、纠错均含在内。** 任务是完成本日指定题，不是刷完整个原文件。状态只记独立完成I、引导后完成H、仍有断点U，不把看过或到时当掌握。\n\n'
        text += '## 今天直接按这个顺序做\n\n'
        text += f'1. **0—10分钟：** 回忆昨天留下的一处断点；Day 1用于直接尝试首题，不先找课程。\n2. **10—60分钟：** 做下面两个模块，共{count}道选择题。先尝试，遇到知识缺口在本页补学；模块时间按题数分配，读解答和纠错算在50分钟内。\n'
        for node in nodes:
            text += f"   - [{node}｜{modules[node]['title']}](modules/{node}.md)：{len(load_questions(node))}题。\n"
        text += '3. **60—110分钟：** 完成下面两道大题，每题25分钟：读题与独立尝试5分钟，卡住读折叠解法7分钟，遮住后重写或重算10分钟，核对2分钟，标状态1分钟。已能独立完成时无需等到用满。\n4. **110—120分钟：** 做文末检查，只记一处最值得明天回看的断点，停止当天训练。\n\n'
        text += '**防止时间失控：** 选择题45—90秒没有入口就读本页讲解；不用先去搜视频或整理新笔记。独立做对且依据正确的题立即离开；引导后仍不会的保留U，次日开头处理。120分钟到时如仍未完成，记录真实未完成题号，不能勾成通关；这也是校准本计划工作量的依据。\n\n'
        for i, q in enumerate(day['written'], 1):
            text += f"## 大题{i}｜{q['id']} · {q['title']}\n\n"
            text += f"原题定位：[src/{q['source']}.md 第{q['number']}题](../src/{q['source']}.md)。以年份题号为准，避免原计划题名错位。\n\n"
            text += image(q['id'], '../') + '\n\n'
            text += fold('没有入口时的第一步', q['prompt']) + '\n'
            text += fold('完整解法与必要补学', q['solution']) + '\n'
            text += fold('重做后检查', q['check']) + '\n'
        text += '## 最后10分钟：闭卷检查与交付\n\n'
        text += '\n'.join(f'{i+1}. {v}' for i,v in enumerate(day['recall'])) + '\n\n'
        text += '在纸上留一行即可，不抄解答、不另建整理任务：\n\n```text\n实际用时__分钟；选择题 I__/H__/U__；大题1 I/H/U；大题2 I/H/U\n明天只回看：题号__；卡住的具体一步__\n```\n'
        text += '\n**完成与掌握分别记录。** 指定题均作答并核对、引导后能重现关键步骤，算本日执行完成；U仍存在就保留未通过项，不以此证明已掌握整个模块。扩展原题单的攻坚部分放到后续阶段；当天有余时也只在120分钟内追加。\n'
        (OUT / f'day{n:02d}.md').write_text(text)
    print(f'Built {len(modules)} choice modules and {len(days)} daily routes')


if __name__ == '__main__':
    build()
