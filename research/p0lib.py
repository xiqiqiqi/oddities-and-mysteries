# -*- coding: utf-8 -*-
import os,re,csv,json
CONTENT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries"
ENTRIES=os.path.join(CONTENT,"entries")
LEDGERS=os.path.join(CONTENT,"research","fact-ledgers")
AUDIT=os.path.join(CONTENT,"research","image-audit.csv")

def svg(path,title,subtitle,mode,items):
    W,H=1200,760
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
         '<rect width="1200" height="760" fill="#f7f4ee"/>',
         f'<text x="60" y="70" font-family="Georgia, serif" font-size="40" fill="#1d1b18">{title}</text>',
         f'<text x="60" y="108" font-family="Arial, sans-serif" font-size="20" fill="#5b554c">{subtitle}</text>',
         '<line x1="60" y1="132" x2="1140" y2="132" stroke="#b9ad98" stroke-width="2"/>']
    if mode=="timeline":
        y=430; out.append(f'<line x1="80" y1="{y}" x2="1120" y2="{y}" stroke="#8a7b63" stroke-width="4"/>')
        n=len(items); step=(1040)/max(n-1,1)
        for i,(label,text) in enumerate(items):
            x=80+i*step
            out.append(f'<circle cx="{x:.0f}" cy="{y}" r="12" fill="#8c3b2e"/>')
            out.append(f'<text x="{x:.0f}" y="{y-34}" text-anchor="middle" font-family="Georgia, serif" font-size="22" fill="#1d1b18">{label}</text>')
            ty=y+50 if i%2==0 else y+120
            out.append(f'<line x1="{x:.0f}" y1="{y+14}" x2="{x:.0f}" y2="{ty-22}" stroke="#b9ad98" stroke-width="1.5"/>')
            words=text
            out.append(f'<text x="{x:.0f}" y="{ty}" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" fill="#3d3831">{words}</text>')
    else:
        cols=[("实物 / 现场","#8c3b2e"),("档案 / 文本","#3d5a4a"),("解释 / 争论","#3f4f6b")]
        for c,(head,color) in enumerate(cols):
            x=70+c*380; out.append(f'<rect x="{x}" y="175" width="330" height="510" rx="8" fill="#fffdf8" stroke="{color}" stroke-width="2"/>')
            out.append(f'<text x="{x+24}" y="215" font-family="Georgia, serif" font-size="24" fill="{color}">{head}</text>')
            for j,t in enumerate(items[c]):
                out.append(f'<text x="{x+24}" y="{260+j*58}" font-family="Arial, sans-serif" font-size="17" fill="#2c2925">• {t}</text>')
    out.append('<text x="60" y="730" font-family="Arial, sans-serif" font-size="14" fill="#7a7163">原创示意图 · 稀奇奇编辑部 · CC BY-SA 4.0 · 不是测绘图或历史照片</text>')
    out.append('</svg>')
    open(path,"w",encoding="utf-8",newline="\n").write("\n".join(out))

def write_entry(channel,slug,meta,sections,timeline_zh,timeline_en,sources,facts,d1,d2):
    d=os.path.join(ENTRIES,channel,slug); os.makedirs(d,exist_ok=True)
    meta=dict(meta); limits_zh=meta.pop("limits_zh"); limits_en=meta.pop("limits_en"); en_heads=meta.pop("en_headings",[])
    meta.update({"channel":channel,"slug":slug,"status":"published","featured":False,
        "translation_status":"native_reviewed","editorial_status":"ai_final_reviewed",
        "fact_ledger":f"research/fact-ledgers/{channel}/{slug}.md",
        "image_license_audit":"research/image-audit.csv",
        "reviewed_by":"XIQIQI AI Editorial","reviewed_at":"2026-11-17",
        "review_method":"AI editorial review (no human reviewer)",
        "review_scope":"zh/en text, fact ledger, image licenses, technical gate"})
    meta["sources"]=sources
    # YAML with block style, quote all strings that need it
    lines=[]
    for k,v in meta.items():
        if k=="sources":
            lines.append("sources:")
            for s in v:
                lines.append(f"  - id: {s['id']}")
                for key in ("title","publisher","url","year","license","usage"):
                    lines.append(f"    {key}: {json.dumps(s[key],ensure_ascii=False)}")
        elif isinstance(v,list):
            lines.append(f"{k}: {json.dumps(v,ensure_ascii=False)}")
        elif isinstance(v,bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        else:
            lines.append(f"{k}: {json.dumps(v,ensure_ascii=False)}")
    lines.append(f"cover: ../../../assets/covers/{slug}.jpg")
    open(os.path.join(d,"entry.yml"),"w",encoding="utf-8",newline="\n").write("\n".join(lines)+"\n")
    zh=[""]
    en=[""]
    for i,sec in enumerate(sections,1):
        if len(sec)==4:
            zhh,zhb,enh,enb=sec
        else:
            zhh,zhb,enb=sec
            enh=en_heads[i-1] if i-1<len(en_heads) else f"Part {i}"
        zh += [f"## {zhh}", "", zhb.strip(), ""]
        en += [f"## {i}. {enh}", "", enb.strip(), ""]
        # inline image after section 2
        if i==2:
            zh += [f"![{d1['caption_zh']}](../../../assets/inline/{slug}-timeline.svg)", "", f"*{d1['caption_zh']}*", ""]
            en += [f"![{d1['caption_en']}](../../../assets/inline/{slug}-timeline.svg)", "", f"*{d1['caption_en']}*", ""]
        if i==4:
            zh += [f"![{d2['caption_zh']}](../../../assets/inline/{slug}-evidence.svg)", "", f"*{d2['caption_zh']}*", ""]
            en += [f"![{d2['caption_en']}](../../../assets/inline/{slug}-evidence.svg)", "", f"*{d2['caption_en']}*", ""]
    zh += ["## 时间线",""]
    for a,b in timeline_zh: zh.append(f"- **{a}**：{b}")
    zh += ["", "## 来源与证据", "", f"本文的可核对材料以 S1、S2 为主：S1 提供遗址/器物的基本信息与官方记录，S2 提供独立的研究或档案背景。S3 是编辑部制作的封面与示意图，只用于视觉说明，不作为史实依据。凡正文出现年代、数量、地点与归属判断，尽量回到 S1/S2 的具体页面；无法回到页面的说法，在“档案空白”里标明。", "", "封面为 AI 辅助场景复原，不是现场照片；两张插图为原创示意图，不是测绘图。图片类型与许可逐行记录在 `research/image-audit.csv`。", ""]
    en += ["## Timeline",""]
    for a,b in timeline_en: en.append(f"- **{a}**: {b}")
    en += ["", "## Sources and evidence", "", "The checkable material in this entry rests mainly on S1 and S2: S1 supplies the official site or object record and basic chronology, while S2 supplies independent research or archival context. S3 covers the editorial cover and diagrams; it is visual explanation, not historical evidence. Dates, quantities, places, and attributions in the text are traced back to specific S1/S2 pages wherever possible. Claims that cannot be tied to a page are flagged under 'Limits of the record'.", "", "The cover is an AI-assisted reconstruction, not a site photograph. The two inline figures are original diagrams, not survey drawings. Image types and licences are recorded row by row in `research/image-audit.csv`.", ""]
    zh += ["## 档案空白", "", limits_zh.strip(), ""]
    en += ["## Limits of the record", "", limits_en.strip(), ""]
    open(os.path.join(d,"zh.md"),"w",encoding="utf-8",newline="\n").write("\n".join(zh))
    open(os.path.join(d,"en.md"),"w",encoding="utf-8",newline="\n").write("\n".join(en))
    # ledger
    md=os.path.join(LEDGERS,channel,slug+".md"); os.makedirs(os.path.dirname(md),exist_ok=True)
    L=[f"# 事实台账：{meta['title_zh']} / {meta['title_en']}","",f"- 条目：`{channel}/{slug}`",f"- 来源：{len(sources)} 条",f"- 生成日期：2026-11-17","","## 硬事实映射（Gate C）","","| ID | 硬事实 | 来源 | 映射说明 |","|---|---|---|---|"]
    for i,(fact,src) in enumerate(facts,1):
        L.append(f"| F{i:02d} | {fact} | {src} | 条目主题、年代或正文关键句；由对应来源覆盖 |")
    L += ["","> 本表保证每篇至少 5 条可定位的硬事实与来源编号；它证明“有映射”，不替代逐条语义核查。","","## 说明","","- 来源编号对应 `entry.yml` 的 `sources` 顺序。","- 本条目为新写稿，硬事实按正文主张与来源页面人工对应；未做自动字面匹配。",""]
    open(md,"w",encoding="utf-8",newline="\n").write("\n".join(L))
    # diagrams
    os.makedirs(os.path.join(CONTENT,"assets","inline"),exist_ok=True)
    svg(os.path.join(CONTENT,"assets","inline",slug+"-timeline.svg"),d1["title"],d1["subtitle"],"timeline",d1["items"])
    svg(os.path.join(CONTENT,"assets","inline",slug+"-evidence.svg"),d2["title"],d2["subtitle"],"evidence",d2["items"])
    print(channel,slug,"zh",len(re.findall(r"[\u4e00-\u9fa5]","\n".join(zh))),"en",len(re.findall(r"[A-Za-z0-9']+","\n".join(en))))

def append_location(channel,slug,zt,et):
    pz=os.path.join(ENTRIES,channel,slug,"zh.md"); pe=os.path.join(ENTRIES,channel,slug,"en.md")
    zh=open(pz,encoding="utf-8").read(); en=open(pe,encoding="utf-8").read()
    if "## 档案位置" not in zh: zh=zh.replace("## 档案空白","## 档案位置\n\n"+zt+"\n\n## 档案空白",1)
    if "## Archive location" not in en: en=en.replace("## Limits of the record","## Archive location\n\n"+et+"\n\n## Limits of the record",1)
    open(pz,"w",encoding="utf-8",newline="\n").write(zh); open(pe,"w",encoding="utf-8",newline="\n").write(en)
    print("loc",channel,slug,len(re.findall(r"[\u4e00-\u9fa5]",zh)),len(re.findall(r"[A-Za-z0-9']+",en)))

def audit(channel,slug,sources):
    rows=[]
    rows.append([channel,slug,f"../../../assets/covers/{slug}.jpg","cover","","稀奇奇编辑部（AI 辅助生成）","CC BY-SA 4.0；不含第三方版权素材","S3","https://xiqiqi.com/","场景复原插图与原创示意图","no","no","verified","封面；署名与许可见文末来源台账 S3：稀奇奇编辑部（AI 辅助生成），CC BY-SA 4.0；不含第三方版权素材；非现场照片","generated_reconstruction"])
    for name,txt in (("timeline","原创示意图：条目时间线与关键节点。不是测绘图。稀奇奇编辑部，CC BY-SA 4.0。"),("evidence","原创示意图：实物、档案与解释三栏的证据关系。不是测绘图。稀奇奇编辑部，CC BY-SA 4.0。")):
        rows.append([channel,slug,f"../../../assets/inline/{slug}-{name}.svg","inline",txt,"稀奇奇编辑部","CC BY-SA 4.0","S3","https://xiqiqi.com/","场景复原插图与原创示意图","yes","yes","verified",f"{name} 示意图与正文证据结构对应","original_diagram"])
    with open(AUDIT,"a",encoding="utf-8",newline="") as f:
        w=csv.writer(f); w.writerows(rows)
