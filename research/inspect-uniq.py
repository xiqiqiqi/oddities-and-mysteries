import os,re,subprocess
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries"; GIT=r"C:\Program Files\Git\cmd\git.exe"; OLD="8573e20"
def cjk(s): return len(re.findall(r"[\u4e00-\u9fa5]",s))
def sections(t):
    parts=re.split(r"^## ",t,flags=re.M)[1:]; out=[]
    for p in parts:
        lines=p.split("\n"); out.append((lines[0].strip(),"\n".join(lines[1:]).strip()))
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
    curs=sections(cur)
    print("\n=====",ch,slug,"current",cjk(cur),"=====")
    for h,b in sections(old):
        if cjk(b)<60: continue
        m=max([sim(b,cb) for _,cb in curs] or [0])
        print(f"\n--- [{h}] sim={m:.2f} chars={cjk(b)} ---\n{b[:900]}")
