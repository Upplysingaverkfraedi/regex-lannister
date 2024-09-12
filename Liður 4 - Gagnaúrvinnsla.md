# Liður 4 - Gagnaúrvinnsla
- Veljið mót frá tímataka.net sem inniheldur keppanda sem þið þekkið eða hefur áhuga á.
- Notið reglulegar segðir til að sækja HTML-skjalið frá vefsíðunni, vinna úr gögnunum og umbreyta í CSV-skrá.
- Gætið þess að aðeins nota reglulegar segðir til að vinna úr HTML-gögnunum (ekki nota BeautifulSoup eða aðra pakka).
- Skrifið Python kóða sem framkvæmir þetta ferli, með möguleika á að vista HTML-skrár ef --debug er notað.


## Forritið  
Python forritið tekur hrágögn af vefsíðunni timataka.net og umbreytir þeim yfir í auðlesanlega csv skrá. 


## Vinnsla 
Farið var yfir mótin á vefsíðunni og ekki áhugavert var að ská Hundahlaupið 2024 og því varð það fyrir valinu að þessu sinni. 

Næst var tekin beinagrindin af kóðanum code/timataka.py og unnið var í def parse_html(html): til þess að útfæra reglulega segð sem tekur til gagna úr html skránni. Reglulegu segðirnar eru eftirfarandi: 

    lina_pattern = re.compile(r'<tr>(.*?)</tr>', re.DOTALL)

    dalkur_pattern = re.compile(r'<td[^>]*>(.*?)</td>', re.DOTALL)

Nú skulum við skoða nánar hvað þessar reglulegu segir þýða: 
- "<tr>" er notað til að skilgreina byrjun á línu af töflu í html skrá 
- "." stendur fyrir hvaða bókstaf sem er 
- "*" hvaða bókstafur sem er kemur í 0 eða fleiri skipti
- "?" leitar af minnstu mögulegu samsvörun frekar en lengstu 
- </tr> lokamerki línunnar í töflunni 
- re.DOTALL segir Python að innihald línunnar getur verið í mörgum línum, ss. "." samsvarar \n bókstafi. 
- "<"td>" er notað til að tákna byrjun á dálki í html skrá
- "[^>]*" passar við 0 eða fleiri bókstafi sem eru ekki >
- </td> lokamerki dálksins í töflunni. 


## Breytingar á kóðanum: 
Beinagrind af kóðanum fékkst undir Code á github. Til þess að klára kóðann og fá hann til þess að keyra þurfti að bæta aðeins við beinagrindina. Því sem var breytt var aðallega undir "parse_html" og "skrifa_nidurstodur" og aðeins undir main fallinu. 

### parse_html: 
Hér voru búnar til reglulegar segðir til að taka in gögn úr html skránni, einnig var athugað með if-setningu hvort að skráin inniheldi 7 dálka eins og skráin sem við vorum búin að velja af vefsíðunni. 

### skrifa_nidurstodur: 
Hér var bætt við nöfnunum á dálkunum 7. 


## Keyrsla 
1. Til þess að keyra kóðann þarf að setja eftirfarandi slóð í console.

python3 Lidur4.py --url "https://timataka.net/hundahlaupid2024/urslit/?race=1&cat=overall" --output data/hlaup.csv --debug

2. Í kjölfarið sendir forritið "request" til URL til þess að sækja HTML skránna af vefsíðunni. 

3. Forritið notar reglulegu segðirnar til að finna allar línur og dálka innan töflunnar.

4. Forritið skrifar næst csv skrá út frá sóttu gögnunum og setur nöfn á dálkana. 

5. Forritið segir til um það ef csv skráin sé klár, eða sendir villubeiðni ef keyrslan gekk ekki upp. 

elisabet@Elisabets-Air regex-lannister % python3 Lidur4.py --url "https://timataka.net/hundahlaupid2024/urslit/?race=1&cat=overall" --output data/hlaup.csv --debug
HTML fyrir https://timataka.net/hundahlaupid2024/urslit/?race=1&cat=overall vistað í data/hlaup.html
Skipping header row
Niðurstöður vistaðar í 'data/hlaup.csv'.
elisabet@Elisabets-Air regex-lannister % 

## Notkun: 
1. Sjáðu til þess að búið sé að hlaða Python í tölvuna og öllum nauðsynlegu pökkum. Í þessu tilfelli eru það: 
import requests
import pandas as pd
import argparse
import re

2. Keyrðu forritið með slóðinni fyrir ofan. 

3. Kostur er á að vista sérstaklega HTML skránna hjá sér með Debug flagginu. Ef þið hafið einungis áhuga á csv skránni á er slóðin fyrir ofan keyrð án þess að hafa --debug. 

4. Forritið vistar niðurstöðurnar úr Hundahlaupinu í csv skrá sem mun vera með 7 dálkum og 64 línum samsvarandi töflunni á vefsíðunni. 

5. Ef eitthvað kemur upp á þá mun koma villumelding eins og "Tókst ekki að sækja gögn af {url}" eða "Slóðin er ekki frá timataka.net eða ekki með úrslitum." o.s.frv. 