import os,re,json,urllib.parse,requests,yaml
ROOT=r"C:\Users\chenhua\Desktop\xiqiqi\repos\oddities-and-mysteries"
proxy={"http":"http://127.0.0.1:7890","https":"http://127.0.0.1:7890"}
TRUST=("unesco.org","whc.unesco.org","britishmuseum.org","metmuseum.org","si.edu","smithsonianmag.com","nasa.gov","noaa.gov","nps.gov","loc.gov","archives.gov","gov.uk","bbc.co.uk","britannica.com","nature.com","science.org","scientificamerican.com","nationalgeographic.com","edu","museum","archive","ac.uk","ucla.edu","yale.edu","harvard.edu")
def page_from(url):
    p=urllib.parse.urlparse(url)
    if "wiki" not in p.netloc: return None
    part=p.path.split("/wiki/")
    if len(part)<2: return None
    return urllib.parse.unquote(part[1]).replace("_"," ")
for ch,slug in [("mystery","blood-falls"),("places","hypogeum"),("objects","sword-of-goujian"),("creatures","mothman"),("tales","rajneeshee")]:
    y=yaml.safe_load(open(os.path.join(ROOT,"entries",ch,slug,"entry.yml"),encoding="utf-8"))
    page=None
    for s in y.get("sources",[]):
        page=page_from(s.get("url",""))
        if page: break
    print("\n==",ch,slug,"page_found",bool(page))
    if not page: continue
    r=requests.get("https://en.wikipedia.org/w/api.php",params={"action":"parse","page":page,"prop":"externallinks","format":"json","redirects":1},proxies=proxy,timeout=30,headers={"User-Agent":"xiqiqi-coverage-audit/1.0"})
    print("status",r.status_code)
    if r.status_code!=200: continue
    links=r.json().get("parse",{}).get("externallinks",[])
    picks=[u for u in links if any(t in urllib.parse.urlparse(u).netloc.lower() for t in TRUST)]
    for u in picks[:12]: print(u)
