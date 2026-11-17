import os, re, subprocess, json, statistics
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries"
GIT=r"C:\Program Files\Git\cmd\git.exe"
OLD="8573e20"

def cjk(s): return len(re.findall(r"[\u4e00-\u9fa5]", s))
def sections(text):
    parts=re.split(r"^## ", text, flags=re.M)[1:]
    out=[]
    for p in parts:
        lines=p.split("\n")
        head=lines[0].strip()
        body="\n".join(lines[1:]).strip()
        body=re.sub(r"!\[[^\]]*\]\([^)]*\)","",body)
        body=re.sub(r"^\*.*\*$","",body,flags=re.M)
        out.append((head,body))
    return out
def sim(a,b):
    a=re.sub(r"\s+","",a); b=re.sub(r"\s+","",b)
    if not a or not b: return 0
    bg={}
    for i in range(len(a)-1):
        k=a[i:i+2]; bg[k]=bg.get(k,0)+1
    hit=0
    for i in range(len(b)-1):
        k=b[i:i+2]
        if bg.get(k,0)>0:
            hit+=1; bg[k]-=1
    return 2*hit/max(1,len(a)+len(b)-2)

rows=[]
for ch in ["creatures","mystery","objects","places","tales"]:
    d=os.path.join(ROOT,"entries",ch)
    for slug in os.listdir(d):
        p=os.path.join(d,slug,"zh.md")
        if not os.path.isfile(p): continue
        cur=open(p,encoding="utf-8").read()
        zc=cjk(cur)
        old=subprocess.run([GIT,"-C",ROOT,"show",f"{OLD}:entries/{ch}/{slug}/zh.md"],capture_output=True,text=True,encoding="utf-8")
        if old.returncode!=0: continue
        olds=sections(old.stdout)
        curs=sections(cur)
        uniq=[]
        for h,b in olds:
            if cjk(b)<60: continue
            m=max([sim(b,cb) for _,cb in curs] or [0])
            if m<0.55: uniq.append((h,b,m))
        rec=sum(cjk(b) for _,b,_ in uniq)
        rows.append((ch,slug,zc,rec,zc+rec,len(uniq)))
rows.sort(key=lambda x:x[2])
print("short entries",sum(1 for r in rows if r[2]<1500))
print("recoverable to >=1500",sum(1 for r in rows if r[2]<1500 and r[4]>=1500))
print("recoverable to >=1400",sum(1 for r in rows if r[2]<1500 and r[4]>=1400))
print("median current",statistics.median([r[2] for r in rows]),"median recover",statistics.median([r[4] for r in rows]))
for r in rows[:40]: print(r)
