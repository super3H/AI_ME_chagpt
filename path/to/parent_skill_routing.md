# Parent Skill Routing

## 目标
当用户指定某个文件、目录或“调用 parent 目录下文件”时，先解析父目录的执行上下文，再决定要走哪条技能链。

## 解析优先级
1. 当前轮用户明确指定的目标、流程或技能。
2. 文件最近父目录中的 `PROJECT_MANIFEST.md`。
3. 文件最近父目录中的 `routing.md` / `*_routing.md`。
4. `30_skills/skill_family_registry.md` 中的技能族默认链路。
5. 根级公共基座：
   - `00_identity/core_identity.md`
   - `10_memory/global_memory.md`
   - `20_rules/global_rules.md`
   - `execution_protocol.md`
   - `model_execution_strategy.md`

## 无路径时的分身自动寻址
当用户只给“功能分身名”而不给路径时，执行顺序改为：

1. 先将分身名映射到技能族、成熟领域或具体项目。
2. 若命中成熟领域：
   - `finance` -> `60_finance/finance_routing.md`
   - `video` -> `70_video/topic_routing.md`
   - `patent` -> `80_patent/patent_routing.md`
   - `novel` -> `90_novel/novel_routing.md`
3. 若命中具体项目：
   - 读取 `40_projects/<project>/PROJECT_MANIFEST.md`
4. 若只命中通用技能族：
   - 按 `30_skills/skill_family_registry.md` 执行默认链路
5. 若都未命中：
   - 根据任务语义选最接近的技能族，并显式说明这是回退解析

默认目标不是“等用户给路径”，而是“先自动完成一次可解释的寻址”。

## 目录到路由文件的映射
- `60_finance/**`
  - 先读：`60_finance/finance_routing.md`
  - 再走：`30_skills/finance/skill_10_*` -> `skill_11_*`
- `70_video/**`
  - 先读：`70_video/topic_routing.md`
  - 再按子目录匹配：`30_skills/video/<topic_type>/`
- `80_patent/**`
  - 先读：`80_patent/patent_routing.md`
  - 再走：`30_skills/patent/skill_10_*` -> `skill_11_*`
- `90_novel/**`
  - 先读：`90_novel/novel_routing.md`
  - 再走：对应小说技能链
- `40_projects/<project>/**`
  - 先读：`40_projects/<project>/PROJECT_MANIFEST.md`
  - 若没有 manifest，则回退到技能族注册表

## 对新分身的要求
每个新分身项目至少补一个 `PROJECT_MANIFEST.md`，否则 parent 目录只能走默认技能族，无法表达该项目的独有规则。

## 最小 Manifest 结构
```md
# PROJECT_MANIFEST

- project_name:
- parent_skill_family:
- primary_skills:
- input_dirs:
- output_dirs:
- execution_rules:
- fallback_rules:
```

## 当前约定
- 以后如果你让我处理某个 parent 目录里的文件，我先读取该 parent 的 manifest 或 routing，再执行对应 skill。
- 如果 parent 没有单独声明，我按最近技能族的默认链路处理，不把文件当成脱离上下文的孤岛。
- 以后如果你只说“执行某个功能分身”，我先做分身自动寻址，再进入对应 skill，不要求你每次手动指定 skill 文件。
