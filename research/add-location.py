# -*- coding: utf-8 -*-
import os,re
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
DATA={
"creatures/spring-heeled-jack":{
"zh_loc":"跃脚杰克的故事主要保存在 19 世纪英国报纸、地方传说集和后来的通俗读物里。1837 年秋天的伦敦恐慌常被当作起点，但报纸上的匿名来信、目击转述和剧场噱头混在一起，很难把一次“目击”还原成具体的时间、地点和人物。今天能查到的多是二次汇编；原始报刊页、教区记录和警方档案需要到地方档案馆逐条核对。本文因此把“报纸报道过”与“确有此人”分开。",
"en_loc":"The Spring-heeled Jack story survives mainly in nineteenth-century newspaper columns, local legend collections, and later popular retellings. The London panic of autumn 1837 is often treated as the starting point, but anonymous letters, second-hand witness reports, and theatre stunts are mixed together, making it difficult to reduce any single sighting to a precise time, place, and person. Most of what can be checked today is secondary compilation; original newspaper pages, parish records, and police files still require item-by-item work in local archives. This entry therefore separates 'the newspapers reported it' from 'a person did it'.",
"zh_note":"这篇条目把跃脚杰克先当作媒体事件，再当作怪物。核心问题不是“有没有一个装弹簧的人”，而是一组报纸说法如何变成耐久的都市传说。有明确日期的报道按日期写，记录含糊的地方保持含糊，不把“有目击者说”升级成“确实发生过”。后来的舞台剧、电影和网络版本同样按这个标准处理：它们是故事的后半生，不是原始事件的证据。",
"en_note":"This entry treats Spring-heeled Jack as a media event before it treats him as a creature. The core question is not whether a man with springs existed, but how a set of newspaper claims became a durable urban legend. Reports are dated where the source dates them, left undated where the record is vague, and never upgraded from 'a witness said' to 'it happened'. The same standard applies to the later stage, film, and internet versions: they are part of the story's afterlife, not evidence for the original events.",
},
"places/jiaohe":{
"zh_loc":"交河故城的记录分三层：联合国教科文组织与《丝绸之路》申遗文本给出遗址范围、年代与突出普遍价值；新疆文物考古机构和吐鲁番学界的调查提供城址分区、寺院、墓葬与出土文书；旅游说明和导览则简化了这些结论。遗址建在雅尔乃孜沟的台地上，城址本身约 37.6 公顷，沟北、沟西墓地另计。本文把申遗文本的框架与考古调查的细节分开，不把导览词当成发掘报告。",
"en_loc":"The record of Jiaohe falls into three layers: the UNESCO Silk Roads inscription and nomination texts set out the property's extent, dates, and outstanding universal value; surveys by Xinjiang cultural-relic and Turpan studies institutions describe the city's zones, temples, tombs, and excavated documents; tourist signs and guidebooks simplify those conclusions. The city sits on a plateau in the Yarnaz valley, with the walled site itself about 37.6 hectares and the cemeteries to the north and west counted separately. This entry keeps the nomination framework apart from the excavation detail and does not treat guidebook wording as an excavation report.",
},
"tales/dancing-plague":{
"zh_loc":"舞蹈瘟疫的原始记录主要来自 1518 年斯特拉斯堡的编年史、城市议会与教会档案，以及后来的医学史和民俗学讨论。编年史记下了日期、人数和持续天数，但对“为什么跳”给出的多是当时的神学或体液解释。后世研究提出过麦角中毒、集体癔症、应激传播等模型，每种模型能解释一部分，却不能解释全部。本文把“有记录”与“有解释”分开，不把某一种诊断当成定论。",
"en_loc":"The dancing plague is documented mainly through the 1518 Strasbourg chronicles, city-council and church records, and later medical-historical and folklore scholarship. The chronicles record dates, numbers, and duration, but their explanations of why people danced are mostly theological or humoral. Later studies have proposed ergot poisoning, mass hysteria, and stress contagion; each model accounts for part of the record, none for all of it. This entry separates 'it was recorded' from 'it has been diagnosed' and does not treat any one explanation as settled.",
},
"places/akrotiri":{
"zh_loc":"阿克罗蒂里的档案由三部分组成：希腊考古学会与雅典法国学院的发掘报告，提供建筑、壁画、陶器和层位；火山学与年代学研究，提供喷发时间与火山灰层的争论；遗址管理方的保护记录，说明哪些壁画和建筑被移入博物馆、哪些留在原地。三部分的时间尺度不同，不能互相替代。本文把“遗址被火山灰覆盖”这一事实，与“喷发年份”这一仍在争论的判断分开。",
"en_loc":"The Akrotiri record has three parts: excavation reports from the Greek Archaeological Society and the French School at Athens, which supply architecture, frescoes, pottery, and stratigraphy; volcanological and chronological studies, which debate the date of the eruption and the ash layers; and site-management conservation records, which show which frescoes and structures were moved to museums and which remain in place. These parts operate on different time scales and cannot substitute for one another. This entry separates the fact that the site was buried in ash from the still-debated question of the eruption year.",
},
"places/great-zimbabwe":{
"zh_loc":"大津巴布韦的记录跨越考古学、建筑史和殖民时期的政治争论。考古调查确认了石墙、山丘建筑群和外围定居点的年代与营造顺序；早期欧洲旅行者和殖民官员的叙述，则长期把“谁建造”当成文明归属的论据。今天的博物馆与大学研究把建筑技术、牧牛与黄金贸易放在南部非洲内部的发展脉络里。本文把考古层位与殖民时代的解释分开，不重复“外来文明”的旧说。",
"en_loc":"The Great Zimbabwe record spans archaeology, architectural history, and colonial-era political argument. Excavations have established the dates and building sequence of the stone walls, the Hill Complex, and the surrounding settlement; early European travellers and colonial officials, by contrast, long used the question of 'who built it' as an argument about civilizational ownership. Current museum and university research places the masonry, cattle keeping, and gold trade within the internal development of southern Africa. This entry separates stratigraphy from colonial-era interpretation and does not repeat the old 'foreign builder' claim.",
},
"places/mohenjo-daro":{
"zh_loc":"摩亨佐-达罗的公开记录主要来自 1920 年代以来的发掘报告、巴基斯坦考古部门的保护档案，以及早期城市规划与水利研究。遗址的街道网格、排水系统、大浴池和住宅区被反复描述，但文字尚未解读，族群与语言归属仍是开放问题。所谓“核爆痕迹”没有可靠发表，属于后来的传说层。本文把城市考古与伪科学说法分开，不把未解读的文字当成已知历史。",
"en_loc":"The public record of Mohenjo-daro comes mainly from excavation reports since the 1920s, conservation files of Pakistan's archaeology department, and studies of early urban planning and water management. The street grid, drains, Great Bath, and residential quarters are repeatedly described, but the script remains undeciphered and the ethnic and linguistic affiliations are still open. The so-called 'nuclear blast traces' have no reliable publication and belong to a later legendary layer. This entry separates urban archaeology from pseudo-scientific claims and does not treat an undeciphered script as known history.",
},
"tales/alien-autopsy":{
"zh_loc":"“外星人尸检”不是一份档案，而是一段电视产品史。1980 年代的付费电视节目、1990 年代的福克斯特别节目和后来的网络剪辑，共用一套画面语言：黑白胶片、手术灯、穿防护服的人、被遮挡的“尸体”。这些素材没有可核对的拍摄地点、日期、摄制人员和原始底片；所谓“胶片速度”“灯架反射”等鉴定，也多在节目内外互相引用。本文把它当作媒体骗局与电视史来写，不把它当作罗斯威尔事件的证据。",
"en_loc":"The 'alien autopsy' is not an archive but a history of television production. The pay-TV programme of the 1990s, the Fox special, and later internet cuts share a visual grammar: black-and-white film, surgical lamps, figures in protective suits, and a body kept partly out of frame. The material has no checkable shooting location, date, crew, or original negative; the 'film-speed' and 'lamp-reflection' analyses tend to cite one another inside and outside the programme. This entry treats it as media hoax and television history, not as evidence for Roswell.",
},
"places/carnac-stones":{
"zh_loc":"卡纳克石阵的记录从 19 世纪的古物学研究开始，经过法国国家古迹署的列级档案、20 世纪的发掘与修复，以及近年的申遗文本。石列、支石墓、土丘和围垣被放在新石器时代布列塔尼的仪式景观里；圣科内利传说则提供了另一种解释。本文把“石阵被建造”这一考古事实，与“石阵为何被建造”这一仍在讨论的问题分开。",
"en_loc":"The Carnac record begins with nineteenth-century antiquarianism, passes through the French national monuments listing, twentieth-century excavation and restoration, and the recent World Heritage nomination. The rows, dolmens, tumuli, and enclosures are placed within the ritual landscape of Neolithic Brittany; the legend of Saint Cornely offers another explanation. This entry separates the archaeological fact that the stones were built from the still-discussed question of why they were built.",
},
"creatures/almas":{
"zh_loc":"阿尔玛斯的材料主要是 19 世纪至 20 世纪的中亚旅行记、地方民族志和苏联时期的考察报告。目击者多为牧民和猎人，描述集中在身高、毛发、脚形和回避人的行为；没有清晰照片、骨骼或可复核的实物。苏联学者曾把阿尔玛斯与尼安德特人残余联系起来，但这一假说缺少遗传学证据。本文把“口述传统中的野人”与“一个未被确认的物种”分开。",
"en_loc":"The Almas material consists mainly of nineteenth- and twentieth-century Central Asian travel accounts, local ethnography, and Soviet-era survey reports. Witnesses were mostly herders and hunters; their descriptions focus on height, hair, foot shape, and avoidance of people. There are no clear photographs, bones, or independently examinable physical remains. Soviet scholars once linked the Almas to a surviving Neanderthal population, but the hypothesis lacks genetic evidence. This entry separates 'a wild man in oral tradition' from 'an unidentified species'.",
},
"creatures/snallygaster":{
"zh_loc":"斯纳利加斯特的档案是报纸档案的典型样本。19 世纪至 20 世纪初的宾夕法尼亚、马里兰地方报纸，把目击、酒馆故事和政治漫画混在一起；后来地方史写作又把这些版面当成“传统”。没有照片、标本或连贯的目击链，只有不断复制的版画和描述。本文把报纸上的形象史与动物学问题分开，不把插图当成目击证据。",
"en_loc":"The Snallygaster file is a sample of newspaper archive work. Nineteenth- and early twentieth-century local papers in Pennsylvania and Maryland mixed sightings, tavern stories, and political cartoons; later local-history writing then treated those pages as 'tradition'. There are no photographs, specimens, or a coherent chain of sightings, only repeatedly copied woodcuts and descriptions. This entry separates the history of a newspaper image from a zoological question and does not treat an illustration as witness evidence.",
},
"mystery/bloop":{
"zh_loc":"Bloop 的记录来自 1997 年太平洋水听器阵列的原始录音、NOAA 的公开说明和后来的频谱分析。信号很短，低频，能被多个阵列听到；研究者后来把它与冰山崩解、冰震类比。但原始波形、阵列坐标和处理参数没有全部公开，独立复算受限。本文把“录到了一个声音”与“知道它是什么”分开。",
"en_loc":"The Bloop record comes from the 1997 Pacific hydrophone array, NOAA's public statements, and later spectral analyses. The signal was short, low-frequency, and heard on more than one array; researchers later compared it to iceberg calving and ice seismicity. The original waveform, array coordinates, and processing parameters were not all released, limiting independent recomputation. This entry separates 'a sound was recorded' from 'we know what made it'.",
},
"mystery/ball-lightning":{
"zh_loc":"球状闪电的记录跨越气象学、等离子体物理和目击者传统。实验室有短寿命的等离子体球实验，田野有大量近距目击，但两者之间没有一条完整的证据链：没有一段被仪器同步记录的野外球状闪电，也没有一种模型能重复所有报告特征。本文把“实验室里能造出类似现象”与“天空中的那个球就是它”分开。",
"en_loc":"The ball-lightning record spans meteorology, plasma physics, and witness tradition. Laboratory experiments have produced short-lived plasma balls, and field reports contain many close sightings, but no complete chain links the two: there is no field ball lightning recorded simultaneously by instruments, and no model reproduces every reported feature. This entry separates 'a similar phenomenon can be made in the lab' from 'that ball in the sky was it'.",
},
"places/herculaneum":{
"zh_loc":"赫库兰尼姆的档案由三套材料构成：18 世纪以来的发掘记录、意大利文化遗产部门的保护与开放档案，以及纸草学与火山学研究。遗址被火山碎屑覆盖，有机材料保存得比庞贝更好；Villa of the Papyri 的纸草卷仍在解读。游客看到的街道和房屋，是发掘、修复与展示共同形成的版本。本文把考古层位、修复干预和旅游呈现分开。",
"en_loc":"The Herculaneum record has three sets of material: excavation records since the eighteenth century, conservation and site-management files of the Italian cultural heritage service, and papyrological and volcanological research. The site was buried under volcanic debris, preserving organic material better than Pompeii; the papyrus scrolls from the Villa of the Papyri are still being read. The streets and houses visitors see are a version shaped by excavation, restoration, and display. This entry separates stratigraphy, restoration intervention, and tourist presentation.",
},
"tales/martian-canals":{
"zh_loc":"火星运河的记录是观测史与印刷文化的历史。19 世纪末的天文观测、洛厄尔的台站笔记和通俗天文学书籍，把低分辨率望远镜下的暗线画成“运河”；后来的探测器影像证明那些线条多是观测伪影与地图绘制的产物。本文把“当时的天文学家看见了什么”与“火星上有什么”分开，不把旧地图当成地貌证据。",
"en_loc":"The Martian canals are a history of observation and print culture. Late nineteenth-century astronomy, Lowell's observatory notes, and popular astronomy books turned faint lines seen through low-resolution telescopes into 'canals'; later spacecraft imaging showed that the lines were largely observational artifacts and cartographic products. This entry separates 'what astronomers thought they saw' from 'what is on Mars' and does not treat old maps as geomorphological evidence.",
},
"places/enfield-poltergeist":{
"zh_loc":"恩菲尔德骚动的记录主要是 1977 年当地报纸、警方回访、儿童保护机构的个案材料，以及后来社会学者对“家庭压力—儿童表演”的访谈。录音和物品移动有目击者，但没有实验室条件下的独立记录；女孩的叙述在不同访谈中有变化。本文把“家里发生过无法解释的事”与“有鬼”分开，也不把当事人的撤回或改口当成全部虚构。",
"en_loc":"The Enfield case is documented mainly through the 1977 local press, police call-outs, child-protection case material, and later sociological interviews on family stress and child performance. There are witnesses to sounds and moving objects, but no independently recorded laboratory conditions; the girls' accounts changed across interviews. This entry separates 'something unexplained happened in the house' from 'a ghost did it', and does not treat a later retraction or change of story as proof of wholesale invention.",
},
"mystery/wanggongchang-1626":{
"zh_loc":"王恭厂灾变的材料主要是明代官方奏报、地方志、私家笔记和后来的地震、火药研究。1626 年 5 月 30 日的爆炸造成大范围破坏，但“核爆”“陨石”等说法多为 20 世纪后的附会。原始记录对声响、火光、房屋倒塌方向和伤亡有不同版本；官方奏报也有赈灾与追责的语境。本文把“灾变发生过”与“原因是火药、地震还是其他”分开。",
"en_loc":"The Wanggongchang disaster is documented mainly through Ming official memorials, local gazetteers, private notes, and later studies of seismology and gunpowder. The explosion of 30 May 1626 caused wide destruction, but 'nuclear blast' and 'meteor' claims are mostly twentieth-century additions. The original records differ on sound, fire, collapse direction, and casualties; official memorials also had relief and accountability contexts. This entry separates 'a disaster happened' from 'whether gunpowder, an earthquake, or something else caused it'.",
},
}
def z(s): return len(re.findall(r"[\u4e00-\u9fa5]",s))
def e(s): return len(re.findall(r"[A-Za-z0-9']+",s))
count=0
for key,d in DATA.items():
    ch,slug=key.split("/")
    pz=os.path.join(ROOT,ch,slug,"zh.md"); pe=os.path.join(ROOT,ch,slug,"en.md")
    zh=open(pz,encoding="utf-8").read(); en=open(pe,encoding="utf-8").read()
    if "zh_note" in d:
        zh=zh.replace("## 档案空白","## 编者说明\n\n"+d["zh_note"]+"\n\n## 档案空白",1)
        en=en.replace("## Limits of the record","## Editorial note\n\n"+d["en_note"]+"\n\n## Limits of the record",1)
    zh=zh.replace("## 档案空白","## 档案位置\n\n"+d["zh_loc"]+"\n\n## 档案空白",1)
    en=en.replace("## Limits of the record","## Archive location\n\n"+d["en_loc"]+"\n\n## Limits of the record",1)
    print(key,"zh",z(zh),"en",e(en))
    open(pz,"w",encoding="utf-8",newline="\n").write(zh)
    open(pe,"w",encoding="utf-8",newline="\n").write(en)
    count+=1
print("updated",count)
