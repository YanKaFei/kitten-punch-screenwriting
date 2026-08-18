# Evidence QC Runtime

## 核心原则

QC 不是“自我感觉检查”。每个 Gate 只能依据可定位的剧本事实判断。

状态：
- PASS：有足够具体证据。
- FAIL：存在明确反证。
- NOT_PROVEN：可能成立，但当前证据不足。
- N/A：当前任务确实不适用。

NOT_PROVEN 不得伪装 PASS。

## Gate Evidence Card

```text
GATE：Gxx NAME
STATUS：PASS / FAIL / NOT_PROVEN / N/A
EVIDENCE：场号 + 事实/原句/状态变化
COUNTERCHECK：最强反例是什么
IMPACT：失败会造成什么
REPAIR_TARGET：若失败，只回哪一层
```

## 依赖关系

- G01 CAUSALITY → 依赖 Scene Source / 主线行动链
- G02 AGENCY → 依赖主角主动行动与高潮选择
- G04 GAP_STRATEGY → 依赖 EXPECTED/ACTUAL/TACTIC_SHIFT
- G05 SCENE_VALUE → 依赖 VALUE_START/VALUE_END
- G08 KNOWLEDGE → 依赖 Knowledge Ledger
- G09 PHYSICAL → 依赖 Object/Injury/Timeline
- G10 WORLD_RULE → 依赖 Capability + World Rule
- G11 PROMISE_PAYOFF → 依赖 Promise Ledger

## 敌意性检查

每次准备 PASS，先问：

1. 有没有一个反例能证明它只是“看起来成立”？
2. 如果删掉一句解释，这个因果还成立吗？
3. 如果观众不知道作者脑中的设定，画面本身能证明吗？
4. 这个信息角色真的得知了吗？
5. 这个能力/道具真的提前建立了吗？
6. 这个回收是否兑现了原承诺，还是换了问题？

## 剧本医生最小输出

不要求把 14 Gate 全部展示给用户。只展示失败或关键风险；内部全检即可。
