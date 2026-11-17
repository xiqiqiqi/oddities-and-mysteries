import os, yaml, collections
from urllib.parse import urlparse
base=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
rows=[]
for root,dirs,files in os.walk(base):
    if "entry.yml" in files:
        rows.append(yaml.safe_load(open(os.path.join(root,"entry.yml"),encoding="utf-8")))

def ind(r):
    ds=[urlparse(s.get("url","")).netloc.lower().replace("www.","") for s in (r.get("sources") or [])]
    return [d for d in ds if d and "wikipedia.org" not in d and "xiqiqi.com" not in d and "commons.wikimedia.org" not in d]

print("entries with 0 independent",sum(1 for r in rows if not ind(r)))
print("entries with 1 independent",sum(1 for r in rows if len(ind(r))==1))
print("entries with >=2 independent",sum(1 for r in rows if len(ind(r))>=2))
print("deficit list")
for r in rows:
    if not ind(r):
        print(r["channel"],r["slug"],len(r.get("sources") or []))
