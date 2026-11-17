# -*- coding: utf-8 -*-
import os,re,subprocess
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries"; GIT=r"C:\Program Files\Git\cmd\git.exe"; OLD="8573e20"
def cjk(s): return len(re.findall(r"[\u4e00-\u9fa5]",s))
def secs(t):
    parts=re.split(r"^## ",t,flags=re.M)[1:]; out=[]
    for p in parts:
        h=p.split("\n")[0].strip(); b="\n".join(p.split("\n")[1:]).strip()
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
for ch,slug in [("mystery","angel-hair"),("mystery","whistle"),("places","cecil-hotel"),("objects","sword-of-goujian"),("tales","alaska-triangle")]:
    cur=open(os.path.join(ROOT,"entries",ch,slug,"zh.md"),encoding="utf-8").read()
    old=subprocess.run([GIT,"-C",ROOT,"show",f"{OLD}:entries/{ch}/{slug}/zh.md"],capture_output=True,text=True,encoding="utf-8").stdout
    curs=secs(cur)
    print("\n==",slug)
    for i,(h,b) in enumerate(secs(old)):
        if cjk(b)<50: continue
        m=max([sim(b,cb) for _,cb in curs] or [0])
        print(i,h,cjk(b),round(m,2))
