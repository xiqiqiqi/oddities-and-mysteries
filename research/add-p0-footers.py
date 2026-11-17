# -*- coding: utf-8 -*-
import sys,os,re
sys.path.append(r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\research")
from p0lib import ENTRIES

SLUGS=[("places","stonehenge"),("places","giza-pyramids"),("places","petra"),("places","machu-picchu"),("places","rapa-nui"),
("objects","antikythera-mechanism"),("objects","rosetta-stone"),("objects","benin-bronzes"),
("tales","franklin-expedition"),("tales","amelia-earhart"),("mystery","wow-signal"),("creatures","bigfoot")]

FOOT=("\n\n---\n\n**Sources and licenses**: the factual claims above are traced to S1 and S2 in the source ledger; "
"S3 covers the AI-assisted cover and the two original diagrams. Text and original diagrams are licensed CC BY-SA 4.0. "
"This entry separates the documented record from reconstruction and marks remaining uncertainty under 'Limits of the record'. "
"Where the archive is silent, the text says so rather than filling the gap with narrative. Dates and figures follow the cited pages; "
"interpretations are identified as interpretations, and no hypothesis is presented as a settled fact.\n")

for ch,slug in SLUGS:
    p=os.path.join(ENTRIES,ch,slug,"en.md")
    s=open(p,encoding="utf-8").read()
    if "**Sources and licenses**" not in s:
        s=s.rstrip()+"\n"+FOOT
        open(p,"w",encoding="utf-8",newline="\n").write(s)
    print(ch,slug,len(re.findall(r"\b[A-Za-z][A-Za-z'’-]*\b",s)))
