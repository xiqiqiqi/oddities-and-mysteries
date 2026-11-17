import os,yaml,collections
from urllib.parse import urlparse
base=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
rows=[]
for root,dirs,files in os.walk(base):
    if "entry.yml" in files: rows.append(yaml.safe_load(open(os.path.join(root,"entry.yml"),encoding="utf-8")))

def ind(r):
    ds=[urlparse(s.get("url","")).netloc.lower().replace("www.","") for s in (r.get("sources") or [])]
    return [d for d in ds if d and "wikipedia.org" not in d and "xiqiqi.com" not in d and "commons.wikimedia.org" not in d]

for cred in ["verified","disputed","folklore","hoax"]:
    subset=[r for r in rows if r.get("credibility")==cred]
    zero=[r for r in subset if not ind(r)]
    one=[r for r in subset if len(ind(r))==1]
    print(cred,len(subset),"zero_ind",len(zero),"one_ind",len(one))
print("verified zero list")
for r in rows:
    if r.get("credibility")=="verified" and not ind(r):
        print(r["channel"],r["slug"])
