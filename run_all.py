#!/usr/bin/env python3
"""PyQt 课程练习小工具：列出、检查或运行练习文件。

用法：
    python run_all.py                    # 检查全部练习的语法
    python run_all.py --list             # 按目录列出全部练习
    python run_all.py --json             # 以 JSON 输出练习列表
    python run_all.py --list --grep 3    # 只列出文件名包含 3 的练习
    python run_all.py --run work1/test1.py
"""

from __future__ import annotations

import argparse
import json
import py_compile
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXERCISE_DIRS = ("class", "work1", "work2", "work3", "work4")


def collect_exercises() -> list[Path]:
    files: list[Path] = []
    for dirname in EXERCISE_DIRS:
        folder = ROOT / dirname
        if folder.is_dir():
            files.extend(sorted(p for p in folder.glob("*.py") if p.name != "__init__.py"))
    return files


def filter_exercises(files: list[Path], keyword: str | None) -> list[Path]:
    if not keyword:
        return files
    needle = keyword.lower()
    return [path for path in files if needle in path.name.lower()]


def list_exercises(files: list[Path]) -> None:
    current = None
    for path in files:
        if path.parent.name != current:
            current = path.parent.name
            print(f"[{current}]")
        print(f"  {path.relative_to(ROOT)}")
    print(f"\n共 {len(files)} 个练习文件")


def dump_json(files: list[Path]) -> None:
    payload = [
        {
            "dir": path.parent.name,
            "name": path.name,
            "path": path.relative_to(ROOT).as_posix(),
        }
        for path in files
    ]
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def show_stats(files: list[Path]) -> None:
    print(f"{'dir':<8}{'files':>7}{'lines':>8}")
    total_files = 0
    total_lines = 0
    for dirname in EXERCISE_DIRS:
        group = [path for path in files if path.parent.name == dirname]
        if not group:
            continue
        lines = sum(len(path.read_text(encoding="utf-8", errors="replace").splitlines()) for path in group)
        total_files += len(group)
        total_lines += lines
        print(f"{dirname:<8}{len(group):>7}{lines:>8}")
    print(f"{'total':<8}{total_files:>7}{total_lines:>8}")


def check_exercises(files: list[Path]) -> int:
    failed = 0
    for path in files:
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as exc:
            failed += 1
            print(f"[FAIL] {path.relative_to(ROOT)}\n{exc}")
        else:
            print(f"[OK]   {path.relative_to(ROOT)}")
    print(f"\n检查完成：{len(files) - failed}/{len(files)} 通过")
    return 1 if failed else 0


def run_exercise(relative_path: str) -> int:
    target = (ROOT / relative_path).resolve()
    if ROOT not in target.parents or not target.is_file():
        print(f"找不到练习文件：{relative_path}", file=sys.stderr)
        return 2
    return subprocess.run([sys.executable, str(target)], check=False).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="PyQt 课程练习工具")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--list", action="store_true", help="列出全部练习")
    group.add_argument("--json", action="store_true", help="以 JSON 格式输出练习列表")
    group.add_argument("--stats", action="store_true", help="按目录统计练习数量与代码行数")
    group.add_argument("--run", metavar="FILE", help="运行指定练习，例如 work1/test1.py")
    parser.add_argument("--grep", metavar="TEXT", help="只保留文件名包含 TEXT 的练习")
    args = parser.parse_args()

    if args.run:
        return run_exercise(args.run)

    files = filter_exercises(collect_exercises(), args.grep)
    if args.grep and not files:
        print(f"没有匹配 {args.grep!r} 的练习文件", file=sys.stderr)
        return 2
    if args.list:
        list_exercises(files)
        return 0
    if args.json:
        dump_json(files)
        return 0
    if args.stats:
        show_stats(files)
        return 0
    return check_exercises(files)


if __name__ == "__main__":
    raise SystemExit(main())
