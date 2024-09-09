import re
import argparse
import os

#Finna segð sem les helgaingim@hi.is, hei2@hi.is, john.smith@new-world.us, python101@regex101.edu.com og john.smith@new-world 
# en ekki @noaddress.com, plainaddress, of@langt.domainnafn, jane.doe@@hi.is, username@.com, email@domain..com

# Segðin er: ^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,6})?$

#Útskýring: 
# [a-zA-Z0-9._%+-]+ segir að innihald svigans getur innihaldið hvaða stafi (bæði há- og lágstafi), tölur, og táknin . (punktur), _ (undirstrik), %, +, og -.
# + þarf að vera í lokin þar sem eitt af þessum merkjum þarf að vera í emailinu allavega einu sinni 
# @ sem skilur notendanafnið frá léninu í tölvupóstfangi.
# [a-zA-Z0-9-]+. Þetta skilgreinir lénshlutann fyrir framan punktinn (t.d. hi í hi.is). Leyfilegt er að hafa stafi (há- og lágstafi), tölustafi og bandstrik - í þessum hluta.+ merkið gefur til kynna að það þarf að vera að minnsta kosti einn slíkur stafur.
# \.[a-zA-Z]{2,6}: Þetta tryggir að topp-lénið (t.d. .com, .is) sé á milli 2 og 6 stafa langt. 
# og þarf backslash að vera á undan punkti svo punkturinn þýðir ekki hvaða staf sem er heldur bókstaflega punkt. 
# (?:\.[a-zA-Z]{2,6})? tryggir að undir-lén (t.d. .co.uk) sé einnig á milli 2 og 6 stafa langt, en er valfrjálst.
# Spurningarmerkið ? á eftir hópnum gerir allt þetta valfrjálst (það má koma einu sinni eða ekki koma).



def parse_arguments():
    """
    Lesa inn argument frá skipanalínu
    :return: (ArgumentParser) parser með argumentunum
    """

    parser = argparse.ArgumentParser(description='Leita að netföngum úr skrá.')
    parser.add_argument('--file', required=True,
                        help='Slóð að inntaksskrá með netföngum.')
    return parser.parse_args()


def lesa_skra(file_path):
    """
    Lesa inntaksskrá og skila lista af línum
    :param file_path: (str) Slóð að skrá
    :return:          (list) Listi af línum
    """

    with open(file_path, 'r') as file:
        return file.readlines()


# Breyta kóðanum hér 
def finna_netfong (text):
    """
    Leita að netföngum í texta
    :param text: (list) Listi af línum
    :return:     (list) Listi af netföngum
    
    """
  # Reglusegð til að finna netföng
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,6})?'
    
    # Samstilla segðina
    compiled_pattern = re.compile(pattern)
    matches = compiled_pattern.finditer(text)
    
    # Búa til lista fyrir niðurstöður
    results = []

    raise NotImplementedError("Regluleg segð til að finna netföng hefur ekki verið útfærð.")

    

def prenta_nidurstodur(netfong_listi):
    """
    Prentar út niðurstöður í console
    :param netfong_listi: (list) Listi af netföngum
    :return:              None
    """

    if netfong_listi:
        print("Fundin netföng:")
        for email in netfong_listi:
            print(email)
    else:
        print("Engin netföng fundust.")


def main():
    """
    Keyrslufall sem les inn skrá, leitar að netföngum og prentar niðurstöður.
    :return: None
    """
    args = parse_arguments()

    # Athuga hvort uppgefin skrá sé til
    if not os.path.isfile(args.file):
        print(f"Skráin {args.file} er ekki til.")
        return

    # Lesa texta úr skránni
    text = lesa_skra(args.file)

    # Leita af netföngum með óútfærðri reglulegri segð
    netfong_listi = finna_netfong(text)
    prenta_nidurstodur(netfong_listi)


if __name__ == "__main__":
    main()


