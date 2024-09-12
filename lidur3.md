# Liður 3 
Í þessum lið viljum við breyta formattinu á skránni nafn_heimilisfang_simanumer.csv:

Jón Jónsson, Litla-Saurbæ, 816 Ölfusi, 555-1234
Guðrún Helgadóttir, Fiskislóð 15, 101 Reykjavík, 510-7000
Jón Oddur Guðmundsson, Úthlíð 6, 450 Patreksfirði, 897-1234

yfir í

Litla-Saurbæ	816 Ölfusi	555-1234	Jónsson, Jón
Fiskislóð 15	101 Reykjavík	510-7000	Helgadóttir, Guðrún
Úthlíð 6	450 Patreksfirði	897-1234	Guðmundsson, Jón Oddur

og í stað kommu á að vera lárétt tab (\t). 

### Lausn: 

Fundin var reglulega segð sem gat lesið hvern hóp fyrir sig; Eiginnafn og millinafn, kenninafn, heimilisfang, póstnúmer og símanúmer:  

    regex_string = r'(?m)^(.*?)\s+(\S+),\s*([^,\n]+),\s*([^,\n]+),\s*([^,\n]+)$'

##### Nánari útskýring: 
(?m): Þýðir að ^ og $ virka fyrir upphaf og endi hverrar línu. 

^ og $: Er alltaf í upphafi og enda hverrar segðar. 

(.*?): Er hópur sem tekur hvaða texta sem er í upphafi þar til það kemur bil. T.d. myndi einungis lesa Jón í Jón Jónsson. 

\s+: Bil milli nafna 

(\S+): Það passar við allt sem er ekki bil. Fangar næsta nafn eins og Jónsson eftir Jón þannig þá væri búið að lesa Jón Jónsson

,\s*: Því næst kemur komma sem aðgreinir nafn frá næsta hópi sem er heimilisfang og \s* við möguleg bil eftir kommu. 

([^,\n]+): Les heimilisfangið (eða allt sem er ekki komma eða línuskipti)

([^,\n]+): Fangar póstnúmer

Að lokum ([^,\n]+): Sem fangar símanúmer

Sem dæmi: Guðrún Helgadóttir, Fiskislóð 15, 101 Reykjavík, 510-7000
(.*?): Les "Guðrún".
(\S+): Les "Helgadóttir".
([^,\n]+): Les "Fiskislóð 15".
([^,\n]+): Les "101 Reykjavík".
([^,\n]+): Les "510-7000"

Notkun á .*? og \S+ er mun þægilegri og almennari leið til að lesa stafi í staðinn fyrir að þurfa að takmarka við aðeins bókstafi eða tölustafi með tjáningum eins og [A-Za-z] eða [0-9].

Þá var búið að flokka upplýsingarnar í 5 hópa sem hægt var að endurraða með því að fara línu eftir línu og gera nýjan streng sem endurraðaði hópunum í heimilisfang, póstnúmer, símanúmer, kenninafn og að lokum eiginnafn og millinafn (í röð) með neðantaldri for-lykku:

out_list = []
    for lina in linur:
        first_name, last_name, address, city, phone = regex.findall(lina)[0]

        line_string = f'{address}\t{city}\t{phone}\t{last_name}, {first_name}'
        out_list.append(line_string)

    return out_list

