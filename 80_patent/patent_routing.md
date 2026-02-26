# Patent Routing

## 技能映射
- 选题与筛选：`30_skills/patent/skill_10_patent_topic_operator.md`
- 交底书草案：`30_skills/patent/skill_11_patent_draft_operator.md`
- 参考规范：`30_skills/patent/references/patent_style_guide.md`
- 参考样例：
  - `30_skills/patent/references/1-附件一-发明实用新型技术交底书--广域容量巡检.docx`
  - `30_skills/patent/references/1-附件一-发明实用新型技术交底书--数据流动.docx`
  - `30_skills/patent/references/1-附件一-发明实用新型技术交底书--数据流动调度策略.docx`

## 输出目录建议
- 选题池：`80_patent/run_XXX_patent_pool.md`
- 入选草案：`80_patent/run_XXX_patent_draft.md`
- 提示词模板：`80_patent/prompt_*.md`

## 执行约束
- 先跑 `skill_10` 再跑 `skill_11`。
- 未指定时自动采用最高分方向。
- 最终文稿必须带“代理人复核清单”。
