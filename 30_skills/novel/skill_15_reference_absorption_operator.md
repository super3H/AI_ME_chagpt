# Skill 15: Reference 结构吸收算子（小说写作：诡舍/死亡万花筒/末日乐园等）

目的：把 `30_skills/novel/references/` 里的参考书“读成方法”，而不是读成梗概。输出一份可执行的写作规律，并把规律落到 Station 0 的大纲/分章/正文动作上。

硬约束：
- 只学结构与手法，不抄原句，不复刻独特细节，不影射可检索真实案件。
- 采用“结构抽样”（开篇/中段/收束）即可，不强制逐字通读全本。
- 最终必须产出：可复用模板 + 本次写作的落地清单（本章/本案怎么用）。

## 输入
- 参考书列表：`30_skills/novel/references/`
- 当前 Series Bible：`90_novel/inbox/series_bible_v9_station0_case_horror.md`
- 当前一致性台账：`90_novel/inbox/continuity_ledger_station0.md`
- 当前 outline（可选）：`90_novel/inbox/outline_v9_station0_ch01.md`

## 输出
1) `90_novel/inbox/reference_digest_*.md`
2) “单章闭环”自查清单（写在 digest 末尾）
3) 对 outline/台账的增量修订建议（如果发现缺字段）

## 执行步骤（结构抽样法）
### Step 1: 每本书抓 3 个点（各 1 段即可）
- 开篇：如何在 300-800 字内立住“异常”和“代入”。
- 推进：如何用动作/信息差把人往前推，而不是解释设定。
- 收束：如何交付一个阶段性闭环，并留下回声/钩子。

### Step 2: 给每本书写“3 条可执行动作”
示例写法（不要写空话）：
- “用一个具体异常开场：味道/磨损/缺位编号 -> 我去确认 -> 异常升级”
- “信息差只给够用：老手一句话逼新人行动，不写教程”
- “收束必须落在一个动作：归位/封口/打孔/装回”

### Step 3: 把动作落到 Station 0（必须）
- 写一个“本章落地表”：
  - 异常锚点是什么（物件/味道/缺位）
  - 我犯的第一个小错是什么（代价小）
  - 我被逼站位的升级点是什么（代价大）
  - 解决动作是什么（可验证）
  - 回声点是什么（具体、难摆脱）

## 编码注意（Windows/中文 txt）
参考书可能包含 GBK/UTF-8。抽样读取时：
- `诡舍.txt` 通常需要 GBK（CP936）读取。
- 其他多数为 UTF-8。
如果出现乱码：改用正确编码再抽样，不要硬读。

## GitHub 补充输入（新增）
- 方法库：`30_skills/novel/references/github_novel_longform_skill_shortlist.md`

执行要求：
- 每次做 `reference_digest` 时，至少从该清单选 1 个“流程型方法”并落到本章动作。
- 只吸收流程与结构，不引入外部项目中的具体剧情或人物设定。
- 若与现有 `series_bible` 冲突，以本地 bible/outline/ledger 为准。
