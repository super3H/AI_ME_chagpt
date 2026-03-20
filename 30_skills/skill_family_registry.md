# Skill Family Registry

这个文件定义“父目录 -> 技能族”的默认映射，解决还没有单独 `*_routing.md` 时的继承问题。

## 解析原则
- 先看最近父目录的显式声明。
- 没有显式声明时，按技能族默认链路执行。
- 技能族只定义默认工作方式，不覆盖用户的当前明确要求。

## 功能分身别名映射
用于“用户只说分身名，不给路径”的场景。

- `视频分身` / `视频` / `长视频`
  - 解析到成熟领域 `video`
- `专利分身` / `专利`
  - 解析到成熟领域 `patent`
- `小说分身` / `写小说` / `无限流`
  - 解析到成熟领域 `novel`
- `金融分身` / `金融` / `财经分身` / `投资分身`
  - 解析到成熟领域 `finance`
- `应用分身` / `工具分身` / `原型分身`
  - 解析到技能族 `application`
- `产品分身` / `产品`
  - 解析到技能族 `product`
- `研究分身` / `调研分身` / `分析分身`
  - 解析到技能族 `research`
- `写作分身` / `内容分身`
  - 解析到技能族 `writing`

如果一个分身名同时命中多个候选，优先级为：
1. 成熟领域
2. 具体项目 manifest
3. 通用技能族

## 技能族映射

### `core`
- 适用：所有任务的基础底座。
- 默认技能链：
  - `30_skills/core/skill_01_structuring_operator.md`
  - `30_skills/core/skill_02_causal_chain_operator.md`
  - `30_skills/core/skill_04_risk_evaluation_operator.md`
  - `30_skills/core/skill_05_compression_operator.md`

### `application`
- 适用：工具、原型、工作流应用、自动化项目。
- 默认目标：先定义输入输出，再定义处理链路和交付形态。
- 默认技能链：
  - `30_skills/core/skill_01_structuring_operator.md`
  - `30_skills/core/skill_03_model_abstraction_operator.md`
  - `30_skills/core/skill_04_risk_evaluation_operator.md`
  - `30_skills/core/skill_05_compression_operator.md`

### `product`
- 适用：产品方案、需求定义、路线图、指标设计。
- 默认目标：围绕用户价值、场景闭环、指标和优先级做判断。
- 默认技能链：
  - `30_skills/core/skill_01_structuring_operator.md`
  - `30_skills/core/skill_03_model_abstraction_operator.md`
  - `30_skills/core/skill_04_risk_evaluation_operator.md`
  - `30_skills/core/skill_05_compression_operator.md`

### `research`
- 适用：调研、验证、证据梳理、假设筛选。
- 默认目标：把问题拆成假设、证据、验证路径。
- 默认技能链：
  - `30_skills/core/skill_01_structuring_operator.md`
  - `30_skills/core/skill_02_causal_chain_operator.md`
  - `30_skills/core/skill_04_risk_evaluation_operator.md`
  - `30_skills/core/skill_05_compression_operator.md`

### `writing`
- 适用：通用写作、内容草拟、表达优化。
- 默认目标：先定结构和约束，再生成内容，再压缩提纯。
- 默认技能链：
  - `30_skills/core/skill_01_structuring_operator.md`
  - `30_skills/core/skill_05_compression_operator.md`

## 已显式注册的成熟领域
- `finance`：以 `60_finance/finance_routing.md` 为准。
- `video`：以 `70_video/topic_routing.md` 为准。
- `patent`：以 `80_patent/patent_routing.md` 为准。
- `novel`：以 `90_novel/novel_routing.md` 为准。
