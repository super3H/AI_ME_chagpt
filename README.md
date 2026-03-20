# AI_ME

`AI_ME` 是一个面向多分身协作的个人 AI 工作台仓库。当前已经落地了金融、视频、专利、小说四个成熟方向，并预留了 `application`、`product`、`research`、`writing` 等后续分身入口。

## 目录结构
- `00_identity/`: 核心身份定义。
- `10_memory/`: 长期记忆与用户偏好。
- `20_rules/`: 全局规则与约束。
- `30_skills/`: 技能层，按领域拆分。
- `40_projects/`: 具体项目或原型应用。
- `60_finance/`: 金融方向的运行产物与路由。
- `70_video/`: 视频方向的运行产物与路由。
- `80_patent/`: 专利方向的运行产物与路由。
- `90_novel/`: 小说方向的运行产物与路由。
- `path/`: 路径和继承协议。

## 当前执行基座
- 身份基线：`00_identity/core_identity.md`
- 全局规则：`20_rules/global_rules.md`
- 执行协议：`execution_protocol.md`
- 策略选择：`model_execution_strategy.md`
- 技能族注册：`30_skills/skill_family_registry.md`
- 父目录继承规则：`path/to/parent_skill_routing.md`

## 父目录 Skill 继承规则
当用户点名一个文件或目录时，不直接把它当成孤立文件处理，而是按下面顺序解析：

1. 用户在当前轮的明确指令。
2. 目标文件最近父目录下的 `PROJECT_MANIFEST.md`。
3. 最近父目录下的 `*_routing.md` 或 `routing.md`。
4. `30_skills/skill_family_registry.md` 中定义的技能族。
5. 根级公共基座：`00_identity` + `10_memory` + `20_rules` + `execution_protocol.md`。

这条规则用于保证“调用 parent 目录下文件时，应执行 parent 对应的 skill”。

## 功能分身自动寻址
当用户没有给具体文件路径，只说“执行某个功能分身”时，默认也不等待补充说明，而是主动做一次分身寻址：

1. 先按分身名、别名、任务关键词匹配 `30_skills/skill_family_registry.md`。
2. 命中成熟领域时，直接读取对应 `*_routing.md`。
3. 命中具体项目时，优先读取该项目的 `PROJECT_MANIFEST.md`。
4. 都没有命中时，回退到最接近的技能族默认链路。

目标是让“你说分身名，我自动找 skill 并执行”成为默认行为。

## 已有领域映射
- `60_finance/**` -> `60_finance/finance_routing.md`
- `70_video/**` -> `70_video/topic_routing.md`
- `80_patent/**` -> `80_patent/patent_routing.md`
- `90_novel/**` -> `90_novel/novel_routing.md`
- `40_projects/<project>/**` -> 优先读取该项目下的 `PROJECT_MANIFEST.md`

## 新分身接入建议
后续新增分身时，按最小规范接入，避免目录长出来以后失控：

1. 在 `30_skills/<family>/` 放技能或技能族说明。
2. 在 `40_projects/<project>/` 新建项目目录。
3. 为项目补一个 `PROJECT_MANIFEST.md`，至少声明：
   - `parent_skill_family`
   - `primary_skills`
   - `input_dirs`
   - `output_dirs`
   - `execution_rules`
4. 如果该方向已经稳定，再补领域级 `*_routing.md`。

模板见：`40_projects/project_manifest_template.md`
