import os, re, json, collections, statistics
import yaml

base = r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
rows=[]
for root, dirs, files in os.walk(base):
    if "entry.yml" not in files: continue
    p=os.path.join(root,"entry.yml")
    with open(p, encoding="utf-8") as f: y=yaml.safe_load(f)
    zh=os.path.join(root,"zh.md"); en=os.path.join(root,"en.md")
    def text(path):
        if not os.path.exists(path): return ""
        s=open(path,encoding="utf-8").read()
        s=re.sub(r"^---[\s\S]*?\n---\s*","",s,count=1)
        s=re.sub(r"!\[[^\]]*\]\([^)]*\)","",s)
        s=re.sub(r"\*[^*]*\*","",s)
        return s
    zt=text(zh); et=text(en)
    zh_chars=len(re.findall(r"[\u4e00-\u9fff]",zt))
    en_words=len(re.findall(r"[A-Za-z][A-Za-z'’-]*",et))
    y["_dir"]=os.path.relpath(root,base).replace("\\","/")
    y["_zh_chars"]=zh_chars; y["_en_words"]=en_words
    y["_n_sources"]=len(y.get("sources") or [])
    rows.append(y)

print("TOTAL",len(rows))
print("CHANNEL",collections.Counter(r.get("channel") for r in rows))
print("TYPE",collections.Counter(r.get("type") for r in rows))
print("STATUS",collections.Counter(r.get("status") for r in rows))
print("CRED",collections.Counter(r.get("credibility") for r in rows))
print("LANG",collections.Counter(r.get("translation_status") for r in rows))
print("EDIT",collections.Counter(r.get("editorial_status") for r in rows))
print("ZH_LEN min/median/max",min(r["_zh_chars"] for r in rows),statistics.median(r["_zh_chars"] for r in rows),max(r["_zh_chars"] for r in rows))
print("EN_LEN min/median/max",min(r["_en_words"] for r in rows),statistics.median(r["_en_words"] for r in rows),max(r["_en_words"] for r in rows))
print("SOURCES min/median/max",min(r["_n_sources"] for r in rows),statistics.median(r["_n_sources"] for r in rows),max(r["_n_sources"] for r in rows))
print("\nREGIONS")
for k,v in collections.Counter((r.get("region") or "?").strip() for r in rows).most_common(): print(v,k)
print("\nCOLLECTIONS")
for k,v in collections.Counter(c for r in rows for c in (r.get("collections") or [])).most_common(): print(v,k)
print("\nTAGS top")
for k,v in collections.Counter(t for r in rows for t in (r.get("tags") or [])).most_common(60): print(v,k)
