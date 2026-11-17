import os,re,collections,yaml
base=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
rows=[]
for root,dirs,files in os.walk(base):
    if "entry.yml" in files: rows.append(yaml.safe_load(open(os.path.join(root,"entry.yml"),encoding="utf-8")))

def bucket(s):
    s=str(s or "")
    if "公元前" in s:
        m=re.search(r"公元前\s*(\d+)",s)
        y=int(m.group(1)) if m else 9999
        return "史前/公元前1500前" if y>=1500 else "公元前1500–前500" if y>=500 else "公元前500–公元1"
    m=re.search(r"(?<!\d)(1\d{3}|20\d{2}|2\d{3})(?!\d)",s)
    if m:
        y=int(m.group(1))
        if y<1500: return "500–1500"
        if y<1800: return "1500–1800"
        if y<1946: return "1800–1945"
        if y<2000: return "1945–2000"
        return "2000 以后"
    if "古代" in s or "传说" in s or "民间" in s or "中世纪" in s or "世纪" in s:
        return "古代/传说（未定年）"
    return "其他/未定年"
c=collections.Counter(bucket(r.get("era")) for r in rows)
for k,v in c.most_common(): print(f"{v:3} {v/len(rows)*100:5.1f}% {k}")
print()
for ch in ["mystery","tales","objects","places","creatures"]:
    print(ch,dict(collections.Counter(bucket(r.get("era")) for r in rows if r.get("channel")==ch)))
