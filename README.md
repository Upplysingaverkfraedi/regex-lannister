# Reglulegar segðir (Regular Expressions)

## Forritið  
Python forritið tekur hrágögn af vefsíðunni timataka.net og umbreytir þeim yfir í auðlesanlega csv skrá. 

## Keyrsla 
1. Til þess að keyra kóðann þarf að setja eftirfarandi slóð í console.

python3 Lidur4.py --url "https://timataka.net/hundahlaupid2024/urslit/?race=1&cat=overall" --output data/hlaup.csv --debug

2. Í kjölfarið sendir forritið "request" til URL til þess að sækja HTML skránna af vefsíðunni. 

3. Forritið notar reglulegu segðirnar til að finna allar línur og dálka innan töflunnar.

4. Forritið skrifar næst csv skrá út frá sóttu gögnunum og setur nöfn á dálkana. 

5. Forritið segir til um það ef csv skráin sé klár, eða sendir villubeiðni ef keyrslan gekk ekki upp. 

Hér má sjá hvernig keyrslan kemur út: 

elisabet@Elisabets-Air regex-lannister % python3 Lidur4.py --url "https://timataka.net/hundahlaupid2024/urslit/?race=1&cat=overall" --output data/hlaup.csv --debug
HTML fyrir https://timataka.net/hundahlaupid2024/urslit/?race=1&cat=overall vistað í data/hlaup.html
Niðurstöður vistaðar í 'data/hlaup.csv'.
elisabet@Elisabets-Air regex-lannister % 

## Notkun: 
1. Sjáðu til þess að búið sé að hlaða Python í tölvuna og öllum nauðsynlegu pökkum. Í þessu tilfelli eru það: 
- import requests
- import pandas as pd
- import argparse
- import re

Til þess að fullvissa sig um að Python sé rétt sett upp í tölvunni er hægt að keyra `python --version` eða `python3 --version` í skipanalínunni. 

3. Keyrðu forritið með slóðinni fyrir ofan. 

4. Kostur er á að vista sérstaklega HTML skránna hjá sér með Debug flagginu. Ef þið hafið einungis áhuga á csv skránni á er slóðin fyrir ofan keyrð án þess að hafa --debug. 

5. Forritið vistar niðurstöðurnar úr Hundahlaupinu í csv skrá sem mun vera með réttum dálkum og línum samsvarandi töflunni á vefsíðunni. 

6. Ef eitthvað kemur upp á þá mun koma villumelding eins og "Tókst ekki að sækja gögn af {url}" eða "Slóðin er ekki frá timataka.net eða ekki með úrslitum." o.s.frv. 
