# Python 程序设计基础练习

> 课程前期 Python 基础题合集，覆盖语法、字符串/列表、二维列表、函数与递归。仓库名沿用课程名「PyQt」，当前代码以 Python 基础练习为主。

[![CI](https://github.com/yunshujing/PyQt/actions/workflows/ci.yml/badge.svg)](https://github.com/yunshujing/PyQt/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat&logo=python&logoColor=white)
![status](https://img.shields.io/badge/status-coursework-lightgrey)

## 内容

| 目录 | 内容 | 入口 |
| --- | --- | --- |
| `work1/` | 基础语法与数学计算：圆面积、闰年、调和级数等 | `python work1/test1.py` |
| `work2/` | 字符串与列表：空格处理、杨辉三角等 | `python work2/test2_1.py` |
| `work3/` | 二维列表：古诗竖排等 | `python work3/test3_1.py` |
| `work4/` | 函数与递归：阶乘等 | `python work4/test4_1.py` |
| `class/` | 课堂演示代码：球体积等 | `python class/demo1.py` |

当前共 25 个练习文件。

## 项目结构

```text
PyQt/
├── run_all.py     # 一键检查 / 运行 / 统计练习
├── tests/         # 工具与路径防护的单元测试
├── work1/         # Python 基础语法
├── work2/         # 字符串与列表
├── work3/         # 二维列表
├── work4/         # 函数与递归
└── class/         # 课堂演示
```

## 环境要求

- Python 3.10+
- 无第三方运行时依赖

## 运行

每个练习文件都是独立入口，直接运行即可：

```bash
python work1/test1.py
python work2/test2_1.py
```

也可以使用 `run_all.py` 批量查看、检查和统计：

```bash
python run_all.py                       # 检查全部练习语法
python run_all.py --list                # 按目录列出全部练习
python run_all.py --json                # 以 JSON 输出练习列表
python run_all.py --list --grep 3       # 只列出文件名含 3 的练习
python run_all.py --stats               # 按目录统计文件数与代码行数
python run_all.py --quiet               # 只输出检查失败的文件
python run_all.py --version             # 查看工具版本
python run_all.py --run work1/test1.py  # 运行指定练习
```

`--stats` 输出示例：

```text
dir       files   lines
class         3      22
work1         8     167
work2         6     156
work3         4      76
work4         4     187
total        25     608
```

`--run` 只接受仓库内的路径，传入 `../` 开头的路径会被拒绝。

## 测试

```bash
python -m unittest discover -s tests -v
```

CI 会在 Python 3.10 / 3.11 / 3.12 上分别跑一遍语法检查和单元测试。

## 参与贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md)。提交前请确认 `python run_all.py` 与单元测试都通过。

## 技术栈 / 学习点

- Python 基础语法、输入输出、条件与循环
- 字符串处理、列表与二维列表
- 函数、递归与简单算法
- 命令行小工具：argparse、路径校验、单元测试与 CI

## 说明

- 本仓库为课程作业，不是生产项目。
- 当前内容为课程前期的 Python 基础练习；仓库名来自课程名，Qt GUI 内容后续补充。
