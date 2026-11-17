import os, yaml
base=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
rows=[]
for root,dirs,files in os.walk(base):
    if "entry.yml" in files:
        y=yaml.safe_load(open(os.path.join(root,"entry.yml"),encoding="utf-8"))
        y["_dir"]=os.path.relpath(root,base)
        rows.append(y)
for r in sorted(rows,key=lambda x:(x.get("channel"),x.get("slug"))):
    print(f"{r.get('channel'):9} {r.get('slug'):32} {r.get('title_zh','')[:28]:30} {str(r.get('era',''))[:26]:28} {str(r.get('region',''))[:36]:38} {r.get('credibility')}")
