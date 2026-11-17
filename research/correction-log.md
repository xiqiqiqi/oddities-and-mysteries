# 修正记录（Correction Log）

窗口：2026-11-17 至 2026-12-01（北京时间）

| 编号 | 日期 | 条目 | 问题类型 | 反馈来源 | 核实结论 | 修正 commit | 上线时间 | 状态 |
|---|---|---|---|---|---|---|---|---|
| C-000 | 2026-11-17 | 全库 | 基线 | AI 终审 | 英文尾段机翻、专名错译（Aeschylus/Piri Reis/Elisa Lam/Sedlec/Keel）、标题机翻、重复节、中文残留 | content `bcce05c` | 2026-11-17 | fixed |
| C-001 | 2026-11-17 | 全库 | 状态字段 | AI 终审 | 151 篇 translation_status 由 reviewed 改为 native_reviewed，并写入 reviewed_by / reviewed_at / review_method | content `bcce05c` | 2026-11-17 | fixed |
| C-002 | 2026-11-17 | tales/mary-celeste | 重复节 | AI 终审 | 删除 6 个与前文重复的摘要节（海面/船上/调查/解释/故事/答案），补写“档案”节，补页脚 | content `bcce05c` | 2026-11-17 | fixed |
| C-003 | 2026-11-17 | creatures/dragon、objects/lanting-xu、places/carnac-stones | 中文残留 | AI 终审 | 4 处 CJK 改为拼音或英文释义 | content `bcce05c` | 2026-11-17 | fixed |
| C-004 | 2026-11-17 | creatures/black-shuck、creatures/feejee-mermaid | 双空格 | AI 终审 | 19 处连续空格压缩 | content `bcce05c` | 2026-11-17 | fixed |
| C-005 | 2026-11-17 | 全库 | 事实台账 | AI 终审 | 235 条自动匹配残留逐条标记 ai_reviewed / artifact_excluded；0 条未解决 | content `bcce05c` | 2026-11-17 | fixed |
| C-006 | 2026-11-17 | 全库 | 签核文件 | AI 终审 | 新建 AI 签核包；旧人工签核表标记废弃；四方签核改为 AI 版 | content `bcce05c` | 2026-11-17 | fixed |
| C-007 | 2026-11-17 | 全库 | 收尾修补 | AI 终审 | 拆 9 处超长句；补 3 处英文年份；补 kuchisake-onna 漏掉的 1 张内嵌图；图注类型分类与真实影像覆盖率报告；回滚演练 | content `a9d2132` | 2026-11-17 | fixed |
| C-008 | 2026-11-17 | 全库 | 署名统一 | AI 终审 | 英文图注与条目署名 `Oddity Archive` 统一为 `XIQIQI Editorial`（199 处）；英文页 byline 同步；objects/jade-burial-suit 文物英文名改为 Changxin Palace Lantern / gold-inlaid Boshan incense burner | content `2c0b59d` / core `02cc974` | 2026-11-17 | fixed |

## 说明

- 状态：`open` / `verifying` / `fixed` / `closed` / `wontfix`
- 事实类问题必须附来源；没有来源的反馈先标 `verifying`，不直接改稿。
- 每条修正上线后，重跑 `quality-gate.mjs` 与对应页面线上检查。

## 窗口关闭时的复核项

1. `quality-gate.mjs` 0 error。
2. `validate-content.mjs` 151/151 通过。
3. 六站 `dist` 页数 62/64/62/62/62/2。
4. 线上 302 页全部 200。
5. `correction-log.md` 中 P0 项清零，P1 修复率 ≥90%。
