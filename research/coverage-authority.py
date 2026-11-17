import os,yaml,collections
from urllib.parse import urlparse
base=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
rows=[]
for root,dirs,files in os.walk(base):
    if "entry.yml" in files:
        rows.append(yaml.safe_load(open(os.path.join(root,"entry.yml"),encoding="utf-8")))
auth=("britannica.com","metmuseum.org","unesco.org","si.edu","smithsonianmag.com","nasa.gov","noaa.gov","bbc.co.uk","nationalgeographic.com",".gov",".edu","loc.gov","archives.gov","royalcollection.org.uk","britishmuseum.org","whc.unesco.org","history.com","scientificamerican.com","nature.com","science.org")
def has_auth(r):
    ds=[urlparse(s.get("url","")).netloc.lower().replace("www.","") for s in (r.get("sources") or [])]
    return any(any(a in d for a in auth) for d in ds)
print("entries with authority source",sum(1 for r in rows if has_auth(r)))
print("by channel",dict(collections.Counter(r["channel"] for r in rows if has_auth(r))))
print("examples without")
for r in rows:
    if not has_auth(r): print(r["channel"],r["slug"])
