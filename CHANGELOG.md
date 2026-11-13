# 更新日志

本文件记录仓库的主要变更。格式参考 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.1.0/)，版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [Unreleased]

## [0.2.0] - 2026-11-14

### 新增

- `run_all.py --stats`：按目录统计练习文件数与代码行数
- `run_all.py --json`：以 JSON 输出练习列表，便于脚本消费
- `run_all.py --grep TEXT`：按文件名筛选练习
- `run_all.py --quiet`：检查时只输出失败文件
- `run_all.py --version`：输出版本号
- `tests/test_paths.py`：覆盖 `run_exercise` 的目录穿越防护
- GitHub Actions CI：Python 3.10 / 3.11 / 3.12 三版本运行语法检查与单元测试
- ruff 配置与 lint 任务
- `CONTRIBUTING.md`、PR 模板、Issue 模板

### 变更

- `check_exercises` 改用 `compile()` 在内存中检查语法，不再生成 `__pycache__`
- README 补充完整命令表与 CI 状态徽章

## [0.1.0] - 2026-10-27

### 新增

- `run_all.py`：`--list` 列出练习、默认检查语法、`--run` 运行指定练习
- `tests/test_run_all.py`：练习收集与语法检查的基础测试
- 课程练习：`class/`、`work1/` ～ `work4/`
