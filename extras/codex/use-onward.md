# 切换到 Onward（仅 Codex）

让 Codex 按本文执行：只切换下表中实际已安装的对应技能。本文是可选操作文档，不是自动发现的技能，也不随 `npx skills add` 安装。

## 共用约定

- 找到实际使用的 Codex 用户配置：`$CODEX_HOME/config.toml`，默认是 `~/.codex/config.toml`。修改前告知用户配置路径、切换范围及影响：这是持久设置，会影响使用同一配置的其他项目。
- 按来源和 `SKILL.md` 中的名称确认已安装路径，包括用户目录、当前项目可发现的技能及符号链接；检查实际存在的 `.codex/skills` 与 `.agents/skills`。仓库源码、测试安装目录和上游快照不当作已安装技能。
- 只修改目标路径的 `[[skills.config]]` 启用状态，保留其他配置和无关技能。同一目标复用已有条目；独立安装副本分别处理。技能文件与 `agents/openai.yaml` 保持原样；不卸载、不移动技能，也不把关闭隐式调用当成禁用技能。
- 在同一 Codex 配置目录的 `onward-switch.json` 保存切换记录：配置路径、目标技能名与实际路径、原版各路径之前的配置条目（含“原先不存在”）、当前模式。只保存切换所需信息，不复制整份配置或凭据。每轮从原版切到 Onward 时记录当时状态；已处于 Onward 模式的重复执行保留原记录，新出现的目标再补录。
- 写回后验证 TOML 可解析，目标状态正确且无关设置未变。报告启停结果与记录位置，并提醒用户重启 Codex 后生效；当前会话已加载的指令不会因此从历史中消失。

开关采用 [Codex 官方方式](https://learn.chatgpt.com/docs/build-skills#enable-or-disable-local-codex-skills)，`path` 填已核实的实际绝对路径：

```toml
[[skills.config]]
path = "/actual/path/to/skill/SKILL.md"
enabled = false
```

## 对应范围

这是唯一的切换名单，不按作者、名称相似度或用途自行扩大范围。`show-me` 的来源是 HumanLayer。

| 原版 | Onward |
|---|---|
| grill-me、grilling | grilling-onward |
| to-spec | to-spec-onward |
| to-tickets | plan-onward |
| implement | implement-onward |
| code-review | code-review-onward |
| research | research-onward |
| domain-modeling | domain-modeling-onward |
| codebase-design | codebase-design-onward |
| tdd | tdd-onward |
| diagnosing-bugs | diagnosing-bugs-onward |
| show-me | show-me-onward |

`grill-me` 是调用 `grilling` 的旧入口；两者都安装时一起切换，只安装其一时只处理已有项。

名单以外一律保持原样，例如 `resolving-merge-conflicts`、其他未被 Onward 收录的 Matt 技能，以及没有原版对应项的 `onward`、`init-onward`、`tidy-onward`。

## 执行

逐行核对实际安装：原版至少存在一项且对应 Onward 已安装时才处理这一组。缺少任何一侧就跳过该组、保留现有状态并报告；不为切换而安装新技能。

只对这些可切换组，按共用约定记录原版状态，将对应 Onward 设为 `enabled = true`、已有原版设为 `enabled = false`，记录模式为 `onward`。启用技能不改变它原有的手动或自动调用策略。

切回时执行 [use-originals.md](use-originals.md)。
