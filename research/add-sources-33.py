# -*- coding: utf-8 -*-
import os,re,json,yaml
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries\entries"
# key: (title, publisher, url, year, license, usage)
DATA={
"creatures/mothman":("Mothman of Point Pleasant: How a Bird Monster Became Appalachian Folklore","Appalachian Historian","https://appalachianhistorian.org/the-mothman-of-point-pleasant-how-a-bird-monster-became-appalachian-folklore/","2025","All rights reserved; citation only","1966 年 11 月首批报纸报道、目击者叙述与地方传说形成过程"),
"creatures/beast-of-gevaudan":("Première agression de la bête du Gévaudan","FranceArchives","https://francearchives.gouv.fr/pages_histoire/38726","2023","Public archive; citation only","1764 年 6 月第一名有记录死者、教区登记与三年袭击序列"),
"creatures/black-shuck":("The Black Dog of Bungay: Religious Conflict and Supernatural Terror in a Suffolk Parish","Journal of Religious History / Wiley","https://onlinelibrary.wiley.com/doi/full/10.1111/1467-9809.13099","2024","All rights reserved; citation only","1577 年 Bungay 教区记录、宗教冲突与黑狗叙事的史料批判"),
"creatures/puca":("The Púca","Fingal County Council","https://www.fingal.ie/puca","2026","© Fingal County Council; citation only","爱尔兰地方口述传统中的 Púca 故事与万圣节习俗"),
"objects/voynich-manuscript":("Can I view the Voynich Manuscript?","Yale University Library","https://ask.library.yale.edu/faq/174903","2024","© Yale University; citation only","手稿的保存状态、数字化影像与调阅限制"),
"creatures/dover-demon":("Dover Demon Revisited","Cryptomundo","https://cryptomundo.com/cryptozoo-news/dd-rev11/","2011","All rights reserved; citation only","1977 年 4 月目击、现场采访与后来《波士顿环球报》的回顾"),
"creatures/kuchisake-onna":("Kuchisake-onna","YOKAI.JP","https://yokai.jp/en/yokai/kuchisake-onna","2026","All rights reserved; citation only","1978–1979 年岐阜起源、1979 年日本全国性恐慌与口述版本"),
"creatures/mongolian-death-worm":("Olgoi-Khorkhoi: The Mongolian Death Worm","Skeptoid","https://skep.us/episodes/4344","2013","All rights reserved; citation only","蒙古戈壁传说、1920 年代西方记录与历次考察未获标本"),
"creatures/owlman":("Owlman: Did a Mysterious Creature Really Haunt the Cornish Town of Mawnan?","Curious Archive","https://curiousarchive.com/owlman-mawnan-cornwall","2021","All rights reserved; citation only","1976 年 Mawnan 教堂目击、女孩素描与 Tony Shiels 的传播角色"),
"creatures/vanishing-hitchhiker":("A History of the Vanishing Hitchhiker","California Folklore Quarterly / University of Warwick","https://warwick.ac.uk/fac/arts/modernlanguages/applying/undergraduate/crossschool/ln305/biblio/beardsley__hankey_a_history_of_the_vanishing_hitchhiker.pdf","1943","Academic article; citation only","1942–1943 年北美搭车鬼故事的类型记录与变体史"),
"mystery/angel-hair":("Condon Report Section III, Chapter 3: Direct Physical Evidence","University of Colorado / NCAS","http://condon.ncas.org/text/s3chap03.htm","1968","Public report; citation only","1952–1955 年 17 起“天使发丝”案例、样本分析与不确定结论"),
"mystery/bridgewater-triangle":("Into the Hockomock: Where wildlife and stories dwell","Mass.gov","https://www.mass.gov/news/into-the-hockomock-where-wildlife-and-stories-dwell","2025","© Commonwealth of Massachusetts; citation only","Hockomock 沼泽生态、地方历史与“Bridgewater Triangle”传说的官方介绍"),
"mystery/dancing-forest":("Kuršių Nerija (Curonian Spit) National Park","State Service for Protected Areas, Lithuania","https://saugoma.lt/en/territories/kursiu-nerija-curonian-spit-national-park","2026","© Lithuanian government; citation only","库尔斯沙嘴国家公园的保护范围与管理背景；舞动森林位于该保护区内"),
"mystery/fairy-circles":("Evolution at the arid extreme: the influence of climate on sand termite colonies and fairy circles of the Namib Desert","Philosophical Transactions of the Royal Society B","https://royalsocietypublishing.org/rstb/article/378/1884/20220149/42844","2023","All rights reserved; citation only","纳米布仙女环的白蚁假说、气候梯度与长期样地证据"),
"mystery/foo-fighters":("Royal Air Force combat reports 1939-1945","The National Archives (UK)","http://www.nationalarchives.gov.uk/help-with-your-research/research-guides/raf-combat-reports-1939-1945","2026","Open Government Licence; citation only","二战飞行员战斗报告档案的范围与查档方法；foo fighter 报告所属的记录类型"),
"mystery/min-min-lights":("Outback Queensland is something else","Queensland, Australia","https://www.queensland.com/gb/en/outback-queensland-is-something-else","2026","© Tourism and Events Queensland; citation only","Boulia 地区 Min Min Light 的地方口述、1912 年客栈火灾后的早期叙述"),
"mystery/phoenix-lights":("Phoenix Lights Revisited","NICAP","https://www.nicap.org/articles/PhoenixLights_MUJ_Feb1999.pdf","1999","All rights reserved; citation only","1997 年 3 月 13 日目击、军方照明弹解释与目击者访谈"),
"mystery/shag-harbour":("UFOs at LAC: The Falcon Lake Incident - Part 1","Library and Archives Canada","https://library-archives.canada.ca/eng/collection/engage-learn/podcast/Pages/ufo-falcon-lake-incident.aspx","2019","© Government of Canada; citation only","加拿大国家档案馆 UFO 档案的背景说明；其中讨论 Shag Harbour 1967 年档案的保存与缺口"),
"mystery/varginha-ufo":("OS ETS DE VARGINHA","Arquivo Nacional (Brazil)","https://imagem.sian.an.gov.br/acervo/derivadas/BR_DFANBSB_ARX/0/0/0462/BR_DFANBSB_ARX_0_0_0462_d0001de0001.pdf","1996","Public archive; citation only","1996 年 1 月 Varginha 事件的军方调查卷宗与民间报告"),
"mystery/washington-merry-go-round":("Records Related to Unidentified Flying Objects (UFOs) and Unidentified Anomalous Phenomena (UAPs) at the National Archives: Textual and Microfilm","U.S. National Archives","https://www.archives.gov/research/topics/uaps/textual-and-microfilm","2026","Public domain; citation only","1952 年华盛顿事件的 Project Blue Book 档案位置与调阅线索"),
"objects/annabelle-doll":("About Us","Haunted Warren Museum","https://hauntedwarrenmuseum.com/about-us/","2026","© museum; citation only","Annabelle 娃娃的现藏地、展陈方式与 Warren 博物馆的官方叙述"),
"objects/crystal-skulls":("Mysterious Crystal Skull on Exhibit for the First Time at Smithsonian’s National Museum of Natural History","Smithsonian Institution","https://www.si.edu/newsdesk/releases/mysterious-crystal-skull-exhibit-first-time-smithsonian-s-national-museum-natural-history","2008","© Smithsonian; citation only","史密森尼藏水晶头骨的现代工具痕、来源链与 2008 年研究结论"),
"objects/kusanagi":("Atsuta-jingu Shrine","Japan National Tourism Organization","https://www.japan.travel/en/spot/1231/","2026","© JNTO; citation only","草薙剑在热田神宫的供奉位置、非公开展示状态与神社历史"),
"objects/stigmata":("A Psychopathological Reading of the Blood Sweat Phenomenon and Religious Stigmas: The Case of Blessed Elena Aiello","PubMed / Turkish Psychiatry","https://pubmed.ncbi.nlm.nih.gov/41070472/","2025","Academic article; citation only","圣痕案例的医学与精神病学讨论、教会认可程序与自然解释争议"),
"places/atlantis":("Timaeus (25)","Perseus Digital Library, Tufts University","https://atlas.perseus.tufts.edu/library/passage/urn:cts:greekLit:tlg0059.tlg031.perseus-eng2:25/","2026","Public domain translation; citation only","柏拉图《蒂迈欧篇》25a–25b 关于亚特兰蒂斯的原始叙述"),
"tales/bre-x":("Re: John Felderhof & Bre-X Minerals Ltd.","Ontario Securities Commission","https://www.osc.ca/en/news-events/news/re-john-felderhof-bre-x-minerals-ltd","1999","© OSC; citation only","Bre-X 欺诈案的监管指控、内幕交易与安大略证券法程序"),
"tales/dancing-plague":("Alors, on danse! Propos sur les épidémies de fièvre dansante au début de l’ère moderne","Société Française d’Histoire de la Médecine / Sorbonne","https://numerabilis.u-paris.fr/ressources/pdf/sfhm/esfhm/esfhmx2019x04/esfhmx2019x04x018.pdf","2019","Academic article; citation only","1518 年斯特拉斯堡舞蹈瘟疫的编年史、城市议事记录与医学史解释"),
"tales/dyatlov-pass":("Prosecution agencies rule out authorities’ involvement in 1959 Dyatlov Pass incident","TASS","https://tass.com/society/1043155","2019","© TASS; citation only","2019 年俄罗斯检察院复查、75 种版本与雪崩/飓风假说"),
"tales/maura-murray":("Frederick J. Murray v. New Hampshire Division of State Police, Special Investigation Unit & a.","New Hampshire Supreme Court / Justia","https://cases.justia.com/new-hampshire/supreme-court/murra152.pdf","2007","Public court record; citation only","2004 年 2 月 9 日失踪、车辆发现经过与警方档案调阅诉讼"),
"tales/piltdown-man":("British Museum (Natural History): Department of Palaeontology: Piltdown Man: Records","The National Archives (UK)","https://discovery.nationalarchives.gov.uk/details/r/be8a8446-e786-47c9-b941-d68ada893240","2026","Open Government Licence; citation only","1912–1983 年 Piltdown 档案、标本记录与 1953 年揭穿后的调查材料"),
"creatures/spring-heeled-jack":("Spring-heeled Jack: The Terror of London","University of Northampton / NECTAR","https://nectar.northampton.ac.uk/id/eprint/9059/7/Mackley20169059.pdf","2016","Academic article; citation only","1838 年 2 月 Alsop 袭击、报纸报道与“弹簧腿杰克”名称的形成"),
"creatures/almas":("The Legend of the Almas: A Comparative and Critical Analysis","SIT Digital Collections","https://digitalcollections.sit.edu/cgi/viewcontent.cgi?article=1780&context=isp_collection","2026","Academic thesis; citation only","阿尔玛斯口述传统、苏联考察与尼安德特人假说的批判性回顾"),
"creatures/beast-of-bray-road":("All about Wisconsin's notorious Beast of Bray Road","Up North News","https://upnorthnewswi.com/community/all-about-wisconsins-notorious-beast-of-bray-road/","2025","All rights reserved; citation only","1936 年看夜人叙述、1990 年代 Linda Godfrey 报道与 Walworth County 目击"),
}
def block(sid,title,pub,url,year,lic,usage):
    q=lambda s:json.dumps(s,ensure_ascii=False)
    return (f"  - id: {sid}\n"
            f"    title: {q(title)}\n"
            f"    publisher: {q(pub)}\n"
            f"    url: {q(url)}\n"
            f"    year: {q(year)}\n"
            f"    license: {q(lic)}\n"
            f"    usage: {q(usage)}\n")
count=0
for key,(title,pub,url,year,lic,usage) in DATA.items():
    ch,slug=key.split("/"); p=os.path.join(ROOT,ch,slug,"entry.yml")
    t=open(p,encoding="utf-8").read(); d=yaml.safe_load(t)
    existing=[s.get("url") for s in d.get("sources",[])]
    if url in existing:
        print("skip",key); continue
    ids=[int(m) for m in re.findall(r"^\s*-\s*id:\s*S(\d+)",t,flags=re.M)]
    sid=f"S{max(ids)+1 if ids else 1}"
    nb=block(sid,title,pub,url,year,lic,usage)
    if "\ncover:" not in t:
        print("NO COVER",key); continue
    t=t.replace("\ncover:","\n"+nb+"cover:",1)
    open(p,"w",encoding="utf-8",newline="\n").write(t)
    print("add",key,sid)
    count+=1
print("updated",count)
