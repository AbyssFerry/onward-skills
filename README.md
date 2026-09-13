# Onward Skills

Onward，意为「向前」。编程时，我们常在一个问题解决后停下来，不知道下一步该走向哪里。Onward 希望接住这些停顿：理清眼前的事，找到下一步，让想法继续生长。每当思路停在半途，就再说一次 onward——让下一步，接住还未完成的远方。

一套围绕项目文档与开发主流程协作的 AI 技能：讨论设计、形成规范、安排计划、实施交付，并按需借助研究、诊断、审查与文档整理。

Onward 面向采用自身项目约定的仓库。它以 Matt Pocock 的技能为重要基础，尽量保留原文，只调整项目约定、输出位置和技能之间的配合。共 **14 个技能：6 个核心技能、8 个支撑技能**。

当前版本：[v0.1.0](https://github.com/AbyssFerry/onward-skills/releases/tag/v0.1.0)。

[中文技能全文、使用场景与逐段对照](https://abyssferry.github.io/onward-skills/) · [来源与修改说明](THIRD_PARTY_NOTICES.md)

## 安装

准备 Node.js（含 npm / npx）和 Git，在要使用 Onward 的项目目录中运行：

```bash
npx skills@latest add AbyssFerry/onward-skills --skill '*' --agent codex
```

这会选择整套技能供 Codex 使用。技能之间有内部引用，首次使用请安装全套。若要安装到用户范围，在命令末尾增加 `-g`；其他 Agent 可通过安装器选择。

只查看仓库提供的技能：

```bash
npx skills@latest add AbyssFerry/onward-skills --list
```

查看已安装技能可用 `npx skills list`，更新使用 `npx skills update`。安装由 [Vercel 的 skills CLI](https://github.com/vercel-labs/skills) 完成。

### 已安装原版技能：可选切换（仅 Codex）

可让 Codex 阅读并执行 [切换到 Onward](extras/codex/use-onward.md) 或 [切回原版](extras/codex/use-originals.md)。只切换文档名单中两侧都已安装的对应组；切回时恢复原版之前的开关。名单外一律保持原样，包括合并冲突等未收录的 Matt 技能和 Onward 的独有入口。

这两份普通 Markdown 放在 `extras/codex/`，不随技能安装，也不会自动执行。切换使用 Codex 用户配置，影响同一配置下的其他项目，修改后需要重启 Codex。

## 开始使用

第一次接入项目：

```text
$init-onward 为这个项目建立 Onward 文档约定。
```

随后按当前需要选择入口，例如：

```text
$grilling-onward 我想增加批量导入，先把需求和设计讨论清楚。
$to-spec-onward 把已经确认的设计写成项目规范。
$to-plan-onward 根据这份规范安排实施任务。
$implement-onward 实施计划中当前依赖已满足的一个任务。
```

不确定接下来做什么时，调用 `$onward`。小功能可以由规范直接进入实施；计划用于需要拆分的工作，也可以更新已有计划。

## 核心技能

主流程及其导航，均由用户手动启动。

| 技能 | 用途 |
|---|---|
| `onward` | 根据当前目标和进度判断下一步，缺少项目约定时提醒初始化 |
| `init-onward` | 首次接入已有项目时并行探索原始材料，再展示迁移方案与约定草稿，按用户调整确认后执行 |
| `grilling-onward` | 讨论并推敲目标与设计，确认共同理解 |
| `to-spec-onward` | 将已确认的讨论整理为本地规范 |
| `to-plan-onward` | 创建或更新有依赖关系的本地任务计划 |
| `implement-onward` | 实施指定规范或当前可执行任务，验证、同步文档、审查并提交 |

## 支撑技能

所有支撑技能都可以手动调用；除 `show-me-onward` 外，其余也允许 AI 按需自动选用。

| 技能 | 用途 |
|---|---|
| `tidy-onward` | 整理、同步和归档文档，从正确性与一致性两方面审查 |
| `diagnosing-bugs-onward` | 复现、诊断和修复棘手 Bug 或性能回退 |
| `code-review-onward` | 从项目规范与需求符合度两方面审查本次改动 |
| `research-onward` | 根据可信的一手来源调查问题，保存研究依据 |
| `domain-modeling-onward` | 建立领域语言，维护术语与架构决策 |
| `codebase-design-onward` | 讨论模块职责、边界与接口 |
| `tdd-onward` | 在适当边界进行测试驱动开发 |
| `show-me-onward` | 用图解或聚焦网页帮助理解当前话题 |

上述自动调用策略通过各技能的 Codex 配置表达；其他工具是否采用同一策略，以其技能机制为准。

目前安装与分发验收在 Windows + Codex 环境完成。`show-me-onward` 使用当前环境可用的工具打开网页；macOS、Linux 及其他 Agent 尚未进行整套行为验证。

## 项目文档

`init-onward` 在使用项目的 `AGENTS.md` 末尾追加简洁的 Onward 约定，只维护稳定的文档职责、采用的位置、阅读入口与维护规则；标题层级顺应原文件，保留原有内容。文件不存在时创建，已有 Onward 区块时更新而不重复追加。项目额外目录、临时位置和具体文件清单通过项目的文档入口或索引导航；版本、阶段、进度及检查结果留在相关规范、计划或报告中。`spec/conventions.md` 从项目已有文档、代码和配置中发现工程约定，整理或引用原有权威规则；本包不提供统一的编码规范套餐，没有实际内容时不创建空文件。依赖 Onward 约定的技能在这些约定缺失时提示先初始化，判断依据不再是 conventions 文件是否存在。

默认文档各有职责，随实际内容按需创建。项目可以在 `spec/` 中增加有独立用途的文件或子目录，并将位置和用途记入项目的文档入口或索引。这些额外目录增删或迁移时，更新文档入口或索引，AGENTS 中的通用 Onward 约定应继续有效：

| 位置 | 用途 |
|---|---|
| `spec/product.md` | 产品服务谁、解决什么问题、范围、用户流程与预期行为 |
| `spec/architecture.md` | 系统与模块边界、职责、交互、数据流及技术取舍 |
| `spec/conventions.md` | 项目自身的目录、编码、构建和测试实践 |
| 根目录 `CONTEXT.md` | 领域术语及定义；多个上下文时沿用已有上下文地图 |
| `spec/adr/` | 重要架构决定及其理由和取舍，每个决定一份编号文件 |
| `spec/api.md` | 对外接口的请求、响应、错误及示例 |
| 模块内 `spec/` | `design.md` 记录内部设计，`interface.md` 记录调用入口与约束并引用详细契约，适用时用 `api.md` 保存对外 API 契约和示例；模块形成后就近维护 |
| `spec/<change-name>-spec.md` | 通常由 `to-spec-onward` 生成，记录一次变更的目标、设计、验收与状态 |
| `spec/plans/<feature-slug>/` | 实施任务及依赖，每项任务一份文件 |
| `.onward/future/` | 以后再讨论或实施的事项，简单清单或独立主题文档 |
| `.onward/research/` | 调查问题、来源、发现与限制 |
| `.onward/visuals/` | 图示、可视化及源文件 |
| `.onward/reports/` | 审查、诊断、验证和交接发现 |
| `.onward/archive/` | 已退出日常维护的历史快照，直接存入此目录 |

项目尚无文档结构时，`init-onward` 按默认结构初始化。首次接入已有项目时，先并行派出只读探索子 Agent，覆盖原始文档及其关系、代码配置与测试、已有工程及 Agent 约定，按实际材料调整分工。范围内的文档完整阅读；主 Agent 汇总带来源的发现，核对分歧并理清受影响内容后，再起草方案。空项目和后续局部更新按实际范围查看材料。

已有文档结构时，参照技能正文的简短示例，用“处理方式、当前文件或章节、推荐位置、用途与原因”四列表格展示推荐迁移方案；合并与拆分明确到内容归属，并交代留在原文件中的部分。初始化还会展示拟写入的 Onward 区块和关键工程约定草稿。你可以全部或部分保留旧位置，也可以自定义；方案确认后，将稳定的 Onward 约定写入 AGENTS.md，项目具体文档导航写入入口文档或索引。迁移由 init 在初始化中完成，保留内容并同步引用与约定。日常文档整理仍由 `tidy-onward` 处理。

ADR 的实际位置遵循 AGENTS.md 中的 Onward 约定；例如选择保留 `docs/decisions/`，领域建模就在那里继续编号，不另建默认目录。

模块设计期可以先用一份规范。`to-spec-onward` 将已确认设计写入适当的规范文档；已有内容需要拆分归位时，由 `tidy-onward` 按项目约定整理。`implement-onward` 收尾时自行检查并同步受影响的规范、任务状态和验证记录，不自动调用 tidy 或额外启动文档审查。

## 来源与许可

Onward 的新增内容采用 [MIT License](LICENSE)。第三方材料保留其原作者与适用许可，并随技能目录携带许可证。

Matt Pocock 的 [mattpocock/skills](https://github.com/mattpocock/skills) 提供了本套件多数复用方法；`show-me-onward` 基于 [HumanLayer 的 show-me](https://github.com/humanlayer/skills/tree/6ab9013a10c28f5046f7f999549cd5328a0b30d7/plugins/show-me)。逐项来源、采用版本、保留内容及实际修改见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)，中文全文对照见 [技能说明页](https://abyssferry.github.io/onward-skills/)。

技能指令本身使用英文，网页提供中文阅读版本。说明中的使用场景是预期行为示例。
