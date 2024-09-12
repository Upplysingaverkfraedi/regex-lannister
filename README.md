
# 1. Kennitölu leitarforrit

Þetta Python forrit leitar að kennitölum einstaklinga og fyrirtækja úr textaskrá með reglulegum segðum. Forritið gefur notanda val um hvort hann vilji fá einstaklings, fyrirtækja eða bæði

## Kröfur

#### Python: 

Fyrst þarf að vera klárt að Python sé uppsett á tölvunni. Þú getur athugað það með því að keyra `python --version` í skipanalínunni.

## Uppsetning

### 1. Hala niður forritinu
Fyrst hala niður öllum viðeigandi skrám af Github, Lidur1seinniHluti.py og testTexti.txt ef þú vilt pre-made prófunartexta, annars má nota hvaða .txt file sem er. Hér þarf að passa að allar skrár séu inn í sömu möppu svo að það verði ekki vandamál með keyrslu með skipanalínunni.

### 2. Settu upp Python (ef það er ekki uppsett)
- **Windows**:
  1. Farðu á [Python niðurhalsvefinn](https://www.python.org/downloads/) og halaðu niður nýjustu útgáfunni af Python.
  2. Keyrðu uppsetningarskrána og vertu viss um að haka við "Add Python to PATH" áður en þú klikkar á "Install".
  3. Eftir að uppsetningunni er lokið skaltu opna skipanalínuna og slá inn `python --version` til að athuga hvort Python hafi verið rétt uppsett.

- **macOS/Linux**:
  1. Farðu á [Python niðurhalsvefinn](https://www.python.org/downloads/) og fylgdu leiðbeiningunum fyrir macOS/Linux.
  2. Eftir uppsetningu geturðu athugað með því að opna „Terminal“ og keyra `python3 --version`.

### 3. Keyra forritið
  1. Keyra forritið með: python Lidur1seinniHluti.py (python3 fyrir macOS)
  2. Forritið biður um textaskrá sem það á að lesa kennitölur úr. Hér má nota fyrirframgerða textaskrá inná Github, eða hvaða textaskrá sem er, svo lengi sem kennitölurnar eru á eftirfarandi formi: XXXXXX-XXXX.
  3. Síðan kemur beiðni um val á leit, einstaklings (slá inn 1 og Enter), fyrirtækja (slá inn 2 og Enter) eða bæði (slá inn 3 og Enter)
  4. Forritið prentar síðan út allar umbeðnar kennitölur sem eru á rétta forminu

## Dæmi um keyrslu

Ef forritið er keyrt með testTexti.txt sem input, og bæði einstaklings- og fyrirtækjakennitölur eru valdar fæst eftirfarandi output:

Kennitölur einstaklinga:
010199-3459
230585-1230
150377-4329
011200-5670

Kennitölur fyrirtækja:
6001-692039
7108-118760

Hér er heildarkeyrslan úr Command glugganum:

C:\Users\bened\OneDrive - Menntaský\Documents\GitHub\regex-lannister>python Lidur1seinniHluti.py

Sláðu inn nafn á textaskrá (t.d. 'input.txt'): testTexti.txt

Viltu einstaklings (1), fyrirtækja (2) eða bæði (3)? (1/2/3): 3

Kennitölur einstaklinga:
010199-3459
230585-1230
150377-4329
011200-5670

Kennitölur fyrirtækja:
6001-692039
7108-118760





# 2. Lögleg email

Þetta Python forrit les inn inn texta skrá með netföngum og prentar út hvaða email eru lögleg.

## Kröfur

#### Python: 

Fyrst þarf að vera klárt að Python sé uppsett á tölvunni. Þú getur athugað það með því að keyra `python --version` í skipanalínunni.

## Uppsetning

### 1. Hala niður forritinu
Nauðsynlegt er að hlaða niður repoinu áður en haldið er lengra. það er gert með
```
git@github.com:Upplysingaverkfraedi/regex-lannister.git
```

### 2. Settu upp Python (ef það er ekki uppsett)
- **Windows**:
  1. Farðu á [Python niðurhalsvefinn](https://www.python.org/downloads/) og halaðu niður nýjustu útgáfunni af Python.
  2. Keyrðu uppsetningarskrána og vertu viss um að haka við "Add Python to PATH" áður en þú klikkar á "Install".
  3. Eftir að uppsetningunni er lokið skaltu opna skipanalínuna og slá inn `python --version` til að athuga hvort Python hafi verið rétt uppsett.

- **macOS/Linux**:
  1. Farðu á [Python niðurhalsvefinn](https://www.python.org/downloads/) og fylgdu leiðbeiningunum fyrir macOS/Linux.
  2. Eftir uppsetningu geturðu athugað með því að opna „Terminal“ og keyra `python3 --version`.

### 3. Setja upp pakka
Nauðsynlegt er að setja upp argparse pakkan áður en forritið er keyrt. Það er gert með
```pip install argparse```

### 4. Keyra forritið
  1. Keyra forritið með:
  ```python Liður-2.py --file=data/email.txt```
  2. Forritið biður um textaskrá í gegnum file inntakið sem það á að lesa email úr. Hér má nota fyrirframgerða textaskrá inná Github, eða hvaða textaskrá sem er.
  4. Forritið prentar síðan út öll lögleg email

## Dæmi um keyrslu

**data/email.txt**
```
helgaingim@hi.is
hei2@hi.is
john.smith@new-world.us
python101@regex101.edu.com
john.smith@new-world
@noaddress.com
plainaddress
of@langt.domainnafn
jane.doe@@hi.is
username@.com
email@domain..com
```

**Terminal**
```
python Liður-2.py --file=data/email.txt
Fundin netföng:
helgaingim@hi.is

hei2@hi.is

john.smith@new-world.us

python101@regex101.edu.com
```



# 3. Endurraða skrá

Þetta forrit les inn skrá í gegnum inntak og endurraðar henni í nýja skrá gefna upp í útakinu.

## Kröfur

#### Python: 

Fyrst þarf að vera klárt að Python sé uppsett á tölvunni. Þú getur athugað það með því að keyra `python --version` í skipanalínunni.

## Uppsetning

### 1. Hala niður forritinu
Nauðsynlegt er að hlaða niður repoinu áður en haldið er lengra. það er gert með
```
git@github.com:Upplysingaverkfraedi/regex-lannister.git
```

### 2. Settu upp Python (ef það er ekki uppsett)
- **Windows**:
  1. Farðu á [Python niðurhalsvefinn](https://www.python.org/downloads/) og halaðu niður nýjustu útgáfunni af Python.
  2. Keyrðu uppsetningarskrána og vertu viss um að haka við "Add Python to PATH" áður en þú klikkar á "Install".
  3. Eftir að uppsetningunni er lokið skaltu opna skipanalínuna og slá inn `python --version` til að athuga hvort Python hafi verið rétt uppsett.

- **macOS/Linux**:
  1. Farðu á [Python niðurhalsvefinn](https://www.python.org/downloads/) og fylgdu leiðbeiningunum fyrir macOS/Linux.
  2. Eftir uppsetningu geturðu athugað með því að opna „Terminal“ og keyra `python3 --version`.

### 3. Setja upp pakka
Nauðsynlegt er að setja upp argparse pakkan áður en forritið er keyrt. Það er gert með
```pip install argparse```

### 4. Keyra forritið
  1. Keyra forritið með:
  ```python3 Liður-3.py --infile=data/nafn_heimilisfang_simanumer.csv --outfile=data/out.tsv```
  2. Forritið biður um textaskrá í gegnum infile inntakið sem það á að lesa úr og skilar svo svarinu í nýja skrá gefin upp í outfile inntakinu. Hér má nota fyrirframgerða textaskrá inná Github, eða hvaða skrá sem er.

## Dæmi um keyrslu

**data/nafn_heimilisfang_simanumer.csv**
```
Jón Jónsson, Litla-Saurbæ, 816 Ölfusi, 555-1234
Guðrún Helgadóttir, Fiskislóð 15, 101 Reykjavík, 510-7000
Jón Oddur Guðmundsson, Úthlíð 6, 450 Patreksfirði, 897-1234
```

**Terminal**
```
python3 Liður-3.py --infile=data/nafn_heimilisfang_simanumer.csv --outfile=data/out.tsv
```

**data/out.tsv**
```
Litla-Saurbæ	816 Ölfusi	555-1234	Jónsson, Jón
Fiskislóð 15	101 Reykjavík	510-7000	Helgadóttir, Guðrún
Úthlíð 6	450 Patreksfirði	897-1234	Guðmundsson, Jón Oddur
```


# 4. Gagnaúrvinnsla

## Forritið  
Python forritið tekur hrágögn af vefsíðunni timataka.net og umbreytir þeim yfir í auðlesanlega csv skrá. 

## Keyrsla 
1. Til þess að keyra kóðann þarf að setja eftirfarandi slóð í console.

`python3 Lidur4.py --url "https://timataka.net/hundahlaupid2024/urslit/?race=1&cat=overall" --output data/hlaup.csv --debug`

2. Í kjölfarið sendir forritið "request" til URL til þess að sækja HTML skránna af vefsíðunni. 

3. Forritið notar reglulegu segðirnar til að finna allar línur og dálka innan töflunnar.

4. Forritið skrifar næst csv skrá út frá sóttu gögnunum og setur nöfn á dálkana. 

5. Forritið segir til um það ef csv skráin sé klár, eða sendir villubeiðni ef keyrslan gekk ekki upp. 

Hér má sjá hvernig keyrslan kemur út: 

`elisabet@Elisabets-Air regex-lannister % python3 Lidur4.py --url "https://timataka.net/hundahlaupid2024/urslit/?race=1&cat=overall" --output data/hlaup.csv --debug
HTML fyrir https://timataka.net/hundahlaupid2024/urslit/?race=1&cat=overall vistað í data/hlaup.html
Niðurstöður vistaðar í 'data/hlaup.csv'.
elisabet@Elisabets-Air regex-lannister % `

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