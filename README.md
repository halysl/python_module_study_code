# Python 模块学习笔记与代码

![Python](https://img.shields.io/badge/Python-3.8.5-blue.svg)
![Status](https://img.shields.io/badge/Status-Archived-lightgrey.svg)
![Period](https://img.shields.io/badge/Period-2018--2021-green.svg)

这是一个记录 Python 模块学习过程的个人项目，包含了丰富的学习文档和练习代码。项目涵盖了从基础标准库到第三方框架的多个领域。

> ⚠️ **注意**: 此项目已归档，不再积极维护。部分内容可能已过时，仅供参考学习。

## 📚 项目结构

```
.
├── doc/                    # 学习文档（Markdown 格式）
│   ├── mysql/              # MySQL 数据库相关文档
│   └── *.md                # 各类模块学习笔记
├── src/                    # 源代码目录
│   ├── study_*/            # 各模块练习代码
│   └── utils/              # 工具函数集合
├── Pipfile                 # Pipenv 依赖配置
└── Pipfile.lock            # 依赖锁定文件
```

## 📝 学习文档

`doc/` 目录下包含了以下学习笔记：

| 文档 | 描述 |
|------|------|
| [pytest的简单学习](doc/pytest的简单学习.md) | pytest 单元测试框架详解，包括 fixture、mark 等特性 |
| [Schema库的简单学习](doc/Schema库的简单学习.md) | 数据校验库 Schema 的使用方法 |
| [marshmallow库的简单学习](doc/marshmallow库的简单学习.md) | 序列化/反序列化库 marshmallow 的学习笔记 |
| [Pexpect库的简单学习](doc/Pexpect库的简单学习.md) | 自动化交互式程序的 Pexpect 库 |
| [paramiko库的简单学习](doc/paramiko库的简单学习.md) | SSH 远程连接库 paramiko 的使用 |
| [argparse学习](doc/argparse学习.md) | 命令行参数解析模块 |
| [Mock的简单学习](doc/Mock的简单学习.md) | 单元测试中的 Mock 技术 |
| [单元测试浅析](doc/单元测试浅析.md) | 单元测试概念与实践 |
| [正则表达式及re库的使用](doc/正则表达式及re库的使用.md) | 正则表达式与 re 模块 |
| [一些技巧](doc/一些技巧.md) | Python 编程小技巧 |

### MySQL 学习文档

`doc/mysql/` 目录包含了 MySQL 数据库的学习资料：

- MySQL 数据库简介
- MySQL 查询与高级查询
- MySQL 内置函数
- MySQL 相关命令
- MySQL 与 Python 结合使用

## 💻 练习代码

`src/` 目录下包含了丰富的练习代码：

### 第三方库学习

| 目录 | 描述 |
|------|------|
| `study_pytest/` | pytest 单元测试框架练习 |
| `study_mock/` | Mock 测试技术练习 |
| `study_marshmallow/` | marshmallow 序列化库练习 |
| `study_schema/` | Schema 数据校验库练习 |
| `study_celery/` | Celery 分布式任务队列 |
| `study_apschedler/` | APScheduler 定时任务调度 |
| `study_tornado/` | Tornado Web 框架 |
| `study_jinja2/` | Jinja2 模板引擎 |
| `study_sqlalchemy/` | SQLAlchemy ORM 框架 |
| `study_requests/` | Requests HTTP 库 |
| `study_paramiko/` | Paramiko SSH 库 |
| `study_redis/` | Redis 数据库操作 |
| `study_numpy/` | NumPy 科学计算库 |

### Web 与爬虫

| 目录 | 描述 |
|------|------|
| `study_spider/` | 网络爬虫练习 |
| `study_tornado/` | Tornado 异步 Web 框架 |

### 标准库与工具

| 目录 | 描述 |
|------|------|
| `study_standard/` | Python 标准库学习 |
| `study_cookbook/` | Python Cookbook 代码实践 |
| `study_object/` | 面向对象编程练习 |
| `study_tar_args/` | 命令行参数处理 |
| `study_invoke/` | invoke 任务执行库 |
| `study_supervisor/` | Supervisor 进程管理 |

### GUI 与可视化

| 目录 | 描述 |
|------|------|
| `pyqt-study/` | PyQt5 GUI 编程 |
| `study_prompt_toolkit/` | prompt-toolkit 命令行界面 |
| `study_wordcloud/` | 词云生成 |
| `heat_map/` | 热力图绘制 |

### 其他

| 目录 | 描述 |
|------|------|
| `study_docx_templates/` | Word 文档模板处理 |
| `study_checkio/` | CheckiO 编程练习题 |
| `study_ctf/` | CTF 安全练习 |
| `utils/` | 通用工具函数 |
| `Card/` | 卡片相关练习 |

## 🛠️ 环境配置

### 依赖管理

本项目使用 [Pipenv](https://pipenv.pypa.io/) 进行依赖管理。

**Python 版本要求**: Python 3.8.5

### 主要依赖

- **Web 框架**: Tornado
- **ORM**: SQLAlchemy
- **数据处理**: NumPy, Pandas
- **HTTP**: Requests
- **模板引擎**: Jinja2
- **任务调度**: APScheduler
- **GUI**: PyQt5
- **数据可视化**: Matplotlib, Seaborn
- **其他**: IPython, docxtpl, lxml

### 安装步骤

```bash
# 安装 Pipenv（如果尚未安装）
pip install pipenv

# 进入项目目录
cd python_module_study_code

# 安装依赖
pipenv install

# 激活虚拟环境
pipenv shell
```

## 📖 使用说明

1. **阅读文档**: 从 `doc/` 目录开始，选择感兴趣的主题阅读对应的 Markdown 文档
2. **运行代码**: 进入 `src/` 目录下对应的模块文件夹，运行练习代码
3. **实践学习**: 结合文档和代码进行学习和实践

```bash
# 运行示例（以 pytest 为例）
cd src/study_pytest
pytest -v
```

## ⏰ 项目时间线

- **2018 年**: 项目创建，开始 Python 模块学习
- **2018-2021**: 持续更新学习笔记和练习代码
- **2021 年**: 项目归档

## 📄 许可证

本项目仅用于个人学习记录，代码和文档仅供参考。

## 🔗 相关资源

- [Python 官方文档](https://docs.python.org/3/)
- [Python Cookbook](https://python3-cookbook.readthedocs.io/)
- [Real Python](https://realpython.com/)

---

*此项目是个人学习 Python 过程中的记录，希望对其他学习者有所帮助。*
