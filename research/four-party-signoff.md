# v3.0-publication 四方签核表

> 用途：发布前人工终审。当前未冒充任何人工签核；机器可验证项已由 `quality-gate.mjs`、`quality-audit.mjs`、302 页线上巡检和 Lighthouse 报告覆盖。

| 角色 | 签核内容 | 姓名 | 日期 | 结论（通过/退回） | 备注 |
|---|---|---|---|---|---|
| 英文母语编辑 | 151 篇英文语言质量与专名一致 |  |  |  | 见 `native-review-packet.md` |
| 中文主编 | 151 篇中文事实、结构、文风与标题 |  |  |  |  |
| 事实核查 | 151 份台账的 5 条硬事实与数字核验残留 |  |  |  | 135 条待语义核对、65 条非 Wikipedia 来源 |
| 版权 | 442 张图的作者、许可、署名与图注 |  |  |  | `image-audit.csv` 442/442 verified |

## 签核顺序

1. 英文母语编辑逐篇签 `native-review-packet.md`，通过后把 `translation_status` 改为 `native_reviewed`。
2. 中文主编抽检 30 篇并复核标题/摘要。
3. 事实核查逐条处理 `needs_review` 与 `no_source_text`，处理完再签。
4. 版权复核 442 行图片台账与线上图注。
5. 四方全部通过后，才勾选计划第 12 节“发布”四项。
