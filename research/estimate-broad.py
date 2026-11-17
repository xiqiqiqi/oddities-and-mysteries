import os,re,subprocess,yaml
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries"; GIT=r"C:\Program Files\Git\cmd\git.exe"
def z(s): return len(re.findall(r"[\u4e00-\u9fa5]",s))
def e(s): return len(re.findall(r"[A-Za-z0-9']+",s))
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
rows=[]
for ch in ["creatures","mystery","objects","places","tales"]:
    for slug in os.listdir(os.path.join(ROOT,"entries",ch)):
        curz=subprocess.run([GIT,"-C",ROOT,"show",f"HEAD:entries/{ch}/{slug}/zh.md"],capture_output=True,text=True,encoding="utf-8").stdout
        cure=subprocess.run([GIT,"-C",ROOT,"show",f"HEAD:entries/{ch}/{slug}/en.md"],capture_output=True,text=True,encoding="utf-8").stdout
        if not curz or not cure: continue
        oldz=subprocess.run([GIT,"-C",ROOT,"show",f"8573e20:entries/{ch}/{slug}/zh.md"],capture_output=True,text=True,encoding="utf-8")
        olde=subprocess.run([GIT,"-C",ROOT,"show",f"8573e20:entries/{ch}/{slug}/en.md"],capture_output=True,text=True,encoding="utf-8")
        if oldz.returncode!=0 or olde.returncode!=0: 
            rows.append((ch,slug,z(curz),e(cure),0,0,0)); continue
        zs=secs(oldz.stdout); es=secs(olde.stdout); cursecs=secs(curz)
        cand=[]
        for i,(h,b) in enumerate(zs):
            if i>=len(es): continue
            if z(b)<60: continue
            if re.match(r"^[一二三四五六七八九十]+、",h): continue
            if "来源与许可" in h: continue
            m=max([sim(b,cb) for _,cb in cursecs] or [0])
            if m>=0.55: continue
            cand.append((m,i,h,b,es[i][1]))
        cand.sort()
        chosen=[]; tot=0; tote=0
        target=max(0,1500-z(curz)-230)
        for m,i,h,b,eb in cand:
            if tot>=target: break
            chosen.append((h,b)); tot+=z(b); tote+=e(eb)
        rows.append((ch,slug,z(curz),e(cure),tot,tote,len(chosen)))
print("entries",len(rows))
print("est zh>=1500",sum(1 for r in rows if r[2]+230+r[4]>=1500))
print("est en>=1000",sum(1 for r in rows if r[3]+150+r[5]>=1000))
print("still zh",sum(1 for r in rows if r[2]<1500 and r[2]+230+r[4]<1500))
print("still en",sum(1 for r in rows if r[3]<1000 and r[3]+150+r[5]<1000))
for r in rows:
    if (r[2]<1500 and r[2]+230+r[4]<1500) or (r[3]<1000 and r[3]+150+r[5]<1000):
        print(r)
