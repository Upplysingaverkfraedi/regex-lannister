import re

# Biður um skráarheiti frá notanda
filename = input("Sláðu inn nafn á textaskrá (t.d. 'input.txt'): ")

# Opnar og les skránna
try:
    with open(filename, 'r') as file:
        texti = file.read()
except FileNotFoundError:
    print(f"Ekki tókst að finna skrána '{filename}'.")
    exit()

# Reglulegar segðir fyrir kennitölur einstaklinga og fyrirtækja
einstaklings_regex = r'\b(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])(\d{2})-(\d{2})(\d{1})([89]|0)\b'
fyrirtaekja_regex = r'\b(4|5|6|7)([0-9])(0[1-9]|1[0-2])(\d{2})-(\d{2})(\d{1})([89]|0)\b'

# Biður notandann um val á einstaklings, fyrirtækja eða bæði
val = input("Viltu einstaklings (1), fyrirtækja (2) eða bæði (3)? (1/2/3): ")

# Fall til að setja bandstrik á réttan stað milli 6. og 7. tölustafs
def format_kennitala(match):
    return ''.join(match[:3]) + '-' + ''.join(match[3:])

# Leitar að viðeigandi kennitölum eftir vali
if val == '1':
    einstaklingar = re.findall(einstaklings_regex, texti)
    print("Kennitölur einstaklinga:")
    for kt in einstaklingar:
        print(format_kennitala(kt))
elif val == '2':
    fyrirtaeki = re.findall(fyrirtaekja_regex, texti)
    print("Kennitölur fyrirtækja:")
    for kt in fyrirtaeki:
        print(format_kennitala(kt))
elif val == '3':
    einstaklingar = re.findall(einstaklings_regex, texti)
    fyrirtaeki = re.findall(fyrirtaekja_regex, texti)
    print("Kennitölur einstaklinga:")
    for kt in einstaklingar:
        print(format_kennitala(kt))
    print("\nKennitölur fyrirtækja:")
    for kt in fyrirtaeki:
        print(format_kennitala(kt))
else:
    print("Ógilt val.")
