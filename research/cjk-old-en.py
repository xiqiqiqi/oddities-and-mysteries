import re,subprocess,os
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries"; GIT=r"C:\Program Files\Git\cmd\git.exe"
for ch,slug in [("objects","sword-of-goujian")]:
    en=subprocess.run([GIT,"-C",ROOT,"show",f"8573e20:entries/{ch}/{slug}/en.md"],capture_output=True,text=True,encoding="utf-8").stdout
    for p in re.split(r"^## ",en,flags=re.M)[1:]:
        h=p.split("\n")[0]
        c=re.findall(r"[\u4e00-\u9fa5]",p)
        if c: print(h,len(c),''.join(c)[:40])
