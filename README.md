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


