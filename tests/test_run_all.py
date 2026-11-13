import contextlib
import io
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import run_all


class TestRunAll(unittest.TestCase):
    def test_collect_exercises(self):
        files = run_all.collect_exercises()
        self.assertEqual(len(files), 25)
        self.assertTrue(all(path.suffix == ".py" for path in files))

    def test_check_exercises_passes(self):
        files = run_all.collect_exercises()
        self.assertEqual(run_all.check_exercises(files), 0)

    def test_show_stats_lists_every_dir(self):
        files = run_all.collect_exercises()
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            run_all.show_stats(files)
        text = output.getvalue()
        for dirname in run_all.EXERCISE_DIRS:
            if any(path.parent.name == dirname for path in files):
                self.assertIn(dirname, text)
        self.assertIn("total", text)


if __name__ == "__main__":
    unittest.main()
