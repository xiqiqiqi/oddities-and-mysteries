# -*- coding: utf-8 -*-
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from p0lib import append_location
DATA={
("tales","franklin-expedition"):(
"富兰克林的档案分布在加拿大、英国和因纽特社区：加拿大公园管理局保存沉船调查、水下考古和遗址管理记录；加拿大国家图书档案馆保存搜索队日志、地图与政府通信；皇家博物馆格林尼治保存 19 世纪搜索队的器物与航海档案；因纽特遗产信托与当地社区保存口述史、地名和目击记录。早期搜索者常把因纽特证词写成“传闻”，现代考古则把它当作可核对的地理信息。本文把沉船位置、日期与已发表的骨骼分析作为可核对事实；死因比例、幸存者人数和同类相食的范围，仍依赖各档案的交叉解释。",
"The Franklin archive is distributed across Canada, Britain, and Inuit communities: Parks Canada holds wreck surveys, underwater archaeology, and site-management records; Library and Archives Canada holds search-party logs, maps, and government correspondence; Royal Museums Greenwich holds objects and naval records from the nineteenth-century searches; Inuit Heritage Trust and local communities hold oral histories, place names, and sightings. Early searchers often recorded Inuit testimony as 'rumour', while modern archaeology treats it as checkable geographical information. This entry treats wreck positions, dates, and published bone analyses as verifiable fact; the share of each cause of death, the number of survivors, and the extent of cannibalism still depend on cross-reading those archives."),
("tales","amelia-earhart"):(
"埃尔哈特的档案有三条主线：普渡大学保存飞行计划、通信、照片与剪报；美国国家档案馆、海军与海岸警卫队保存搜索航迹、无线电日志和官方报告；史密森尼国家航空航天博物馆保存 Electra 相关资料与航空史收藏。民间调查组织（如 TIGHAR）另有一套照片、声呐与实地记录，但其方法、样本和结论需要独立评估。三条主线的共同缺口是：没有飞机残骸、没有可确认的最终位置、没有完整的最后无线电原始记录。本文因此只写已确认的航线和搜索范围，不把任何单一假说写成结论。",
"Earhart's archive has three main lines: Purdue University holds flight plans, correspondence, photographs, and clippings; the US National Archives, Navy, and Coast Guard hold search tracks, radio logs, and official reports; the Smithsonian National Air and Space Museum holds Electra-related material and aviation-history collections. Private investigation groups such as TIGHAR keep separate photographic, sonar, and field records, but their methods, samples, and conclusions need independent assessment. The common gap across all three lines is the absence of wreckage, a confirmed final position, and a complete original record of the last radio messages. This entry therefore states only the confirmed route and search area, and treats no single hypothesis as a conclusion."),
("mystery","wow-signal"):(
"Wow 信号的档案主要在俄亥俄州：俄亥俄州立大学图书馆保存“大耳朵”巡天打印记录、观测日志与部分设备文件；NAAPO 保存望远镜历史、成员口述和后续搜索资料。原始打印纸是核心物证，但它只记录强度代码、时间与波束位置，不含完整的校准和干扰信息。SETI 机构与后续观测团队保存自己的搜索日志，但没有一份能与 1977 年的记录形成闭环。本文把频率、持续时间、强度代码和“未重复”写成记录事实；来源解释、彗星假说与设备状态，则标明为待验证或仍有争议的部分。",
"The Wow signal's archive is mainly in Ohio: Ohio State University Libraries hold the Big Ear survey printouts, observing logs, and some instrument files; NAAPO holds telescope history, members' recollections, and follow-up search material. The original printout is the core physical record, but it gives only intensity codes, time, and beam position, not complete calibration or interference data. SETI institutions and later observing teams keep their own search logs, but none closes the loop with the 1977 record. This entry states frequency, duration, intensity code, and non-repetition as recorded facts; source explanations, the comet hypothesis, and instrument state are marked as unverified or disputed."),
("creatures","bigfoot"):(
"大脚怪没有“模式标本”，因此没有博物馆级的生物档案；现有材料分散在私人收藏、地方历史学会、大学民俗档案和媒体机构。史密森尼与多家动物学机构保存的是熊、鹿、狼等常见动物的标本与 DNA 参考数据，用来比对所谓大脚怪样本；美国民俗学会及大学民俗项目保存目击叙述、剪报和民间叙事研究。商业组织（如 BFRO）另建目击数据库，但采集标准、核实流程和访问权限不透明。本文使用的 DNA 结论来自已发表的同行评议研究；目击叙述只作为文化材料，不作为生物存在证据。",
"Bigfoot has no type specimen and therefore no museum-grade biological archive; existing material is scattered across private collections, local historical societies, university folklore archives, and media organisations. The Smithsonian and other zoological institutions hold specimens and DNA reference data for bears, deer, wolves, and other common animals, used to compare alleged Bigfoot samples; the American Folklore Society and university folklore programmes hold sightings, clippings, and narrative research. Commercial organisations such as the BFRO maintain separate sighting databases, but collection standards, verification, and access are not transparent. The DNA conclusions used here come from published peer-reviewed research; sightings are treated as cultural material, not as evidence of a living creature."),
}
for k,v in DATA.items(): append_location(k[0],k[1],v[0],v[1])

# Benin English needs a little more
import re
from p0lib import ENTRIES
p=os.path.join(ENTRIES,"objects","benin-bronzes","en.md")
s=open(p,encoding="utf-8").read()
s=s.replace("and that is the hardest part of the return negotiations.","and that is the hardest part of the return negotiations. The archive is not a neutral inventory: it was built by the same institutions that acquired the objects, and its categories still shape how the return is argued.")
open(p,"w",encoding="utf-8",newline="\n").write(s)
print("benin en",len(re.findall(r"[A-Za-z0-9']+",s)))
