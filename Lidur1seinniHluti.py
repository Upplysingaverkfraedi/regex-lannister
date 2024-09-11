import re

## Ég byrja á að setja upp smá texta sem við getum notað til að keyra kóðann

with open('input.txt', 'r') as file:
    texti = file.read()

## Nú set ég upp reglulegu segðirnar sem ég setti fram fyrr í lausninni

einstaklings_regex = r'\b(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])(\d{2})-(\d{2})(\d{1})([89]|0)\b'

fyrirtaekja_regex = r'\b(4|5|6|7)([0-9])(0[1-9]|1[0-2])(\d{2})-(\d{2})(\d{1})([89]|0)\b'

## Hér er beðið um val á einstaklings, fyrirtækja eða bæði

val = input("Viltu einstaklings (1), fyrirtækja (2) eða bæði (3)? (1/2/3):")

## Út frá valinu leitar forritið að viðeigandi kennitölum

if val == '1':
    einstaklingar = re.findall(einstaklings_regex, texti)
    print("Kennitölur einstaklinga:")
    for kt in einstaklingar:
        print(kt)
elif val == '2':
    fyrirtaeki = re.findall(fyrirtaekja_regex, texti)
    print("Kennitölur fyrirtækja:")
    for kt in fyrirtaeki:
        print(kt)
elif val == '3':
    einstaklingar = re.findall(einstaklings_regex, texti)
    fyrirtaeki = re.findall(fyrirtaekja_regex, texti)
    print("Kennitölur einstaklinga:")
    for kt in einstaklingar:
        print(kt)
    print("\nKennitölur fyrirtækja:")
    for kt in fyrirtaeki:
        print(kt)
else:
    print("Ógilt val.")