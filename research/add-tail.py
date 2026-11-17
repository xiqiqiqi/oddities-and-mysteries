# -*- coding: utf-8 -*-
import os,re
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
DATA={
"creatures/black-shuck":("黑狗的材料散落在教区登记簿、地方报纸和后来的民俗专栏里；没有一处档案保存完整序列，同一个故事常在几个郡以不同名字出现。", "The Black Shuck material is scattered across parish registers, local newspapers, and later folklore columns; no single archive holds a complete run, and the same story often appears in several counties under different names."),
"creatures/bloody-mary":("血腥玛丽的材料主要是口述与商业产品：校园游戏、电影电视和万圣节商品。仪式本身没有原始档案，本文因此把不同版本当作“故事如何被讲述”的证据，而不是镜子里发生了什么的证据。", "The Bloody Mary material is mostly oral and commercial: school playgrounds, film and television, and Halloween products. There is no primary archive of the ritual itself, so the entry treats the versions as evidence of how the story is told, not of what happens in a mirror."),
"creatures/honey-island-swamp-monster":("蜂蜜岛沼泽怪物的档案由地方报纸特写、猎人访谈和后来的旅游文案组成；没有标本、足迹石膏或经独立复核的照片。", "The Honey Island material consists of local newspaper features, hunter interviews, and later tourism copy; no specimen, track cast, or photograph has been independently verified."),
"creatures/spring-heeled-jack":("跃脚杰克的档案还受另一层干扰：后来的回忆录反复复用同一批报纸条目，一句看起来像新目击的话，往往只是对旧报道的改写。", "The Spring-heeled Jack file is further complicated by the way later memoirs reuse the same handful of newspaper items; a sentence that looks like a new witness is often a paraphrase of an earlier report."),
"creatures/squonk":("“斯宽克”更像是伐木营地的文学发明，而不是野外记录；它的档案是出版过的荒诞故事、歌曲和后来的童书，不是捕获动物的记录。", "The Squonk is a literary and lumber-camp invention more than a field report; its archive is the published tall tale, the song, and the later children's book, not a record of a captured animal."),
"mystery/blue-jets":("蓝喷流的观测夹在航空报告、卫星仪器和大气物理之间；同一次事件可能同时是飞行员描述、相机帧和模型输出，三者各自都不完整。", "Blue-jet observations sit between aviation reports, satellite instruments, and atmospheric physics; the same event can appear as a pilot's description, a camera frame, and a model, and none of these is complete on its own."),
"mystery/bristol-hum":("布里斯托嗡鸣的档案主要是一条地方政府与公共卫生的纸面链：投诉、议会回应、声学测量，以及调查者始终无法达成一致的那个“没有声源”。", "The Bristol hum file is mostly a local-government and public-health paper trail: complaints, council responses, acoustic surveys, and the absence of a source that all investigators could agree on."),
"mystery/fairy-circles":("仙女环研究分散在长期样地、航拍照片和数学模型之间；档案对“图案”很强，对“制造图案的生物”却很弱。", "Fairy-circle research is split between long-term field plots, aerial photography, and mathematical models; the archive is strong on pattern and weak on the identity of the organism that makes it."),
"mystery/foo-fighters":("喷火战斗机的报告主要保存在战时部队史、飞行员访谈和战后航空医学研究里；档案很少带仪器数据，所以它始终是一个类别，而不是一个确定物体。", "Foo-fighter reports are preserved mainly in wartime unit histories, pilot interviews, and postwar aviation-medicine studies; the files rarely include instrument data, which is why the phenomenon remains a category rather than a single object."),
"mystery/phoenix-lights":("凤凰城光点的档案包括飞行员报告、警方日志、电视素材和后来的照明弹解释；最硬的部分是目击的时间与方向，而不是光点的形状。", "The Phoenix Lights file includes pilot reports, police logs, television footage, and later flare explanations; the strongest material is the timing and direction of the sightings, not the shape of the lights."),
"mystery/whistle":("口哨声的档案异常薄：几则报纸消息、一个家族故事和后来的汇编。没有早期录音或独立目击陈述留下来，本文因此把“声音”和“解释”分栏并列。", "The whistle archive is unusually thin: a few newspaper items, a family story, and later compilations. No early recording or independent witness statement survives, so the entry keeps the sound and the explanation in separate columns."),
"objects/bog-bodies":("沼泽尸体的研究建立在博物馆保护档案、法医报告和泥炭化学研究上；同一具尸体可以同时是考古发现、刑事案件和民俗故事，本文把这几套记录分开。", "Bog-body research is grounded in museum conservation files, forensic reports, and peat-chemistry studies; the same body can be an archaeological find, a legal case, and a folk story, and the entry keeps those registers apart."),
"objects/dead-sea-scrolls":("死海古卷的档案是一套保护与学术记录：洞穴发现、收购史、编辑重建和博物馆陈列。文本往往不完整，每一次翻译都是在解释字母之间的空白。", "The Scrolls archive is a conservation and scholarly record: cave finds, acquisition histories, editorial reconstructions, and museum display. The text is often incomplete, and every translation is an interpretation of gaps as well as letters."),
"places/great-zimbabwe":("大津巴布韦的档案一半是石头，一半是“谁有权解释石头”的纸面争论；本文先跟石头，再跟殖民时代的论辩。", "Great Zimbabwe's archive is split between the stone evidence and the paper trail of who was allowed to interpret it; the entry follows the stone first and the colonial argument second."),
"places/jiaohe":("交河的纸面档案穿过发掘报告、保护文件和丝绸之路申遗文本；遗址本身才是第一手文件，凡文字记录变薄的地方，本文回到废墟。", "Jiaohe's paper trail runs through excavation reports, conservation files, and the Silk Roads nomination; the site's own ruins are the primary document, and the entry returns to them whenever the written record thins."),
"places/lalibela":("拉利贝拉的档案由教会记录、保护报告和旅行记述组成；凿岩教堂是首要证据，而建城传说与每座建筑的年代仍有一部分开放。", "Lalibela's archive combines church records, conservation reports, and travel accounts; the rock-cut churches are the primary evidence, while the founding legend and the date of each building remain partly open."),
"places/mohenjo-daro":("摩亨佐-达罗的档案首先是发掘档案：平面图、照片和器物登记，都在保护与后来的城市压力改变遗址之前完成。", "Mohenjo-daro's archive is an excavation archive first: plans, photographs, and object registers made before conservation and later urban pressure changed the site."),
"places/troy":("特洛伊的档案是层层叠压的发掘档案，从施里曼的探沟到现代地层学；荷马故事与土丘是两种记录，本文不把它们熔在一起。", "Troy's archive is a layered excavation archive, from Schliemann's trenches to modern stratigraphic work; the Homeric story and the mound are two different records, and the entry does not fuse them."),
"places/winchester-mystery-house":("温彻斯特神秘屋的档案主要是房子本身、建筑许可和家族的宣传材料；“连续施工”是解释的一部分，不是独立记录。", "The Winchester Mystery House archive is mostly the house itself, building permits, and the family's own promotional material; the 'continuous construction' story is part of the interpretation, not an independent record."),
"tales/alien-autopsy":("“外星人尸检”的档案是电视档案：播出带、收视报道和后来对制作者的访谈。没有医疗记录，没有保管链，也没有原始胶片元素。", "The alien-autopsy file is a television archive: broadcast masters, ratings coverage, and later interviews with the producers. There is no medical record, no chain of custody, and no original film element."),
"tales/dancing-plague":("舞蹈瘟疫的档案是编年史档案：城镇记录、布道文和后来的医学评论。离 1518 年越远，记述往往越详细，这与法医记录的正常方向相反。", "The dancing-plague archive is a chronicle archive: town records, sermons, and later medical commentary. The further the account is from 1518, the more detail it tends to add, which is the opposite of what a forensic record usually does."),
}
def z(s): return len(re.findall(r"[\u4e00-\u9fa5]",s))
def e(s): return len(re.findall(r"[A-Za-z0-9']+",s))
for key,(zt,et) in DATA.items():
    ch,slug=key.split("/")
    pz=os.path.join(ROOT,ch,slug,"zh.md"); pe=os.path.join(ROOT,ch,slug,"en.md")
    zh=open(pz,encoding="utf-8").read(); en=open(pe,encoding="utf-8").read()
    if "## 档案位置" in zh:
        zh=zh.replace("## 档案空白", zt+"\n\n## 档案空白",1)
    else:
        zh=zh.replace("## 档案空白", "## 档案位置\n\n"+zt+"\n\n## 档案空白",1)
    if "## Archive location" in en:
        en=en.replace("## Limits of the record", et+"\n\n## Limits of the record",1)
    else:
        en=en.replace("## Limits of the record", "## Archive location\n\n"+et+"\n\n## Limits of the record",1)
    open(pz,"w",encoding="utf-8",newline="\n").write(zh); open(pe,"w",encoding="utf-8",newline="\n").write(en)
    print(key,z(zh),e(en))
print("updated",len(DATA))
