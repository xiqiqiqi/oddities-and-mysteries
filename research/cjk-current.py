import re,os
for ch,slug in [("objects","sword-of-goujian")]:
    p=os.path.join(r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries",ch,slug,"en.md")
    t=open(p,encoding="utf-8").read()
    for i,line in enumerate(t.split("\n"),1):
        c=re.findall(r"[\u4e00-\u9fa5]",line)
        if c: print(i,len(c),line[:160])
