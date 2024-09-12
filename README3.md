# Endurraða skrá

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