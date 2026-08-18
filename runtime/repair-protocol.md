# Monotonic Repair Protocol

## 目标

修复失败，同时保护已经正确的部分。

## 步骤

1. 定位最早失败点，不从最终症状倒着乱补。
2. 判断失败层：事实 / 状态 / 因果 / 人物 / 场景 / 对白 / 语言。
3. 建立“不可破坏清单”：用户锁定项、已通过 Gate、已兑现 Promise、既有状态。
4. 只改最小必要节点。
5. 重算该节点之后受影响的状态。
6. 重测失败 Gate + 直接依赖 Gate。
7. 跑一次全局回归，确认没有新增冲突。

## 常见错误 → 根因

- 下一场人物突然知道真相 → Knowledge Ledger
- 角色突然和好 → Relationship State
- 高潮突然会新技能 → Capability Setup
- 伏笔消失 → Promise Ledger
- 连续三场追杀 → Gap/Tactic Shift 不存在
- 台词很“有道理”但不像人 → Voice + Natural Chinese
- 场景漂亮但删掉无影响 → Scene Value / Next Pressure
- 结尾主题靠旁白讲 → Theme 未通过选择落地

## 禁止修法

- 新增万能角色
- 新增未铺垫证据
- 新增一段解释前面为什么合理
- 改写所有人物动机来迁就一个漏洞
- 把 FAIL 改名成“风格选择”
