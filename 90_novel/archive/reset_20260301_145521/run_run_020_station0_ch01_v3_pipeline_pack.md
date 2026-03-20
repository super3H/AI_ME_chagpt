# run_020（Station 0 / ch01_v3）多模型流水线包

本轮目标：
- 按“故事惊悚恐怖”重做核心设定（弱规则、强剧情选择、强现实回波）。
- 由三模型按身份产出：主写/总编审核/编辑润色，并落盘到固定路径。

输入源（本轮唯一权威）：
- Series Bible：`90_novel/inbox/series_bible_v6_station0_story_horror.md`
- Outline：`90_novel/inbox/outline_v6_station0_story_horror.md`

输出物（必须落盘）：
- WRITER(kimi2.5)：`90_novel/reviewed/station0_ch01_v3_kimi.md`
- AUDIT(glm5)：`90_novel/inbox/feedback_station0_ch01_glm_v3.md`
- EDITOR(minimax)：`90_novel/reviewed/station0_ch01_v3_clean.md` + `90_novel/inbox/feedback_station0_ch01_minimax_v3.md`
- GPT(reader)：`90_novel/inbox/feedback_station0_ch01_gpt_v3.md`
- Bundle：`90_novel/inbox/feedback_station0_ch01_v3_bundle.md`

硬约束：
- 取材只写“地铁火灾/踩踏事故”的类型结构，细节彻底虚构化；不得出现真实案件名称/真实地名/真实人物。
- 恐怖要“故事化”：空间、物件、人，少条款；规则只让读者感到“它在咬你”，不要做上墙制度宣讲。
- 本章必须出现：同号票据冲突/监控10秒纯黑/日志缺页/口供模板化+锚点/结尾现实回波/关键二选一选择（投票定版本）。
- 去AI味：少模板句，少对称排比，少连续比喻；靠动作和具体物理细节。

