from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = [
    root/'SKILL.md',
    root/'references'/'concept-film.md',
    root/'references'/'natural-chinese.md',
    root/'references'/'vertical-drama.md',
    root/'runtime'/'story-state.md',
    root/'runtime'/'evidence-qc.md',
    root/'runtime'/'promise-payoff.md',
    root/'runtime'/'repair-protocol.md',
    root/'tests'/'regression-cases.md',
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
text = (root/'SKILL.md').read_text(encoding='utf-8') if (root/'SKILL.md').exists() else ''
checks = {
    'display_name': '小猫揍人编剧强化 Skill' in text,
    'version': 'version: 1.0.0' in text,
    'story_state': 'STORY SSoT' in text,
    'knowledge_ledger': 'Character Knowledge Ledger' in text,
    'promise_payoff': 'Promise–Payoff' in text,
    'evidence_qc': '14 GATES' in text,
    'anti_rationalization': '反自我合理化协议' in text,
    'monotonic_repair': 'MONOTONIC REPAIR' in text,
    'stop_condition': 'STOP CONDITION' in text,
}
print('Missing files:', missing or 'NONE')
for k,v in checks.items():
    print(f'{k}:', 'PASS' if v else 'FAIL')
if missing or not all(checks.values()):
    sys.exit(1)
print('PACKAGE VALIDATION: PASS')
