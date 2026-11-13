import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import run_all


class TestRunExerciseGuard(unittest.TestCase):
    """run_exercise 必须拒绝仓库之外的路径。"""

    def test_rejects_path_outside_repo(self):
        self.assertEqual(run_all.run_exercise("../outside.py"), 2)

    def test_rejects_nested_traversal(self):
        self.assertEqual(run_all.run_exercise("work1/../../outside.py"), 2)

    def test_rejects_missing_file(self):
        self.assertEqual(run_all.run_exercise("work1/not_exists.py"), 2)

    def test_rejects_directory(self):
        self.assertEqual(run_all.run_exercise("work1"), 2)

    def test_accepts_file_inside_repo(self):
        self.assertEqual(run_all.run_exercise("tests/fixtures/ok.py"), 0)


if __name__ == "__main__":
    unittest.main()
