# Video Topic Routing

## 选题类型与目录映射
- `jackalope_bridge`:
  - 技能目录：`30_skills/video/jackalope_bridge/`
  - 输出目录：`70_video/jackalope_bridge/`
- `ai_product_latest`:
  - 技能目录：`30_skills/video/ai_product_latest/`
  - 输出目录：`70_video/ai_product_latest/`
- `github_ai_star`:
  - 技能目录：`30_skills/video/github_ai_star/`
  - 输出目录：`70_video/github_ai_star/`

## 文件命名建议
- 选题筛选：`run_XXX_topic_pool.md`
- 成片文稿：`run_XXX_top1_script.md`
- 提示词模板：`prompt_*.md`

## 执行约束
- 同一轮任务只使用一个选题类型。
- `skill_10` 与 `skill_11` 必须使用同类型子技能。
- 未指定类型时默认 `jackalope_bridge`。
