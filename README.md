<div align="center">

# 小猫揍人编剧强化 Skill

[![DeepSeek Harness](https://img.shields.io/badge/DeepSeek%20Harness-dsh--plugin-4D6BFE?style=flat-square)](https://github.com/deepseek-ai/deepseek-harness)
[![Agent Skill](https://img.shields.io/badge/Agent-Skill-7C3AED?style=flat-square)](SKILL.md)
[![License](https://img.shields.io/github/license/YanKaFei/kitten-punch-screenwriting?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square)](VERSION)

**生产级中文编剧创作与剧本诊断系统**

概念超短片 ｜ 短片 ｜ 电影长片 ｜ 剧集 · 连续剧 ｜ 竖屏短剧 · 微短剧

</div>

---

## 这是什么

生产级中文编剧创作与剧本诊断系统：从零开发、续写、改戏、对白打磨、剧本医生、结构诊断与长篇连续性维护。小猫揍人编剧强化skill v1.0.0，内置一套“因果优先、证据循环”的工程化写作方法。它不是提示词合集，而是一台把“故事状态”当作账本维护的编译器：每个场景都是一次状态事务，只有通过 QC 才允许提交，失败不会污染整个故事。

## 核心能力

- **主角驱动因果**：高潮与转折必须来自主角已有的欲望、选择、能力与信息。
- **场景价值转折**：每场必须改变处境、关系、信息、资源、危险或选择空间之一，并留下下一场压力。
- **故事状态机（Story SSoT）**：人物图谱、关系状态、物件/资源、世界规则、不可逆事件、承诺-兑现、时间线全部唯一真实可操作化。
- **对白引擎**：对白是行为而非信息朗读，每个主要人物维护自身的信息和台词样本；内置中文自然度与去 AI 味规范。
- **承诺-兑现系统**：神秘身份、特殊能力、道具、预言、被遮住的真相等制造期待的内容，`BROKEN` 。
- **14 道证据式 QC**：因果、主角能动性、目标、落差、行为策略、场景价值、下场压力、代价升级、知识连续、物理连续、世界规则、承诺兑现、人物声音、可拍摄性、语言自然度。
- **单调修复**：QC 失败后按来源回修对应层，禁止为修局部问题重写整体或引入新设定。
- **长篇记忆快照**：按 Sequence / 集 / 关键高潮滚动更新，保证长篇连续性。

## 目录结构

```text
kitten-punch-screenwriting v1.0.0

├── SKILL.md                      # 主说明与完整工作流
├── references/
│   ├── concept-film.md           # 概念超短片
│   ├── natural-chinese.md        # 中文自然度与去 AI 味
│   └── vertical-drama.md         # 竖屏短剧
├── runtime/
│   ├── story-state.md            # 故事状态机与账本
│   ├── evidence-qc.md            # 证据式 QC 与 Gate 依赖
│   ├── promise-payoff.md         # 承诺—兑现系统
│   └── repair-protocol.md        # 失败定位与单调修复
├── tests/
│   └── regression-cases.md       # 代表性回归测试
├── scripts/
│   └── validate_skill.py         # 结构校验脚本
├── VERSION
├── MANIFEST.txt
└── SHA256SUMS
```

## 使用方式

这是一个标准 Skill 包，可作为 Claude Code / DeepSeek Harness 等 Agent 的技能加载：将本目录放入对应平台的 `skills/` 目录，或直接让 Agent 读取 `SKILL.md` 作为写作规范。

校验完整性：

```bash
cd kitten-punch-screenwriting
python3 scripts/validate_skill.py
```

## 许可证

MIT，见 [LICENSE](LICENSE)。
