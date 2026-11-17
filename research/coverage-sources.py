import os, re, collections, statistics, yaml
from urllib.parse import urlparse
base=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
rows=[]
for root,dirs,files in os.walk(base):
    if "entry.yml" not in files: continue
    y=yaml.safe_load(open(os.path.join(root,"entry.yml"),encoding="utf-8"))
    rows.append(y)
dom=collections.Counter(); pub=collections.Counter(); kinds=collections.Counter()
onlywp=0; wp_plus_art=0; primaryish=0
for r in rows:
    src=r.get("sources") or []
    ds=[]; ps=[]
    for s in src:
        u=(s.get("url") or "")
        d=urlparse(u).netloc.lower().replace("www.","") if u.startswith("http") else "(no-url)"
        ds.append(d); dom[d]+=1
        ps.append((s.get("publisher") or "").strip()); pub[ps[-1]]+=1
    n=len(src)
    has_wp=any("wikipedia.org" in d for d in ds)
    own=any(("xiqiqi.com" in d) or ("稀奇奇" in p) for d,p in zip(ds,ps))
    if has_wp and n<=3 and own: wp_plus_art+=1
    if has_wp and not own: onlywp+=1
    if any(k in d for d in ds if False): pass
print("entries",len(rows),"total sources",sum(len(r.get('sources') or []) for r in rows))
print("median sources",statistics.median(len(r.get('sources') or []) for r in rows))
print("distribution",collections.Counter(len(r.get('sources') or []) for r in rows).most_common())
print("TOP DOMAINS")
for k,v in dom.most_common(25): print(v,k)
print("TOP PUBLISHERS")
for k,v in pub.most_common(20): print(v,k)
print("entries with wikipedia+own and <=3 sources",wp_plus_art,"of",len(rows))
