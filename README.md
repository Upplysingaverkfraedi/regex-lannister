# Kennitölu leitarforrit

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

