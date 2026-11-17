import os,re
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
def z(s): return len(re.findall(r"[\u4e00-\u9fa5]",s))
def e(s): return len(re.findall(r"[A-Za-z0-9']+",s))
zs=[]; es=[]
for ch in os.listdir(ROOT):
    d=os.path.join(ROOT,ch)
    if not os.path.isdir(d): continue
    for slug in os.listdir(d):
        p=os.path.join(d,slug,"zh.md")
        if not os.path.isfile(p): continue
        zh=open(p,encoding="utf-8").read(); en=open(os.path.join(d,slug,"en.md"),encoding="utf-8").read()
        if z(zh)<1500: zs.append((ch,slug,z(zh)))
        if e(en)<1000: es.append((ch,slug,e(en)))
print("zh<1500",len(zs)); print("en<1000",len(es))
print("zh worst",sorted(zs,key=lambda x:x[2])[:25])
print("en worst",sorted(es,key=lambda x:x[2])[:25])
