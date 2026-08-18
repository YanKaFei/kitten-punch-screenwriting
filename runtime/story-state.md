# Story State Runtime

## 目的

把长篇剧本从“模型记得大概”升级为“状态可核对”。剧情事实只允许通过场景事务改变。

## 1. Character State

```yaml
character:
  name: ""
  location: ""
  physical_state: []
  emotional_state: ""
  want_now: ""
  tactic_now: ""
  capability_established: []
  limits: []
```

## 2. Character Knowledge Ledger

```text
FACT_ID | FACT | CHARACTER | SOURCE_SCENE | SOURCE_METHOD | CERTAINTY | CAN_ACT_ON
```

SOURCE_METHOD：亲眼看见 / 被告知 / 推理 / 偷听 / 文件 / 误导。

规则：
- 没有来源的知识不得进入角色行动。
- 角色推理出来的事实必须区分“知道”与“猜测”。
- 谎言、误导、误判不能被模型自动当真相。

## 3. Relationship State

```text
A | B | CURRENT_STATE | POWER_BALANCE | TRUST | DEBT | LAST_CHANGE | CAUSE
```

关系不能因“下一场需要温柔/敌对”自动跳变。

## 4. Object / Resource Ledger

```text
ITEM | OWNER/HOLDER | LOCATION | CONDITION | LAST_SEEN | FUNCTION | STATUS
```

关键物件必须满足：出现有来源、移动有过程、损坏有后果、丢失后不能自动回来。

## 5. Injury / Physical Continuity

记录伤势部位、严重度、发生时间、已接受处理、对行动限制。若短时间跨越不支持恢复，不允许下一场自动痊愈。

## 6. World Rule Ledger

```text
RULE_ID | RULE | ESTABLISHED_AT | EXCEPTIONS | CONSEQUENCE | USED_AT
```

高潮新规则若此前未建立，默认 DEUS_EX_MACHINA 风险。

## 7. Irreversible Event Ledger

死亡、公开身份、证据曝光、重大背叛、关键物毁坏、法律/社会层面不可撤销结果写入此表。

任何后续“恢复原状”必须有足够成本与前序铺垫。

## 8. Timeline

维护：故事日期/相对第几天、昼夜、路程、等待、伤势恢复、工作日/节日等必要时间约束。

## 9. Scene Transaction

写场景前：读取相关 State。

写完场景后先生成暂存 Mutation：

```text
KNOWLEDGE +:
RELATIONSHIP Δ:
OBJECT Δ:
PHYSICAL Δ:
WORLD_RULE +:
IRREVERSIBLE +:
PROMISE +/PAYOFF:
TIMELINE Δ:
```

通过必要 QC 后才 COMMIT。
