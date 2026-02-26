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
