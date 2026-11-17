import re
p=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries\mystery\blood-falls\entry.yml"
s=open(p,encoding="utf-8").read()
print(re.sub(r"https?://[^\s\"]+","[URL]",s)[:4000])
print("---LEDGER---")
p=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\research\fact-ledgers\mystery\blood-falls.md"
s=open(p,encoding="utf-8").read()
print(re.sub(r"https?://[^\s\"]+","[URL]",s)[:4000])
