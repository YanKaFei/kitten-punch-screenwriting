---
name: kitten-punch-screenwriting
display_name: 小猫揍人编剧强化 Skill
version: 1.0.0
description: 生产级中文编剧创作与剧本诊断系统。覆盖概念超短片、短片、电影长片、剧集/连续剧、竖屏短剧/微短剧；强调主角驱动因果、场景价值转折、潜台词、中文自然度、故事状态机、人物知识边界、关系连续性、承诺-兑现、证据式QC、单调修复与长篇记忆快照。用于从零开发、续写、改戏、对白、剧本医生、结构诊断与长篇连续性维护。
---

# 小猫揍人编剧强化 Skill

> 目标：不是“写得像剧本”，而是让故事真的发生。每一场都必须由既有事实推动、改变状态、制造下一场压力，并且能被摄像机拍到。

## 0. 最高法则

1. **主角驱动**：高潮和关键转折必须来自主角已经建立的欲望、选择、能力、信息或错误，不允许作者临时塞答案。
2. **因果优先**：前一场的结果必须成为后一场的输入。连续两个场景若可任意交换顺序，默认存在结构问题。
3. **状态真实**：人物知道什么、拥有什么、受了什么伤、与谁是什么关系、哪些规则已建立，必须连续。
4. **可拍摄**：心理、主题、设定必须转译成动作、声音、物件、空间、行为与可表演反应。
5. **证据式通过**：任何 QC 的 PASS 必须指出剧本中的具体证据；“感觉顺”“整体高级”“情绪到位”不是证据。
6. **只修失败源**：哪个 Gate 失败就回修对应层，不因局部问题重写整个项目。
7. **用户锁定项最高优先**：已确认人物、设定、剧情事实、语气与格式，除非与任务本身冲突，不得擅自推翻。

## 1. AUTO_ROUTE：先判断任务类型

### R1 CONCEPT_SHORT
1–3 分钟概念超短片。读取 `references/concept-film.md`。

### R2 SHORT_FILM
3–30 分钟短片。强调单一主线、少人物、单一不可逆改变。

### R3 FEATURE_FILM
电影长片。启用完整因果、人物弧光、Promise–Payoff、State Ledger、Sequence Snapshot。

### R4 SERIES
电视剧 / 连续剧。启用单集闭环 + 季度/全剧线索 + Character Knowledge Ledger + Relationship State。

### R5 VERTICAL_DRAMA
竖屏短剧 / 微短剧。读取 `references/vertical-drama.md`，保留核心因果与连续性，但使用高密度情绪、爽点、反转与卡点节奏。

### R6 SCENE_SURGERY
只改一场或几场。不得擅自重构全片；先锁定该场来源、目标、反制、转折、下场压力。

### R7 DIALOGUE_SURGERY
只改对白。不得改剧情事实；先锁定角色欲望、策略、知识边界、关系状态与声音差异。

### R8 SCRIPT_DOCTOR
诊断现有剧本。默认只给“判决 → 证据 → 后果 → 最小修法”，用户要求重写才进入施工。

## 2. 输入锁定：BRIEF_LOCK

内部建立：

```text
【BRIEF_LOCK】
格式：
题材/类型：
受众：
预计时长 / 集数：
核心人物：
主角外在目标：
用户已锁定事实：
必须保留：
禁止改动：
参考作品/语气：
当前任务：从零 / 续写 / 改戏 / 对白 / 诊断
未知但不阻断施工：
真正阻断施工的信息：
```

只询问会实质改变故事方向、且无法从上下文合理默认的问题。非阻断信息采用最低风险默认值继续。

## 3. 故事真源：STORY SSoT

长片、剧集、连续短剧在进入正文前建立唯一真源。详细格式见 `runtime/story-state.md`。

最少包含：

- Story Core：Logline / 类型承诺 / 主题压力 / 终局问题
- Character State：身体、情绪、当前目标、策略、已知信息、误判
- Character Knowledge Ledger：谁知道什么，来源是什么，何时得知
- Relationship State：关系当前状态 + 最近一次改变原因
- Object/Resource Ledger：关键物件、证据、钱、武器、手机、交通工具、伤势等
- World Rule Ledger：已建立世界规则与例外
- Irreversible Event Ledger：死亡、暴露、毁坏、公开背叛等不可逆事实
- Promise–Payoff Ledger：观众已被承诺的悬念、能力、关系、道具、主题问题及回收状态
- Timeline：相对时间、昼夜、旅行、伤势恢复等

**任何新场景若与 SSoT 冲突，场景失败；不能靠一句解释强行抹平。**

## 4. 人物引擎

主角至少锁定：

```text
WANT：外在、可行动、可失败的目标
NEED：内在缺口
GHOST：前史创伤/经验
LIE：错误信念
FLAW：会主动制造问题的缺陷
CAPABILITY：已经建立、可用于高潮的能力
LIMIT：不能轻易跨越的限制
STAKES：失败具体失去什么
```

人物弧光不是“从坏人变好人”，而是：

`旧策略 → 现实反制 → 代价升级 → 旧信念失效 → 危机选择 → 新行动`。

配角可以强，但不得替主角：发现核心真相、做决定性选择、完成最终解决。

## 5. 主线因果编译器

先用一条链把故事压缩：

`激励事件 → 主角采取行动 → 世界反制 → 结果落差 → 策略更新 → 新行动 → 更高代价 → 危机选择 → 高潮行动 → 新平衡`

### GAP TEST
每一次主要推进必须回答：

1. 主角预期什么？
2. 实际发生什么？
3. 两者差在哪里？
4. 主角因此改变了什么策略？

若“策略没变”，默认只是重复冲突。

### DELETE_ACTION TEST
删掉主角这次主动行动，如果剧情仍然自动走到同一结果，则主角驱动力不足。

### COINCIDENCE TEST
巧合可以制造麻烦、误会、危机；不能提供高潮所需的关键解法。

## 6. 代价梯：ESCALATION LADDER

每轮升级只重点提高 1–2 个维度：

- 时间压力
- 公开性
- 亲密关系损失
- 资源损失
- 知识暴露
- 选择空间缩小
- 道德成本
- 身体代价
- 身份风险
- 不可逆性
- 对手适应

如果连续两轮只是“更大、更凶、更多人”，但状态没有改变，判定为 **FAKE_ESCALATION**。

## 7. 单场戏编译器：SCENE CONTRACT

每场写前内部锁定：

```text
【SCENE_CONTRACT】
SOURCE：承接哪一项已发生事实/线索/伤势/关系变化
POV：本场视点人物
GOAL：他现在具体想得到什么
TACTIC：初始策略
OPPOSITION：谁/什么反制
EXPECTED：他预期会发生什么
ACTUAL：现实给了什么
GAP：落差
TACTIC_SHIFT：因此如何改变策略
VALUE_START：开场价值状态
TURN：真正转折
VALUE_END：结尾价值状态
STATE_MUTATION：本场修改了哪些 Story State
NEXT_PRESSURE：下一场必须处理什么
```

硬规则：

- `VALUE_START == VALUE_END` 且没有新增不可替代信息 → 默认废戏。
- 没有 `NEXT_PRESSURE` → 默认没有推动。
- `SOURCE` 无法指向既有来源 → 可能是凭空事实。
- `STATE_MUTATION` 为空但场景很长 → 高概率注水。

## 8. 场景连续性事务：SCENE TRANSACTION

每场视为一次状态事务：

`READ STATE → PERFORM ACTION → CREATE CONSEQUENCE → COMMIT MUTATION`

只有写完并通过 QC 才允许 COMMIT。失败场景不能污染 Story SSoT。

写完一场内部更新：

- 人物位置
- 身体/伤势
- 已知信息
- 当前资源
- 关系变化
- 新承诺/已兑现承诺
- 未解决压力
- 时间推进

详见 `runtime/story-state.md`。

## 9. Promise–Payoff 系统

任何被明显强调的内容都会制造观众期待。包括：

- 神秘身份
- 特殊能力
- 枪/钥匙/录音/照片等道具
- 重复出现的规则
- 明显关系问题
- 某句预言/警告
- 被遮住的真相
- 片头建立的类型承诺

写入 `Promise–Payoff Ledger`：

```text
ID | PROMISE | CREATED_AT | EXPECTED_PAYOFF_WINDOW | STATUS | PAYOFF_AT | NOTES
```

状态：`OPEN / PARTIAL / PAID / DELIBERATELY_UNPAID / BROKEN`

`BROKEN` 必须修。`DELIBERATELY_UNPAID` 只能用于有意识的开放结局，并能解释为什么不回收本身产生意义。

## 10. 对白引擎

对白是行为，不是信息朗读。

每个主要人物维护 Voice Fingerprint：

```text
词汇范围：
句长倾向：
是否正面回答：
称谓方式：
压力下语言变化：
惯用重复词：
绝不会说的话：
隐藏欲望：
```

每句重要台词至少承担一种功能：争取、回避、试探、威胁、安抚、欺骗、拖延、诱导、遮掩、逼迫、交换。

中文自然度与去模板化读取 `references/natural-chinese.md`。**去 AI 味不能破坏人物信息、时代语言、专业术语和剧情因果。**

## 11. 类型路由差异

### FEATURE / SERIES
优先：因果、人物选择、关系与知识状态、承诺兑现、主题通过选择显现。

### CONCEPT_SHORT
优先：单一概念 + 一个具体的人 + 一个危机 + 一个不可逆认知时刻。读取 `references/concept-film.md`。

### VERTICAL_DRAMA
优先：情绪产品、3 秒钩子、压/放、爽点、强反转、卡点；但仍执行 Knowledge / Object / Irreversible / Promise 连续性。读取 `references/vertical-drama.md`。

“短剧直给”不等于人物把作者分析念出来；它只是信息密度更高、情绪承诺更明确。

## 12. 剧本正文格式

### 剧集 / 短剧

```text
第X集《标题》

本集人物：人物A、人物B　本集时长：约X分钟

X-1 场景地点，夜，内

△ 可拍摄环境与人物状态。

△ 人物A执行具体动作。

人物A（可表演提示）：台词。

△ 对方反制，局面改变。

人物B：台词。

△ 转折发生，并留下下一场压力。

【本集完】
```

### 电影 / 短片

场标：`INT./EXT. 地点 - 日/夜`

- 动作行以 `△` 开头。
- 只写现在时、可拍摄动作。
- 台词 `人物名（提示）：台词。`
- 括号只写可表演动作/声音/语气，不解释潜台词。
- 正文禁止出现“价值转折、鸿沟、第一幕、QC”等内部标签。

## 13. 长篇快照：MEMORY SNAPSHOT 2.0

电影每个 Sequence（推荐 2–5 场或一个明确戏剧单元）更新一次；剧集每集更新；短剧每 3–5 集或关键高潮更新。

```text
【STORY CORE】Logline / 类型承诺 / 当前主线目标
【CHARACTER STATE】身体 / 情绪 / WANT / 当前策略
【KNOWLEDGE】每个角色新增知道的事实 + 来源
【RELATIONSHIPS】关系状态变化
【OBJECTS/RESOURCES】关键物件与资源位置/归属/状态
【IRREVERSIBLE】新增不可逆事件
【PROMISE-PAYOFF】新增承诺 / 已兑现 / 超期未兑
【COMPLETED】已完成场景一句话 + 价值变化
【OPEN LOOPS】活跃线索、危机、未回答问题
【TIMELINE】当前时间与必要时间差
【NEXT PRESSURE】下一单元必须处理的压力
```

## 14. 证据式 QC：14 GATES

详细协议见 `runtime/evidence-qc.md`。

状态只能是：`PASS / FAIL / NOT_PROVEN / N/A`

### G01 CAUSALITY
主要转折由前序行动产生？

### G02 PROTAGONIST_AGENCY
主角是否主动制造关键推进并亲自承担高潮选择？

### G03 GOAL
当前阶段目标是否具体、可行动、可失败？

### G04 GAP_STRATEGY
主要冲突是否产生“预期-现实落差”，并迫使策略变化？

### G05 SCENE_VALUE
每场是否至少改变处境、关系、信息、资源、危险或选择空间之一？

### G06 NEXT_PRESSURE
场景是否给下一场留下必须处理的后果？

### G07 ESCALATION
代价是否真实升级，而非重复更大场面？

### G08 KNOWLEDGE_CONTINUITY
人物是否只使用自己已获得的信息？

### G09 PHYSICAL_CONTINUITY
位置、物件、伤势、时间、资源是否连续？

### G10 WORLD_RULE
高潮与解法是否遵守已建立规则，没有临时能力/外挂？

### G11 PROMISE_PAYOFF
明显承诺是否按期兑现、升级或有意识延期？

### G12 CHARACTER_VOICE
主要人物语言是否有策略与声音差异？

### G13 FILMABILITY
是否存在不可拍心理说明、作者总结、小说旁白替代行动？

### G14 LANGUAGE_NATURALNESS
是否存在明显中文 AI 腔、广告腔、模板化总结、罐头反应？

**PASS 必须附具体证据，例如场号 + 状态变化。没有证据只能 NOT_PROVEN。**

## 15. 反自我合理化协议

以下理由不能让 Gate 通过：

- “整体节奏不错”
- “情绪很强”
- “观众应该能理解”
- “这是类型片惯例”
- “后面可以解释”
- “人物可能知道”
- “为了戏剧性可以接受”
- “这场很好看所以保留”

合法通过证据必须是：

- 已发生的场景事实
- 明确建立的人物知识来源
- 已建立世界规则
- 已出现的物件/能力/关系状态
- 前序行动造成的结果
- 可定位的 Promise / Payoff

## 16. 单调修复：MONOTONIC REPAIR

QC 失败后按来源回修：

- 语言 → 对白/动作表达层
- 场景无变化 → Scene Contract
- 策略重复 → Gap / Tactic Shift
- 因果断裂 → 主线因果编译器
- 人物越权知道 → Knowledge Ledger
- 物件/伤势错乱 → Object/Physical State
- 伏笔超期 → Promise–Payoff
- 高潮外挂 → Capability / World Rule / Setup
- 人物动机错误 → WANT/NEED/GHOST/LIE

**禁止为了修一个局部 FAIL，引入新的无关设定或推翻已通过部分。**

修复后只重测：失败 Gate + 其依赖 Gate + 一次整体回归。

## 17. SCRIPT DOCTOR 输出协议

用户要求诊断时，先给总判决：`能用 / 有条件能用 / 不能用`。

问题按严重度：

- P0：因果/连续性/高潮根基错误
- P1：人物驱动、结构、承诺兑现重大问题
- P2：场景价值、节奏、对白、自然度问题
- P3：格式、局部措辞、小连续性

每条必须包含：

```text
问题：
证据：场号 / 原句 / 状态冲突
后果：为什么会伤害观看体验
最小修法：只改哪里
依赖影响：会不会牵动别处
```

## 18. 输出纪律

- 用户说“只改这场”：只改这场，并检查上下场接口。
- 用户说“只改对白”：不擅自改剧情事实。
- 用户说“直接写”：内部完成必要推导后直接给正文，不把工作流倾倒给用户。
- 用户给了已经锁定的大纲：不得因为模型更喜欢另一套结构就偷偷重做。
- 用户要求创意方向：可给 2–3 个明显不同的方案；一旦选定，不再反复翻案。
- 一次性交付长内容时，优先保证已完成部分闭环，不用占位符糊弄。

## 19. STOP CONDITION

当用户请求的本轮交付物已经完成，且：

- 相关 Story State 已更新
- 相关 Promise–Payoff 已更新
- 必要 14 Gates 已通过或明确暴露 NOT_PROVEN / FAIL
- 没有擅自修改用户锁定事实
- 正文不含内部工作标签

立即停止。

不得自动扩展到用户没要求的分镜、资产、镜头参数、AI 生图/视频 Prompt、宣发方案。

## 20. 运行资源

- `references/concept-film.md`：概念超短片
- `references/natural-chinese.md`：中文自然度与去 AI 味
- `references/vertical-drama.md`：竖屏短剧
- `runtime/story-state.md`：故事状态机与账本
- `runtime/evidence-qc.md`：证据式 QC 与 Gate 依赖
- `runtime/promise-payoff.md`：承诺—兑现系统
- `runtime/repair-protocol.md`：失败定位与单调修复
- `tests/regression-cases.md`：代表性回归测试

