# -*- coding: utf-8 -*-
import os,re,yaml
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
PARITY="creatures/almas mystery/brine-pools mystery/fairy-circles mystery/magnetic-hill mystery/min-min-lights objects/ark-of-the-covenant objects/he-shi-bi objects/iron-pillar-delhi objects/true-cross places/carnac-stones places/jiaohe tales/aeschylus".split()
def z(s): return len(re.findall(r"[\u4e00-\u9fa5]",s))
def e(s): return len(re.findall(r"[A-Za-z0-9']+",s))
for k in PARITY:
    ch,slug=k.split("/"); pe=os.path.join(ROOT,ch,slug,"en.md"); py=os.path.join(ROOT,ch,slug,"entry.yml")
    en=open(pe,encoding="utf-8").read(); d=yaml.safe_load(open(py,encoding="utf-8"))
    if "## Timeline" in en:
        print("has timeline",k); continue
    era=d.get("era_en") or "The entry's period is described in the opening sections."
    block="## Timeline\n\n- Background: "+str(era)+"\n\n"
    if "## Sources and evidence" in en:
        en=en.replace("## Sources and evidence",block+"## Sources and evidence",1)
    else:
        en=en.rstrip()+"\n\n"+block
    open(pe,"w",encoding="utf-8",newline="\n").write(en)
    print("timeline",k,e(en))

# spring-heeled-jack: extend archive-location paragraph
pz=os.path.join(ROOT,"creatures","spring-heeled-jack","zh.md")
pe=os.path.join(ROOT,"creatures","spring-heeled-jack","en.md")
zh=open(pz,encoding="utf-8").read(); en=open(pe,encoding="utf-8").read()
zh=zh.replace("本文因此把“报纸报道过”与“确有此人”分开。","报纸上的地址彼此分散，既没有一条固定的街道，也没有一个能被反复核对的名字。这种分散本身就是记录的一部分，也是本文把它归入“未决的都市传说”而不是“有案可查的袭击”的原因。")
en=en.replace("This entry therefore separates 'the newspapers reported it' from 'a person did it'.","Neither the newspaper notices nor the later memoirs identify a consistent street, date, or name; the few addresses that appear are scattered across London and its suburbs. That scatter is itself part of the record, and it is why the case is filed here as an unresolved urban legend rather than a documented assault.")
open(pz,"w",encoding="utf-8",newline="\n").write(zh); open(pe,"w",encoding="utf-8",newline="\n").write(en)
print("spring",z(zh),e(en))

# Washington: rewrite the short 'What remains' section so it no longer resembles the source note
pz=os.path.join(ROOT,"mystery","washington-merry-go-round","zh.md")
pe=os.path.join(ROOT,"mystery","washington-merry-go-round","en.md")
zh=open(pz,encoding="utf-8").read(); en=open(pe,encoding="utf-8").read()
en=re.sub(r"## 7\. What remains\n.*?(?=\n## )", "## 7. What remains\nThe Washington case left no physical object. What survives is a paper trail: radar scope logs, radio transcripts, weather records, and the pilots' written statements. The files are held in U.S. military and civil-aviation archives, and not all of them are digitised. That is the material this entry can check; the rest of the story is later retelling.\n", en, flags=re.S)
zh=re.sub(r"## 七、剩下的\n.*?(?=\n## )", "## 七、剩下的\n华盛顿事件没有留下实物。留下来的是纸面记录：雷达荧光屏的日志、无线电通话、气象记录和飞行员的书面陈述。这些文件分别藏在美国军方和民航档案里，并未全部数字化。本文能核对的是这一层；其余部分是后来的转述。\n", zh, flags=re.S)
open(pz,"w",encoding="utf-8",newline="\n").write(zh); open(pe,"w",encoding="utf-8",newline="\n").write(en)
print("washington",z(zh),e(en))
