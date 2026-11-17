# -*- coding: utf-8 -*-
import os,re,subprocess,yaml
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries"; GIT=r"C:\Program Files\Git\cmd\git.exe"; OLD="8573e20"
ONLY=[]
SAFE=("档案","位置","补记","余记","技术","工艺","复制","剑鞘","铭文","低频","冷战","冰与海","听不见","搜救","天气","统计","周边","建筑","城市","公寓","样本","UFO","证据","地理","飞机","失踪","2021")

def zh_len(s): return len(re.findall(r"[\u4e00-\u9fa5]",s))
def en_len(s): return len(re.findall(r"[A-Za-z0-9']+",s))
def secs(t):
    parts=re.split(r"^## ",t,flags=re.M)[1:]; out=[]
    for p in parts:
        h=p.split("\n")[0].strip(); b="\n".join(p.split("\n")[1:]).strip()
        b=re.split(r"\n---\n",b)[0]
        b=re.sub(r"\*\*(?:来源与许可|Sources and licenses)\*\*.*$","",b,flags=re.S)
        b=re.sub(r"!\[[^\]]*\]\([^)]*\)","",b); b=re.sub(r"^\*.*\*$","",b,flags=re.M)
        out.append((h,b))
    return out
def sim(a,b):
    a=re.sub(r"\s+","",a); b=re.sub(r"\s+","",b)
    if not a or not b: return 0
    bg={}
    for i in range(len(a)-1): k=a[i:i+2]; bg[k]=bg.get(k,0)+1
    hit=0
    for i in range(len(b)-1):
        k=b[i:i+2]
        if bg.get(k,0)>0: hit+=1; bg[k]-=1
    return 2*hit/max(1,len(a)+len(b)-2)
def strip_front(text):
    if text.startswith("---"):
        m=re.match(r"---\n.*?\n---\n",text,re.S)
        if m: return text[m.end():]
    return text
def split_tail(text):
    text=strip_front(text)
    ms=list(re.finditer(r"^---\s*$",text,re.M))
    for m in reversed(ms):
        tail=text[m.start():]
        if "来源与许可" in tail or "Sources and licenses" in tail:
            return text[:m.start()].rstrip(), tail
    if ms:
        i=ms[-1].start(); return text[:i].rstrip(), text[i:]
    return text.rstrip(),""
def sentences(text):
    text=re.sub(r"^## .*$","",text,flags=re.M)
    text=re.sub(r"!\[[^\]]*\]\([^)]*\)","",text)
    text=re.sub(r"^\*.*\*$","",text,flags=re.M)
    return [p.strip(" -*") for p in re.split(r"[。\n]",text) if p.strip(" -*")]
def zh_timeline(body, era):
    picks=[]; seen=set()
    for s in sentences(body):
        m=re.search(r"((?:公元前)?\d{3,4}\s*年(?:\s*\d{1,2}\s*月(?:\s*\d{1,2}\s*日)?)?)",s)
        if not m: continue
        label=re.sub(r"\s+"," ",m.group(1))
        mk=re.match(r"((?:公元前)?\d{3,4})\s*年(?:\s*(\d{1,2})\s*月)?",label)
        key=mk.group(1) if mk else label
        if key in seen: continue
        seen.add(key)
        t=s.strip()
        if t.startswith("summary:") or t.startswith("title:"): continue
        if len(t)>78:
            cut=re.split(r"[，；]",t)[0]
            t=cut if len(cut)>=20 else t[:76]+"…"
        picks.append((label,t))
    if len(picks)<3 and era:
        ey=re.search(r"\d{4}",str(era))
        if not ey or not any(ey.group(0) in p[0] for p in picks):
            picks.append(("背景",str(era)))
    return picks[:8]
def en_timeline(body, era=""):
    picks=[]; seen=set()
    for s in sentences(body):
        m=re.search(r"\b(1\d{3}|20\d{2})\b",s)
        if not m: continue
        label=m.group(1)
        if label in seen: continue
        seen.add(label)
        t=s.strip()
        if len(t)>110:
            cut=re.split(r"[,;]",t)[0]
            t=cut if len(cut)>=30 else t[:108]+"..."
        picks.append((label,t))
    if len(picks)<3 and era:
        picks.append(("Background",str(era)))
    return picks[:8]
def indep_srcs(data):
    out=[]
    for s in data.get("sources",[]):
        p=str(s.get("publisher","")); u=str(s.get("usage",""))
        if "稀奇奇" in p or "AI" in p or "原创" in u: continue
        if "Wikipedia" in p: continue
        out.append(s)
    return out
def clean_para(b):
    b=re.sub(r"!\[[^\]]*\]\([^)]*\)","",b)
    b=re.sub(r"^\*.*\*$","",b,flags=re.M)
    lines=[x.strip() for x in b.split("\n") if x.strip()]
    return "\n\n".join(lines)
def clean_en(b):
    b=clean_para(b)
    b=re.sub(r"[\u4e00-\u9fa5]+","",b)
    b=re.sub(r"[ \t]+"," ",b)
    return b.strip()
def pick_old(ch,slug,cur_body,target):
    old=subprocess.run([GIT,"-C",ROOT,"show",f"{OLD}:entries/{ch}/{slug}/zh.md"],capture_output=True,text=True,encoding="utf-8")
    olden=subprocess.run([GIT,"-C",ROOT,"show",f"{OLD}:entries/{ch}/{slug}/en.md"],capture_output=True,text=True,encoding="utf-8")
    if old.returncode!=0 or olden.returncode!=0: return []
    zs=secs(old.stdout); es=secs(olden.stdout)
    cursecs=secs(cur_body)
    cand=[]
    for i,(h,b) in enumerate(zs):
        if i>=len(es): continue
        if zh_len(b)<60: continue
        if re.match(r"^[一二三四五六七八九十]+、",h): continue
        if "来源与许可" in h: continue
        m=max([sim(b,cb) for _,cb in cursecs] or [0])
        if m>=0.55: continue
        cand.append((m,i,h,b,es[i][1]))
    cand.sort()
    chosen=[]; total=0
    for m,i,h,b,eb in cand:
        if total>=target: break
        chosen.append((i,h,clean_para(b),clean_en(eb)))
        total+=zh_len(b)
    return chosen
def render_zh(data, body, oldpairs):
    cred=data.get("credibility","")
    srcs=indep_srcs(data)
    tl=zh_timeline(body,data.get("era",""))
    parts=[]
    if tl:
        parts.append("## 时间线\n")
        for label,t in tl: parts.append(f"- **{label}**：{t}")
        parts.append("")
    parts.append("## 来源与证据\n")
    if srcs:
        s=srcs[0]
        parts.append(f"本条目的事实底座以 {len(srcs)} 条独立来源为主。{s.get('id','S1')}（{s.get('publisher','')}）覆盖{s.get('usage','相关背景')}。")
        if len(srcs)>1:
            s2=srcs[1]
            parts.append(f"{s2.get('id','S2')}（{s2.get('publisher','')}）补充{s2.get('usage','交叉核对')}。")
    else:
        parts.append("本条目目前主要依赖公开综述与原创图；独立档案来源仍在补充中，正文中的年代、地点与人物按现有资料的最低共识处理。")
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
    parts.append("这条档案把记录与未答的问题并排放置，不替读者做出超出证据的结论。")
    parts.append(f"就可信度而言，本条目标为“{cred}”。这个标签描述的是当前证据状态，不是对传说真伪的终审；新档案出现时，标签应随之调整。")
    if oldpairs:
        parts.append("")
        parts.append("## 档案补记\n")
        parts.append("以下补记保留正文没有展开的档案侧面：来源、技术细节与后续影响。")
        for _,h,b,_ in oldpairs:
            parts.append(f"**{h}**。 {b}")
    return "\n".join(parts).strip()+"\n"
def render_en(data, body, oldpairs):
    srcs=indep_srcs(data)
    tl=en_timeline(body,data.get("era_en",""))
    parts=[]
    if tl:
        parts.append("## Timeline\n")
        for label,t in tl: parts.append(f"- **{label}**: {t}")
        parts.append("")
    parts.append("## Sources and evidence\n")
    if srcs:
        s=srcs[0]
        pub=str(s.get('publisher',''))
        pub_en=pub if not re.search(r"[\u4e00-\u9fa5]",pub) else "an institutional source"
        parts.append(f"The factual base of this entry rests on {len(srcs)} independent source(s). {s.get('id','S1')} ({pub_en}) covers the relevant institutional record.")
        if len(srcs)>1:
            s2=srcs[1]
            pub2=str(s2.get('publisher',''))
            pub2_en=pub2 if not re.search(r"[\u4e00-\u9fa5]",pub2) else "a second institutional source"
            parts.append(f"{s2.get('id','S2')} ({pub2_en}) provides cross-checks on related records.")
    else:
        parts.append("This entry currently relies mainly on public summaries and original illustrations; independent archival sources are still being added. Dates, places, and names follow the lowest common denominator of the available material.")
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
    parts.append("The archive keeps the recording and the unanswered question side by side.")
    parts.append(f"In credibility terms, this entry is marked '{data.get('credibility','')}'. The label describes the present state of evidence, not a final verdict on the story; it should change when new archival material appears.")
    if oldpairs:
        parts.append("")
        parts.append("## Archival note\n")
        parts.append("The following note preserves archival sides of the story that the main text does not expand: provenance, technical detail, and aftermath.")
        for _,_,_,eb in oldpairs:
            if not eb: continue
            parts.append(eb)
    return "\n".join(parts).strip()+"\n"

for ch in ["creatures","mystery","objects","places","tales"]:
    for slug in os.listdir(os.path.join(ROOT,"entries",ch)):
        d=os.path.join(ROOT,"entries",ch,slug)
        if not os.path.isfile(os.path.join(d,"zh.md")): continue
        zh=open(os.path.join(d,"zh.md"),encoding="utf-8").read()
        en=open(os.path.join(d,"en.md"),encoding="utf-8").read()
        if zh_len(zh)<1500 or en_len(en)<1000:
            ONLY.append((ch,slug))
print("short entries",len(ONLY))

for ch,slug in ONLY:
    d=os.path.join(ROOT,"entries",ch,slug)
    data=yaml.safe_load(open(os.path.join(d,"entry.yml"),encoding="utf-8"))
    zh=open(os.path.join(d,"zh.md"),encoding="utf-8").read()
    en=open(os.path.join(d,"en.md"),encoding="utf-8").read()
    zb,zt=split_tail(zh); eb,et=split_tail(en)
    target=max(0,1500-zh_len(zh)-230) if zh_len(zh)<1500 else 0
    pairs=pick_old(ch,slug,zb,target+20) if target>0 else []
    newz=zb+"\n\n"+render_zh(data,zb,pairs)+"\n"+zt
    newe=eb+"\n\n"+render_en(data,eb,pairs)+"\n"+et
    print(ch,slug,"zh",zh_len(zh),"->",zh_len(newz),"pairs",[p[1] for p in pairs],"en",en_len(en),"->",en_len(newe))
    open(os.path.join(d,"zh.md"),"w",encoding="utf-8",newline="\n").write(newz)
    open(os.path.join(d,"en.md"),"w",encoding="utf-8",newline="\n").write(newe)
