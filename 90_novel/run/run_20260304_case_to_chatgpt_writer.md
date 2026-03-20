# ChatGPT 主写执行模板（固定）

【执行角色】
- 主写与整合：ChatGPT（GPT-5.x）
- 审校：glm-5
- 润色：MiniMax-M2.5
- 读者：kimi-k2.5

【指令】
按 `90_novel/prompt_multi_model_pipeline.md` 严格执行，不反问。
先生成本章正文 v1（第一人称），再自动生成 TO_GLM / TO_MINIMAX / TO_KIMI_READER 三份分发包。
禁止生成任何 `to_claude_*` 分发包。

【输入文件】
- Bible：`90_novel/inbox/series_bible_v10_station0_real_hazard.md`
- 全卷大纲：`90_novel/inbox/outline_v10_volume1_12ch.md`
- Case细纲：`90_novel/inbox/outline_v10_case01.md`
- 约束卡：`90_novel/inbox/station0_constraints_card.md`

