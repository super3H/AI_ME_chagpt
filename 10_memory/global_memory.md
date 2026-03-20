# Global Memory

## 目标
将长期有效的信息沉淀为可调用记忆，减少重复沟通与重复推理。

## 记忆分层
- 用户层：目标、偏好、禁忌、沟通风格。
- 项目层：项目目标、当前阶段、关键约束、里程碑。
- 结论层：已验证结论、适用范围、失效条件。
- 待验证层：重要假设与验证计划。

## 记忆结构模板
```md
### [Memory-ID]
- type: user | project | conclusion | hypothesis
- content:
- source: 用户明确说明 | 推断
- confidence: high | medium | low
- updated_at: YYYY-MM-DD
- valid_until: YYYY-MM-DD | none
- invalidation_trigger:
```

## 当前用户长期记忆（已写入）
### MEM-USER-20260224-LONGVIDEO
- type: user
- content: 目标是做长视频知识区 UP 主，优先产出 8-15 分钟的结构化选题与成片脚本。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-24
- valid_until: none
- invalidation_trigger: 用户明确更改赛道或内容形态

## 写入规则
- 仅写入“跨任务复用价值高”的信息。
- 明确区分“用户明确给出”与“模型推断”。
- 推断信息默认 `confidence=low/medium`，不得伪装为确定事实。

## 读取优先级
- 当前任务直接上下文 > 项目层记忆 > 用户层长期偏好 > 历史推断。
- 新输入与旧记忆冲突时，以最新且更高置信信息为准。

## 更新触发
- 用户明确修正目标/偏好时，立即覆盖旧记忆。
- 关键结论验证失败时，立刻标记失效并记录原因。
- 任务结束时，沉淀可复用方法和高价值约束。

### MEM-USER-20260224-AUTOPICK
- type: user
- content: 后续视频任务默认按评分最高的选题直接生成文稿，无需再次确认。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-24
- valid_until: none
- invalidation_trigger: 用户明确要求手动选题

### MEM-USER-20260224-PATENT-APP
- type: user
- content: 分身新增应用“专利”，后续可按专利链路执行方向筛选与交底书草案生成。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-24
- valid_until: none
- invalidation_trigger: 用户明确关闭专利应用或更改专利流程

### MEM-USER-20260224-PATENT-STYLE-3REF
- type: user
- content: 后续专利内容修改默认对齐三份参考交底书风格（广域容量巡检/数据流动/数据流动调度策略）。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-24
- valid_until: none
- invalidation_trigger: 用户明确指定新风格基线

### MEM-USER-20260224-NOVEL-APP
- type: user
- content: 分身新增应用“小说”，后续可按小说链路执行选题筛选、分章大纲和样章生成。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-24
- valid_until: none
- invalidation_trigger: 用户明确关闭小说应用或更改小说流程

### MEM-USER-20260227-NOVEL-REVISION-LEDGER
- type: user
- content: 小说写作/修订必须保留“记忆与台账”：章节文件使用版本号（如 ch01_v1/ch01_v2），每次修订输出需附变更说明，并同步更新 `90_novel/inbox/continuity_ledger.md`（人物状态/线索/伏笔/时间线），避免后续重复犯一致性错误。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-27
- valid_until: none
- invalidation_trigger: 用户明确取消台账或改用其它记忆管理方式

### MEM-USER-20260227-NOVEL-MULTI-MODEL-PIPELINE
- type: user
- content: 小说产出要按 `90_novel/prompt_multi_model_pipeline.md` 执行：GPT-5.2 负责任务分发与整合，并作为读者只看终稿输出体验报告；kimi-k2.5 负责主写；glm-5 负责总编审核（看圣经+大纲+正文输出一致性/大纲对齐/修改指令）；MiniMax-M2.5 负责编辑润色（不改事件链输出润色版正文+说明）；并在整合修订时输出 v2 + 变更说明，同时更新台账，禁止抄袭与照搬参考文本。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-27
- valid_until: none
- invalidation_trigger: 用户明确改用单模型或变更流水线

### MEM-USER-20260227-NOVEL-ANTI-AI-TONE
- type: user
- content: 小说正文需要明显降低“AI味”：避免模板化排比与套路比喻堆叠（尤其反复“像…”），减少解释性旁白替读者总结；增加具体细节与自然呼吸感；读者反馈必须引用原文定位，避免泛泛而谈。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-27
- valid_until: none
- invalidation_trigger: 用户明确允许更强的“模板化”写法或不再关注 AI 痕迹检测

### MEM-USER-20260227-NOVEL-STYLE-DAOMU-GUISHE
- type: user
- content: 小说（无限流/副本）写作希望加入《诡舍》的规则恐怖机制感，并参考《盗墓笔记》的沉浸式现场感（更身临其境、脑洞更大但不能无聊）；“审计/流程”题材要避免写成纯术语走流程。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-27
- valid_until: none
- invalidation_trigger: 用户明确更换参考风格或回到更偏“流程/报告体”的写法

### MEM-USER-20260227-NOVEL-RETARGET-HORROR
- type: user
- content: 用户明确反馈当前“审计办公室副本”不吸引也不恐怖，需要改成更沉浸、更恐怖的选题/皮肤再继续写。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-27
- valid_until: none
- invalidation_trigger: 用户明确回到审计题材或确认当前方向可继续写

### MEM-USER-20260227-NOVEL-REAL-CASE-SOURCING
- type: user
- content: 后续恐怖副本/案件要求“取材自现实案件类型”，但必须彻底虚构化（不写真实案件名称、真实地名、真实人物），并据此重写圣经与大纲；该工作由 glm-5 负责，你（GPT）只作为读者做体验反馈。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-27
- valid_until: none
- invalidation_trigger: 用户明确取消“现实案件类型取材”约束或更换分工

### MEM-USER-20260227-NOVEL-REVIEW-EVERY-VERSION
- type: user
- content: 每次写完一个正文版本（vN）都必须立刻完成评鉴并落盘；当前分工为：GPT-5.2 作为读者（只看正文出体验报告）、glm-5 做总编审核、MiniMax-M2.5 做编辑润色说明与不确定点；未完成评鉴不得进入下一章或下一轮改稿。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-27
- valid_until: none
- invalidation_trigger: 用户明确允许跳过评鉴或改用单模型

### MEM-USER-20260227-AI-DETECT-ZHUQUE
- type: user
- content: 用户使用“朱雀AI检测助手”（Tencent Matrix AI Detect 报告）对小说文本做 AIGC 值检测，并以降低检测出的 AI 痕迹作为优化目标之一。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-02-27
- valid_until: none
- invalidation_trigger: 用户不再使用该检测或更换检测工具

### MEM-OPS-20260227-NOVEL-ANTI-AI-DETECTORS
- type: assistant
- content: 为降低 AI 检测命中率与“模板感”，优先改写“报告/清单/编号列表”类段落为更像手写底稿的自然表达；同时清理异常 Markdown 产物（如误插入的图片链接/路径），并统一倒计时等格式避免机械重复。
- source: 结合用户目标与朱雀检测分段特征的工作约束
- confidence: medium
- updated_at: 2026-02-27
- valid_until: none
- invalidation_trigger: 用户明确要求保留更强的表格/清单体或不再参考 AI 检测结果

### MEM-USER-20260319-AUTO-AVATAR-RESOLUTION
- type: user
- content: 当用户只说“执行某个功能分身”时，应由系统自动根据分身名、别名、父目录路由和项目 manifest 寻找对应 skill 并执行，不要求用户每次手动指定 skill 文件。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-03-19
- valid_until: none
- invalidation_trigger: 用户明确要求改回手动指定 skill 或禁用自动寻址

### MEM-USER-20260319-FINANCE-AVATAR
- type: user
- content: 分身新增应用“金融”，后续用户点名“金融分身/财经分身/投资分身”时，默认走 `60_finance/finance_routing.md` 和 `30_skills/finance/` 下的技能链。
- source: 用户明确说明
- confidence: high
- updated_at: 2026-03-19
- valid_until: none
- invalidation_trigger: 用户明确关闭金融分身或改用其它金融执行链
