# oddities-and-mysteries

**稀奇奇 / XIQIQI** 的开源内容仓库。

收集全世界稀奇古怪的事件、故事、物品、遗迹与生物。中文 + 英文，Markdown 为唯一内容源，网站由这个仓库自动派生。

> 稀奇不稀奇？无奇不有。

## 结构

```text
entries/
  <channel>/<slug>/
    entry.yml   # 共享元数据：频道、年代、地区、标签、来源、可信度
    zh.md       # 中文标题、摘要、正文
    en.md       # 英文标题、摘要、正文
taxonomy/
  channels.yml
  types.yml
  tags.yml
  collections.yml
schema/
  entry.schema.json
topics/
  150-topics.csv
  150-topics.md
assets/
  covers/
  inline/
```

## 频道

| channel | 中文 | 英文 | 注释 |
|---|---|---|---|
| `mystery` | 未解之谜 | Mysteries | 匪夷所思 |
| `tales` | 离奇故事 | Strange Tales | 千奇百怪 |
| `objects` | 奇物 | Objects | 奇珍异宝 |
| `places` | 奇境 | Places | 别有洞天 |
| `creatures` | 奇兽 | Creatures | 珍禽异兽 |
| `hoaxes` | 骗局档案 | Hoaxes | 以假乱真（未来频道） |

`channel` 决定条目进入哪个站点。`type` 是内容形态，只作为筛选属性。

## 新增一条内容

1. 在 `entries/<channel>/<slug>/` 建目录，slug 用小写英文和连字符。
2. 写 `entry.yml`，至少填：`channel`、`type`、`slug`、`title_zh`、`era`、`region`、`tags`、`credibility`、`sources`、`cover`、`status`、`translation_status`。
3. 写 `zh.md`，标题、摘要、正文。正文 1,500–3,000 字，场景化叙事，不用「震惊」「揭秘」。
4. 写 `en.md`。英文未完成时，`translation_status: zh_only`，网站不生成英文页。
5. 至少 2 条来源；来源台账放在正文最底部。
6. 图片放 `assets/covers/` 或 `assets/inline/`，逐张记录来源和许可。
7. 本地校验：`node ../oddities-core/scripts/validate-content.mjs`。
8. 提交 PR，等待编辑复审。

## 双语规则

- 中文默认在根路径：`/tunguska-1908/`
- 英文在 `/en/`：`/en/tunguska-1908/`
- 中英 slug 保持一致。
- 英文未完成不生成英文页，不输出 `hreflang`。
- `translation_status`：`zh_only` / `translated` / `reviewed`。

## 可信度

| 值 | 含义 | 展示 |
|---|---|---|
| `verified` | 有可靠史料或多方交叉验证 | 已核实 |
| `disputed` | 事实基本成立，解释有争议 | 争议 |
| `folklore` | 传说、都市传说、口述传统 | 传说 |
| `hoax` | 已知骗局或伪造 | 骗局 |

## 版权

- 文字、原创地图、原创图表：CC BY-SA 4.0。
- 历史图片：逐张标注来源和许可，优先公有领域、CC0、CC BY、CC BY-SA。
- 场景复原插图：可以 AI 辅助，但必须标注「场景复原，不是历史照片」。
- 不复制版权来源的原文。

## 许可

除非另有说明，本仓库内容采用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 许可。

## 相关仓库

- `oddities-core`：统一 UI、组件、i18n、构建脚本。
- `portal`：xiqiqi.com。
- `mysteries` / `tales` / `objects` / `places` / `creatures`：五个频道站。
