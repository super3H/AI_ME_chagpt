# GitHub 长篇小说/故事 Skills 与框架清单（2026-03-06）

用途：给你的小说流水线补充“可复用的方法和工具”，不是替代你现有风格与设定。

## 先说结论（适合你当前项目）
1. 主写流程参考：`EdwardAThomson/NovelWriter`  
   链接：<https://github.com/EdwardAThomson/NovelWriter>  
   价值：多阶段写作（世界观/大纲/场景/章节）+ 多轮评审思路，和你当前多模型分工最接近。

2. 长篇工程化管理：`vkbo/novelWriter`  
   链接：<https://github.com/vkbo/novelWriter>  
   价值：把长篇拆成小文档管理，适合章节连载与版本回滚，降低上下文混乱。

3. 成稿与出版产线：`jp-fosterson/pandoc-novel`  
   链接：<https://github.com/jp-fosterson/pandoc-novel>  
   价值：把 markdown 章节一键构建成 PDF/ePub/投稿稿，适合你后续整理全集。

4. 稿件标准化呈现：`taw00/manuscript-css`  
   链接：<https://github.com/taw00/manuscript-css>  
   价值：用 CSS 将 Markdown 渲染为标准稿格式，适合读者测读与编辑审阅。

5. 研究方法库（写作策略更新）：`yingpengma/Awesome-Story-Generation`  
   链接：<https://github.com/yingpengma/Awesome-Story-Generation>  
   价值：持续跟进 Story Generation 新方法（仓库公开显示约 587 stars），用于升级你的 skill 规则。

## 如何接入你现有流水线（最小改动）
- 主写与审计分工不变（你当前 `GPT/GLM/Kimi/MiniMax` 角色保持）。
- 增加两条固定动作：
  - 每月一次：从 `Awesome-Story-Generation` 抽 3 个“可执行方法”写入你的 skill。
  - 每章一次：按 `novelWriter` 的“章节拆分+元数据”思想维护章节状态（冲突/线索/角色弧线）。

## 采纳规则（防跑偏）
- 只学“结构、流程、评审机制”，不搬运具体剧情内容。
- 你当前风格优先（第一人称、强代入、现实改编恐怖），开源项目仅作流程增强。
- 若外部方法与现有 bible 冲突，以 `series_bible` 和 `continuity_ledger` 为准。

