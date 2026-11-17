# -*- coding: utf-8 -*-
import sys,os,re
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from p0lib import ENTRIES

def edit(ch,slug,zh_old,zh_new,en_old,en_new):
    pz=os.path.join(ENTRIES,ch,slug,"zh.md"); pe=os.path.join(ENTRIES,ch,slug,"en.md")
    zh=open(pz,encoding="utf-8").read(); en=open(pe,encoding="utf-8").read()
    if zh_old:
        if zh_old not in zh: print("MISS zh",slug,zh_old[:20])
        zh=zh.replace(zh_old,zh_new,1)
    if en_old:
        if en_old not in en: print("MISS en",slug,en_old[:20])
        en=en.replace(en_old,en_new,1)
    open(pz,"w",encoding="utf-8",newline="\n").write(zh); open(pe,"w",encoding="utf-8",newline="\n").write(en)
    print(slug,len(re.findall(r"[\u4e00-\u9fa5]",zh)),len(re.findall(r"[A-Za-z0-9']+",en)))

edit("objects","benin-bronzes",
"这正是归还谈判中最难的部分。",
"这正是归还谈判中最难的部分。档案的空白本身也是争议的一部分：谁掌握记录，谁就有权叙述器物的来路。",
"and that is the hardest part of the return negotiations.",
"and that is the hardest part of the return negotiations. That asymmetry is part of the object's history, not a technical footnote; it shapes claims of ownership as much as the objects themselves do.")

edit("tales","amelia-earhart",None,None,
"and treats no single hypothesis as a conclusion.",
"and treats no single hypothesis as a conclusion. No single archive can settle the case, and no single theory should be presented as if it had. The absence of a final position is itself the most important archival fact.")

edit("mystery","wow-signal",
"则标明为待验证或仍有争议的部分。",
"则标明为待验证或仍有争议的部分。档案的不完整也解释了为什么这项记录至今无法被重复：缺少校准、干扰与设备状态的原始数据，后续搜索只能缩小范围，不能重建当时的观测条件。因此，“Wow”既是一个真实的记录，也是一个开放的问题；两者并不矛盾。",
"are marked as unverified or disputed.",
"are marked as unverified or disputed. The incompleteness also explains why the record has never been reproduced: without original calibration, interference, and instrument-state data, later searches can narrow the field but cannot rebuild the observing conditions. 'Wow' is therefore both a real record and an open question, and those two things are not in conflict.")

edit("creatures","bigfoot",None,None,
"sightings are treated as cultural material, not as evidence of a living creature.",
"sightings are treated as cultural material, not as evidence of a living creature. The absence of a type specimen is not a small technicality: it is the central reason the question remains open, and it places the burden of proof on those who claim the creature exists. Museum collections can test samples, but they cannot manufacture a body that has never been found. That is why the strongest scientific statement is negative: no confirmed specimen, no confirmed species.")
