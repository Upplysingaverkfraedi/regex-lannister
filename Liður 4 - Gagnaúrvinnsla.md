# 4. Gagnaúrvinnsla - útskýringar

## Verkefnalýsing 
- Veljið mót frá tímataka.net sem inniheldur keppanda sem þið þekkið eða hefur áhuga á.
- Notið reglulegar segðir til að sækja HTML-skjalið frá vefsíðunni, vinna úr gögnunum og umbreyta í CSV-skrá.
- Gætið þess að aðeins nota reglulegar segðir til að vinna úr HTML-gögnunum (ekki nota BeautifulSoup eða aðra pakka).
- Skrifið Python kóða sem framkvæmir þetta ferli, með möguleika á að vista HTML-skrár ef --debug er notað.


## Forritið  
Python forritið tekur hrágögn af vefsíðunni timataka.net og umbreytir þeim yfir í auðlesanlega CSV skrá. Forritið notar reglulegar segðir til gagnaúrvinnslu úr HTML töflum.


## Vinnsla 
Farið var yfir mótin á vefsíðunni og áhugavert var að sjá Hundahlaupið 2024 og því varð það fyrir valinu að þessu sinni. 

Næst var tekin beinagrindin af kóðanum code/timataka.py og unnið var í def parse_html(html) til þess að útfæra reglulega segð sem tekur til gagna úr HTML skránni. Reglulegu segðirnar eru eftirfarandi: 

    - row_pattern = re.compile(r'<tr>(.*?)</tr>', re.DOTALL)

    - column_pattern = re.compile(r'<td[^>]*>(.*?)</td>', re.DOTALL)

### Nú skulum við skoða nánar hvað þessar reglulegu segir þýða: 
- `<tr>` er notað til að skilgreina byrjun á línu af töflu í HTML skrá 
- `.` stendur fyrir hvaða bókstaf sem er 
- `*` hvaða bókstafur sem er kemur í 0 eða fleiri skipti
- `?` leitar af minnstu mögulegu samsvörun frekar en lengstu 
- `</tr>` lokamerki línunnar í töflunni 
- `re.DOTALL` segir Python að innihald línunnar getur verið í mörgum línum, ss. "." samsvarar \n bókstafi. 
- `<"td>` er notað til að tákna byrjun á dálki í HTML skrá
- `[^>]*` passar við 0 eða fleiri bókstafi sem eru ekki >
- `</td>` lokamerki dálksins í töflunni. 


## Breytingar á kóðanum: 
Beinagrind af kóðanum fékkst undir Code á Github. Til þess að klára kóðann og fá hann til þess að keyra þurfti að bæta aðeins við beinagrindina. Því sem var breytt var undir "parse_html" og svo voru if-skilyrðin í main fallinu aðeins lagfærð. 

### parse_html: 
Hér voru búnar til reglulegar segðir til að taka in gögn úr HTML skránni. Einnig var búinn til kóðabútur sem les inn hverja línu af skránni og hreinsar til hvern dálk og skilar svo lista yfir gildin í hverjum dálki í hverri línu af HTML skránni. 
`r'<[^>]+>'` segðin er hér notuð til þess að hreinsa gögn frá HTML skránni til að tryggja að þau séu rétt útlesin. 

### main fall: 
Hér var bætt við því að athuga bæði hvort URL sé frá timataka.net og hvort hún hafi 'urslit'. Þetta tryggir að forritið keyrir aðeins á réttri vefsíðu og notast aðeins við úrslit úr keppnum. 

 
