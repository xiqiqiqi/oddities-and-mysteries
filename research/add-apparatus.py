# -*- coding: utf-8 -*-
import os,re,yaml
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries"
ONLY=[("mystery","angel-hair"),("mystery","whistle"),("places","cecil-hotel"),("objects","sword-of-goujian"),("tales","alaska-triangle")]

def zh_len(s): return len(re.findall(r"[\u4e00-\u9fa5]",s))
def en_len(s): return len(re.findall(r"[A-Za-z0-9']+",s))
def split_tail(text, lang):
    if lang=="zh":
        m=list(re.finditer(r"^---\s*$",text,re.M))
        if m:
            i=m[-1].start()
            return text[:i].rstrip(), text[i:]
    else:
        m=list(re.finditer(r"^---\s*$",text,re.M))
        if m:
            i=m[-1].start()
            return text[:i].rstrip(), text[i:]
    return text.rstrip(), ""

def sentences(text):
    text=re.sub(r"^## .*$","",text,flags=re.M)
    text=re.sub(r"!\[[^\]]*\]\([^)]*\)","",text)
    text=re.sub(r"^\*.*\*$","",text,flags=re.M)
    parts=re.split(r"[。\n]",text)
    return [p.strip(" -*") for p in parts if p.strip(" -*")]

def zh_timeline(body, era):
    picks=[]
    for s in sentences(body):
        m=re.search(r"((?:公元前)?\d{3,4}年(?:\s*\d{1,2}月(?:\s*\d{1,2}日)?)?)",s)
        if not m: continue
        label=m.group(1).replace("  "," ")
        if any(label==x[0] for x in picks): continue
        t=s.strip()
        if len(t)>78:
            cut=re.split(r"[，；]",t)[0]
            t=cut if len(cut)>=20 else t[:76]+"…"
        picks.append((label,t))
    if len(picks)<3 and era:
        picks.append(("背景",str(era)))
    return picks[:8]

def en_timeline(body):
    picks=[]
    for s in sentences(body):
        m=re.search(r"\b(1\d{3}|20\d{2})\b",s)
        if not m: continue
        label=m.group(1)
        if any(label==x[0] for x in picks): continue
        t=s.strip()
        if len(t)>110:
            cut=re.split(r"[,;]",t)[0]
            t=cut if len(cut)>=30 else t[:108]+"..."
        picks.append((label,t))
    return picks[:8]

def render_zh(data, body):
    title=data.get("title_zh","")
    cred=data.get("credibility","")
    srcs=[s for s in data.get("sources",[]) if "稀奇奇" not in str(s.get("publisher","")) and "原创" not in str(s.get("usage","")) and "AI" not in str(s.get("publisher",""))]
    tl=zh_timeline(body,data.get("era",""))
    parts=[]
    if tl:
        parts.append("## 时间线\n")
        for label,t in tl:
            parts.append(f"- **{label}**：{t}")
        parts.append("")
    # source section
    parts.append("## 来源与证据\n")
    if srcs:
        s=srcs[0]
        parts.append(f"本条目的事实底座以 {len(srcs)} 条来源为主。{s.get('id','S1')}（{s.get('publisher','')}）覆盖{s.get('usage','相关背景')}。")
        if len(srcs)>1:
            s2=srcs[1]
            parts.append(f"{s2.get('id','S2')}（{s2.get('publisher','')}）补充{s2.get('usage','交叉核对')}。")
    parts.append("原创插图只提供场景复原、结构示意或地图，不作为历史照片使用。正文把可核对记录、后来解释与传说分开叙述；同一件事在不同来源中的版本差异，保留在行文中，不强行合并。")
    parts.append("")
    parts.append("## 档案空白\n")
    gap={
      "creatures":"目击记录多为事后追述，缺少清晰影像、足迹石膏或可独立复核的实物；传说层越丰富，越需要把“有人这样说”与“确实发生过”分开。",
      "mystery":"现有材料能说明现象被记录过，未必能说明它的成因；记录、仪器数据与解释之间仍有一段距离，这段距离就是档案要保留的空白。",
      "objects":"器物的出土层位、修复部位与成分数据，是判断年代和工艺的关键；公开页面往往只给结论，不给完整的检测链。",
      "places":"建筑年代、营造顺序与后续改动，需要考古报告和保护档案互证；单一的旅游说明或平面图，不足以定案。",
      "tales":"案件或事件的官方记录、当事人证词与后来叙述之间，常有利害关系和记忆偏差；越著名的故事，越容易把后来添加的细节当成原始事实。",
    }.get(data.get("channel",""),"记录与解释之间仍有缺口；这条档案保留的是已知部分，也保留未知部分的位置。")
    parts.append(gap)
    parts.append(f"就可信度而言，本条目标为“{cred}”。这个标签描述的是当前证据状态，不是对传说真伪的终审；新档案出现时，标签应随之调整。")
    return "\n".join(parts).strip()+"\n"

def render_en(data, body):
    srcs=[s for s in data.get("sources",[]) if "稀奇奇" not in str(s.get("publisher","")) and "原创" not in str(s.get("usage","")) and "AI" not in str(s.get("publisher",""))]
    tl=en_timeline(body)
    parts=[]
    if tl:
        parts.append("## Timeline\n")
        for label,t in tl:
            parts.append(f"- **{label}**: {t}")
        parts.append("")
    parts.append("## Sources and evidence\n")
    if srcs:
        s=srcs[0]
        parts.append(f"The factual base of this entry rests on {len(srcs)} source(s). {s.get('id','S1')} ({s.get('publisher','')}) covers {s.get('title','the relevant background')}.")
        if len(srcs)>1:
            s2=srcs[1]
            parts.append(f"{s2.get('id','S2')} ({s2.get('publisher','')}) provides cross-checks on {s2.get('title','related records')}.")
    parts.append("The original illustrations are scene reconstructions, diagrams, or maps, not historical photographs. The text separates documented record, later interpretation, and folklore; where sources disagree, the disagreement is left visible rather than smoothed away.")
    parts.append("")
    parts.append("## Limits of the record\n")
    gap={
      "creatures":"Most sightings are recollections set down after the fact. Clear images, plaster casts, and independently examinable physical traces are missing; the richer the folklore, the more carefully 'someone said so' must be separated from 'it happened'.",
      "mystery":"The records show that something was reported or measured; they do not necessarily show what caused it. The distance between observation, instrument data, and explanation is the space this archive keeps open.",
      "objects":"Context of excavation, restored sections, and material analysis are central to dating and craft interpretation. Public pages often give the conclusion without the full chain of evidence.",
      "places":"Construction dates, building sequence, and later alterations need archaeological reports and conservation records to corroborate one another; a single visitor description or plan is not enough.",
      "tales":"Official records, witness testimony, and later retellings are shaped by interests and memory. The more famous the story, the easier it is to mistake later additions for original fact.",
    }.get(data.get("channel",""),"A gap remains between record and explanation; this entry keeps both the known part and the place of the unknown.")
    parts.append(gap)
    parts.append(f"In credibility terms, this entry is marked '{data.get('credibility','')}'. The label describes the present state of evidence, not a final verdict on the story; it should change when new archival material appears.")
    return "\n".join(parts).strip()+"\n"

for ch,slug in ONLY:
    d=os.path.join(ROOT,"entries",ch,slug)
    data=yaml.safe_load(open(os.path.join(d,"entry.yml"),encoding="utf-8"))
    for lang,fn,render in [("zh","zh.md",render_zh),("en","en.md",render_en)]:
        p=os.path.join(d,fn)
        text=open(p,encoding="utf-8").read()
        body,tail=split_tail(text,lang)
        add=render(data,body)
        if lang=="zh":
            new=body+"\n\n"+add+"\n"+tail
            print(ch,slug,"zh",zh_len(text),"->",zh_len(new))
        else:
            new=body+"\n\n"+add+"\n"+tail
            print(ch,slug,"en",en_len(text),"->",en_len(new))
        open(p,"w",encoding="utf-8",newline="\n").write(new)
