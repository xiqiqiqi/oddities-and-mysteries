# -*- coding: utf-8 -*-
import os,re,json
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries"
DATA={
"mystery/blood-falls":dict(title="MIDGE: Blood Falls, McMurdo Dry Valleys",publisher="United States Antarctic Program Data Center (NSF)",url="https://www.usap-dc.org/view/project/p0000002",year="2012",license="公开科研项目页面；引用与事实核对",usage="血瀑布的卤水、微生物与实地研究项目记录"),
"mystery/blue-jets":dict(title="The Role of the Space Shuttle Videotapes in the Discovery of Sprites, Jets, and ELVES",publisher="NASA Earthdata",url="https://www.earthdata.nasa.gov/learn/data-in-action/role-space-shuttle-videotapes-discovery-sprites-jets-elves",year="2025",license="NASA 公开资料；引用与事实核对",usage="蓝色喷流的命名、观测与发现史"),
"mystery/brine-pools":dict(title="Investigations of Chemosynthetic Communities on the Lower Continental Slope of the Gulf of Mexico (2006)",publisher="NOAA National Centers for Environmental Information",url="https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncei:DeepSlope2006;view=iso",year="2006",license="美国政府公开资料；引用与事实核对",usage="墨西哥湾深海卤水池的实地观测与生态记录"),
"mystery/litvinenko":dict(title="Litvinenko Inquiry: Statement to the House of Commons",publisher="UK Parliament (Hansard)",url="https://hansard.parliament.uk/Commons/2016-01-21/debates/16012124000003/LitvinenkoInquiry",year="2016",license="Open Parliament Licence",usage="英国议会关于利特维年科调查结论的官方记录"),
"mystery/magnetic-hill":dict(title="Magnetic Hill Illusion",publisher="City of Moncton",url="https://www.moncton.ca/en/magnetic-hill-illusion",year="2026",license="政府网站内容；引用与事实核对",usage="磁山的官方说明与重力丘错觉"),
"objects/bog-bodies":dict(title="Bog Bodies – National Museum of Ireland Collections Online",publisher="National Museum of Ireland",url="https://www.museum.ie/collections/nmi_story/kingship-and-sacrifice/bog-bodies/",year="2026",license="博物馆藏品页；引用与事实核对",usage="爱尔兰沼泽尸体的年代、死因与藏品记录"),
"objects/iron-pillar-delhi":dict(title="On the Corrosion Resistance of the Delhi Iron Pillar",publisher="Corrosion Science (Elsevier)",url="https://doi.org/10.1016/S0010-938X(00)00046-9",year="2000",license="学术论文；引用与事实核对",usage="德里铁柱的耐腐蚀机制与冶金分析"),
"objects/jade-burial-suit":dict(title="汉世雄风——纪念满城汉墓考古发掘50周年特展：金缕玉衣",publisher="中国国家博物馆",url="https://www.chnmuseum.cn/Portals/0/web/exhibition/exhibitions/201812han/43.html",year="2018",license="博物馆展览页；引用与事实核对",usage="满城汉墓金缕玉衣的形制、玉片与金丝数据"),
"objects/star-of-africa":dict(title="The Cullinan Diamond",publisher="Royal Collection Trust",url="https://www.rct.uk/collection/stories/the-crown-jewels/the-cullinan-diamond",year="2026",license="皇家收藏基金会页面；引用与事实核对",usage="库里南钻石的发现、切磨与库里南一号"),
"objects/sword-of-goujian":dict(title="越王勾践剑",publisher="湖北省博物馆",url="https://www.hbww.org.cn/zgzb/p/4694.html",year="2026",license="博物馆藏品页；引用与事实核对",usage="越王勾践剑的出土、尺寸、铭文与保存状况"),
"places/carnac-stones":dict(title="The Carnac alignments: a spectacular landscape",publisher="Alignements de Carnac / Centre des monuments nationaux",url="https://www.menhirs-carnac.fr/en/content/download/9853053/file/ALIGNEMENTS%20CARNAC_EN_web.pdf?version=14&inLanguage=eng-GB",year="2026",license="法国官方遗址资料；引用与事实核对",usage="卡纳克石阵的新石器时代背景、保护史与传说"),
"places/herculaneum":dict(title="Archaeological Areas of Pompeii, Herculaneum and Torre Annunziata",publisher="Patrimonio UNESCO (Italian Ministry of Culture)",url="https://www.patrimoniounesco.it/directory-tangibili/listing/aree-archeologiche-di-pompei-ercolano-e-torre-annunziata-teatro-di-ercolano/",year="2026",license="官方世界遗产名录；引用与事实核对",usage="赫库兰尼姆作为世界遗产的范围与编号"),
"places/hypogeum":dict(title="State of the Heritage Report 2005: The Hal-Saflieni Hypogeum",publisher="Superintendence of Cultural Heritage, Malta",url="https://schmalta.mt/wp-content/uploads/2022/09/SoH-2005.pdf",year="2005",license="政府文化遗产报告；引用与事实核对",usage="哈尔萨夫利尼地下墓室的世遗列入与保护状况"),
"places/jiaohe":dict(title="丝绸之路：长安—天山廊道的路网",publisher="国家文物局",url="http://www.ncha.gov.cn/art/2024/8/8/art_2791_190636.html",year="2024",license="政府文物局页面；引用与事实核对",usage="交河故城作为丝绸之路世界遗产的构成与价值"),
"places/lalibela":dict(title="Rock-Hewn Churches, Lalibela",publisher="UNESCO World Heritage Centre",url="https://whc.unesco.org/en/list/18/",year="1978",license="UNESCO 世界遗产页面；引用与事实核对",usage="拉利贝拉岩石教堂的列入时间、数量与价值"),
"places/sacsayhuaman":dict(title="Parque Arqueologico Nacional de Saqsaywaman",publisher="Direccion Desconcentrada de Cultura de Cusco",url="https://www.culturacusco.gob.pe/parques-arqueologicos/saqsaywaman/",year="2024",license="政府文化机构页面；引用与事实核对",usage="萨克塞瓦曼国家考古公园的管理与保护"),
"places/sipan":dict(title="Visitar el Museo Tumbas Reales de Sipan",publisher="Ministerio de Cultura del Peru",url="https://www.gob.pe/10982-visitar-el-museo-tumbas-reales-de-sipan",year="2025",license="政府门户；引用与事实核对",usage="西潘王陵博物馆与西潘领主的官方说明"),
"tales/kettle-war":dict(title="Spotprent op de prins, de hertog en de politieke toestand van Nederland in 1784",publisher="Rijksmuseum / Europeana",url="https://www.europeana.eu/nl/item/90402/RP_P_OB_85_365",year="1784",license="公有领域",usage="1784 年荷兰政治危机的讽刺版画，作为时代背景；不是凯特尔战争本身记录"),
"tales/rajneeshee":dict(title="The 1984 Rajneeshee Bioterrorism Attack: An Example of Biological Warfare by Violent Non-state Actors",publisher="PMC / National Library of Medicine",url="https://pmc.ncbi.nlm.nih.gov/articles/PMC12369568/",year="2025",license="开放获取学术论文；引用与事实核对",usage="1984 年拉杰尼希生物恐怖袭击与调查"),
"tales/toledo-war":dict(title="The Toledo War",publisher="Michigan State University Department of Geography",url="https://project.geo.msu.edu/geogmich/toledo_war.html",year="2026",license="大学教学资料；引用与事实核对",usage="托莱多战争的边界争议与 1836 年妥协"),
}
def esc(s): return s.replace('"','\\"')
count=0
for key,d in DATA.items():
    ch,slug=key.split("/")
    p=os.path.join(ROOT,"entries",ch,slug,"entry.yml")
    text=open(p,encoding="utf-8").read()
    ids=[int(m) for m in re.findall(r"^  - id: S(\d+)$",text,re.M)]
    nid=max(ids)+1 if ids else 1
    block=f'  - id: S{nid}\n    title: "{esc(d["title"])}"\n    publisher: "{esc(d["publisher"])}"\n    url: {d["url"]}\n    year: "{d["year"]}"\n    license: "{esc(d["license"])}"\n    usage: {d["usage"]}\n'
    if "cover: " not in text:
        print("NO COVER",key); continue
    text=text.replace("cover: ",block+"cover: ",1)
    open(p,"w",encoding="utf-8",newline="\n").write(text)
    count+=1
print("updated",count)
