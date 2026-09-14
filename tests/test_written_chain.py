import datetime as dt
import importlib.util
import json
import sys
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent


def load_builder():
    tools = str(REPO / "tools")
    if tools not in sys.path:
        sys.path.insert(0, tools)
    path = REPO / "tools" / "build_written_chain.py"
    spec = importlib.util.spec_from_file_location("build_written_chain", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class WrittenChainTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.builder = load_builder()
        cls.source = json.loads((REPO / "data/written_lines.json").read_text(encoding="utf-8"))

    def test_every_written_question_has_one_primary_group(self):
        counts = self.builder.validate_source(self.source)
        self.assertEqual(len(counts), 17 * 7)
        self.assertEqual(sum(counts.values()), 17 * 7)
        self.assertTrue(all(count == 1 for count in counts.values()))

    def test_written_chain_starts_after_sealed_choice_chain(self):
        nodes = self.builder.compile_chain(self.source)
        self.assertEqual(nodes[0]["file"], "src/0914.md")
        self.assertEqual(nodes[-1]["file"], "src/1002.md")
        self.assertEqual(nodes[0]["prev"], "src/0908.md")
        for left, right in zip(nodes, nodes[1:]):
            self.assertEqual(
                dt.date.fromisoformat(right["date"]) - dt.date.fromisoformat(left["date"]),
                dt.timedelta(days=1),
            )

    def test_questions_remain_in_year_order(self):
        for line in self.source["lines"]:
            self.assertEqual(
                line["questions"],
                sorted(line["questions"], key=self.builder.question_parts),
            )


if __name__ == "__main__":
    unittest.main()
