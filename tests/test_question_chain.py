import datetime as dt
import importlib.util
import json
import unittest
import tempfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent


def load_builder():
    path = REPO / "tools/build_question_chain.py"
    spec = importlib.util.spec_from_file_location("build_question_chain", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class QuestionChainTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.builder = load_builder()
        cls.source = json.loads((REPO / "data/ability_lines.json").read_text(encoding="utf-8"))

    def test_all_bank_questions_are_assigned(self):
        counts = self.builder.validate_source(self.source)
        self.assertEqual(len(counts), 680)
        self.assertEqual(sum(counts.values()), 706)

    def test_one_ability_line_is_one_consecutive_node(self):
        nodes = self.builder.compile_chain(self.source)
        self.assertEqual(len(nodes), 40)
        self.assertEqual(nodes[0]["file"], "src/0731.md")
        self.assertEqual(nodes[-1]["file"], "src/0908.md")
        for left, right in zip(nodes, nodes[1:]):
            self.assertEqual(
                dt.date.fromisoformat(right["date"]) - dt.date.fromisoformat(left["date"]),
                dt.timedelta(days=1),
            )
            self.assertEqual(left["next"], right["file"])
            self.assertEqual(right["prev"], left["file"])

    def test_rebuild_preserves_manual_prose_but_rejects_changed_questions(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "0731.md"
            original = '### 01 · 2011-01\n![corrected crop](../bank/2011/q02.png)\nHuman explanation and review links\n'
            path.write_text(original)
            rendered = {path: '### 01 · 2011-01\n![q](../bank/2011/q01.png)\nGenerated prose'}
            self.builder.protect_existing_pages(rendered)
            self.assertNotIn(path, rendered)
            self.assertEqual(path.read_text(), original)
            with self.assertRaises(ValueError):
                self.builder.protect_existing_pages({path: '### 01 · 2012-01\n![q](../bank/2012/q01.png)'})

    def test_questions_remain_in_year_order(self):
        for line in self.source["lines"]:
            self.assertEqual(
                line["questions"],
                sorted(line["questions"], key=self.builder.question_parts),
            )


if __name__ == "__main__":
    unittest.main()
