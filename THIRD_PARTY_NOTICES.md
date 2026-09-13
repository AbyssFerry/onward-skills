# 来源、许可证与修改说明

Onward Skills 包含自建内容和经调整的第三方技能。Onward 新增内容采用 [MIT License](LICENSE)；第三方原作者、版权和许可证按下文分别保留。每个技能目录携带 `LICENSE`，用于按技能安装或复制时一并保留声明。

## Matt Pocock

来源仓库：[mattpocock/skills](https://github.com/mattpocock/skills)。采用的来源版本为 [`3cca18b368ae95cdbdebbff572ccafa662551015`](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015)。版权归 Matt Pocock，原许可为 [MIT](licenses/mattpocock-skills-MIT.txt)。

下表中的每项都改为 Onward 的独立名称；适用的界面名称也相应调整。修改说明包括正文、内部引用及调用配置，而不仅是方法是否改变。

| Onward 技能 | 原技能 | 保留与修改范围 |
|---|---|---|
| `grilling-onward` | [grilling](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/productivity/grilling/SKILL.md) | 保留原提问与探索方法；补充领域建模、模块设计的按需引用和确认后报告并停止的边界；设为仅手动调用 |
| `to-spec-onward` | [to-spec](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/to-spec/SKILL.md) | 保留综合讨论、完整规范模板和测试决定等要求；追踪器前提改为 AGENTS.md 中的 Onward 约定，发布议题改为本地文档；保留仅手动调用语义 |
| `to-plan-onward` | [to-tickets](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/to-tickets/SKILL.md) | 将 ticket／窄切片改为完整实施任务，默认按 implement 交付周期判断粒度并检查合并机会；保留依赖、用户确认、大范围重构迁移顺序及本地模板；输出限定为本地任务文件，增加计划更新和规范引用，使用 AGENTS.md 中的 Onward 约定；保留仅手动调用语义 |
| `implement-onward` | [implement](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/implement/SKILL.md) | 保留 TDD、检查频率、审查和提交；限定指定规范或当前可执行任务，保护已有改动，调用共用审查，提交前自行检查并同步受影响的规范、任务状态和验证记录，收尾报告后停止；保留仅手动调用语义 |
| `code-review-onward` | [code-review](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/code-review/SKILL.md) | 保留双轴并行审查、Git 基准与提交列表、引用和空差异检查、规范查找、12 项代码异味与独立汇总；改用可选追踪器及本地规范目录，复用调用方输入，包含范围内未提交改动和新文件，按选定任务核对 |
| `research-onward` | [research](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/research/SKILL.md) | 方法正文保留；允许自动与手动调用 |
| `domain-modeling-onward` | [domain-modeling](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/domain-modeling/SKILL.md) | 保留建模方法、领域词汇表格式和 ADR 模板、条件与示例；增加遵循 AGENTS.md 中选定的文档位置，ADR 默认改为 spec/adr/，同步其创建和编号查找位置；允许自动与手动调用 |
| `codebase-design-onward` | [codebase-design](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/codebase-design/SKILL.md) | 方法正文及模块深化、双方案设计参考保留；允许自动与手动调用 |
| `tdd-onward` | [tdd](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/tdd/SKILL.md) | 方法及测试、模拟参考保留；模块设计和代码审查的引用改为本包技能名称；允许自动与手动调用 |
| `diagnosing-bugs-onward` | [diagnosing-bugs](https://github.com/mattpocock/skills/blob/3cca18b368ae95cdbdebbff572ccafa662551015/skills/engineering/diagnosing-bugs/SKILL.md) | 完整六阶段方法、脱敏、复现、假设、回归要求及人工配合脚本保留；增加读取 AGENTS.md 中 Onward 约定的前提；允许自动与手动调用 |

`agents/openai.yaml` 是本包使用的 Codex 界面与调用配置。原技能的仅手动调用要求在适用时转换为 `allow_implicit_invocation: false`。`grilling-onward`、`to-spec-onward` 和 `to-plan-onward` 只保留调用策略，未复制来源适配中的界面展示字段；`implement-onward` 同时更新界面名称与短描述，其余保留的界面名称加入 Onward。其他新增或保留的自动调用选择见 [README](README.md)。

## HumanLayer

`show-me-onward` 来源于 [humanlayer/skills](https://github.com/humanlayer/skills)，原路径为 [`plugins/show-me/skills/show-me/SKILL.md`](https://github.com/humanlayer/skills/blob/6ab9013a10c28f5046f7f999549cd5328a0b30d7/plugins/show-me/skills/show-me/SKILL.md)，采用提交 [`6ab9013a10c28f5046f7f999549cd5328a0b30d7`](https://github.com/humanlayer/skills/commit/6ab9013a10c28f5046f7f999549cd5328a0b30d7)。版权归 HumanLayer，原许可为 [MIT](licenses/humanlayer-skills-MIT.txt)。

方法结构、图解类型、示例与指导保留。实际差异是：

1. 技能名改为 `show-me-onward`。
2. 将打开 HTML 的固定 `Bash(open …)` 命令改为使用当前环境可用的工具，保留 HTML 文件命名示例；不限定操作系统。
3. 新增 Codex 调用配置，设为仅手动调用。

## Onward 自建内容

`onward`、`init-onward` 和 `tidy-onward` 是本项目自建技能，不对应一份被改写的第三方技能原文。项目约定、套件组合、中文说明、网页及上述新增修改采用 Onward 的 MIT 许可。

完整中文原文、使用场景和逐段差异见 [技能说明页](https://abyssferry.github.io/onward-skills/)。所有来源声明均独立于技能指令正文；第三方作者不因此被表示为本项目的维护者或背书方。
