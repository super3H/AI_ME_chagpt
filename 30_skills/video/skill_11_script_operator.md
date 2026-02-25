# Skill 11 Router: 按选题类型分发

## 目标
将文稿生成任务分发到对应类型的 `skill_11`，保证脚本结构和选题类型一致。

## 输入
- 选题类型：`jackalope_bridge` | `ai_product_latest` | `github_ai_star`
- 来自对应 `skill_10` 的最高分选题结果。

## 分发规则
- `jackalope_bridge` -> `30_skills/video/jackalope_bridge/skill_11_script_operator.md`
- `ai_product_latest` -> `30_skills/video/ai_product_latest/skill_11_script_operator.md`
- `github_ai_star` -> `30_skills/video/github_ai_star/skill_11_script_operator.md`

## 输出目录规则
- `jackalope_bridge` -> `70_video/jackalope_bridge/`
- `ai_product_latest` -> `70_video/ai_product_latest/`
- `github_ai_star` -> `70_video/github_ai_star/`

## 强制约束
- 必须与 `skill_10` 选择的类型一致。
- 禁止在一个文稿中混用不同类型章节结构。
- 未指定类型时，默认 `jackalope_bridge`。
