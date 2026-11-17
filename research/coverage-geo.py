import os,re,collections,yaml
base=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
rows=[]
for root,dirs,files in os.walk(base):
    if "entry.yml" in files:
        rows.append(yaml.safe_load(open(os.path.join(root,"entry.yml"),encoding="utf-8")))

def macro(s):
    s=s or ""
    # order matters
    if any(k in s for k in ["全球","火星","太空","天鹅座","印度洋","南太平洋","大西洋","马六甲","红海","欧洲上空"]): return "全球/海洋/太空"
    if any(k in s for k in ["美国","加拿大","墨西哥"]): return "北美"
    if any(k in s for k in ["巴西","秘鲁","智利","阿根廷","哥伦比亚"]): return "拉丁美洲"
    if "澳大利亚" in s or "新西兰" in s: return "大洋洲"
    if any(k in s for k in ["埃及","埃塞俄比亚","纳米比亚","津巴布韦","南非","肯尼亚","摩洛哥"]): return "非洲"
    if any(k in s for k in ["中国","日本","印度","巴基斯坦","蒙古","中亚","土耳其","以色列","黎巴嫩","柬埔寨","印度尼西亚","尼泊尔","喜马拉雅","奥斯曼","哈萨克斯坦","北京","黎凡特"]): return "亚洲"
    if "南极" in s: return "南极"
    if any(k in s for k in ["英国","苏格兰","爱尔兰","法国","德国","意大利","挪威","荷兰","奥地利","捷克","罗马尼亚","马耳他","希腊","俄罗斯","苏联","欧洲","丹麦","波兰","西班牙","葡萄牙"]): return "欧洲"
    return "其他:"+s

c=collections.Counter(macro(r.get("region")) for r in rows)
print("MACRO")
for k,v in c.most_common(): print(f"{v:3} {v/len(rows)*100:5.1f}% {k}")

def country(s):
    s=s or ""
    for k in ["美国","加拿大","墨西哥","巴西","秘鲁","澳大利亚","埃及","埃塞俄比亚","纳米比亚","津巴布韦","南非","中国","日本","印度","巴基斯坦","蒙古","土耳其","以色列","黎巴嫩","柬埔寨","印度尼西亚","尼泊尔","英国","苏格兰","爱尔兰","法国","德国","意大利","挪威","荷兰","奥地利","捷克","罗马尼亚","马耳他","希腊","俄罗斯","哈萨克斯坦","波兰","西班牙","葡萄牙"]:
        if k in s: return k
    return "跨国/全球/其他"
cc=collections.Counter(country(r.get("region")) for r in rows)
print("\nCOUNTRY")
for k,v in cc.most_common(): print(f"{v:3} {k}")
print("distinct",len([k for k in cc if k not in ('跨国/全球/其他',)]))

print("\nCHANNEL x MACRO")
for ch in ["mystery","tales","objects","places","creatures"]:
    cc2=collections.Counter(macro(r.get("region")) for r in rows if r.get("channel")==ch)
    print(ch, dict(cc2))
