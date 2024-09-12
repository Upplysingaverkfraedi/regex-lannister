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

^ og $: alltaf í upphafi og enda hverrar segðar. 

(.*?): Er hópur sem tekur hvaða texta sem er í upphafi þar til það kemur bil. T.d. myndi einungis lesa Jón í Jón Jónsson. 

\s+: Bil milli nafna 

(\S+): Fangar annað orð. T.d. Jón Jónsson

Því næst kemur komma sem aðgreinir nafn frá næsta hópi sem er heimilisfang og \s* við möguleg bil eftir kommu 

([^,\n]+): Tekur heimilisfangið (eða allt sem er ekki komma eða línuskipti)

,\s*: Aðgreinir næsta hóp og leyfir bil

([^,\n]+): Fangar póstnúmer og stað 

Að lokum ([^,\n]+): Sem fangar símanúmer

Sem dæmi: Guðrún Helgadóttir, Fiskislóð 15, 101 Reykjavík, 510-7000
(.*?): Fanga "Guðrún".
(\S+): Fanga "Helgadóttir".
([^,\n]+): Fanga "Fiskislóð 15".
([^,\n]+): Fanga "101 Reykjavík".
([^,\n]+): Fanga "510-7000"

Notkun á .*? og \S+ er mun þægilegri og almennari leið til að fanga stafi í staðinn fyrir að þurfa að takmarka við aðeins bókstafi eða tölustafi með tjáningum eins og [A-Za-z] eða [0-9].
Þar sem:
.: Táknar hvaða staf sem er nema línuskipti. 
Í tjáningunni .*?, passar það við hvaða staf sem er, þar á meðal bókstafi, tölustafi og sértákn.

\S+: Táknar hvaða runu af stöfum sem er sem eru ekki bil. Það passar við allt sem er ekki bil, þar með talið bókstafi, tölustafi og tákn.

Þá var hægt að endurraða hópunum með því að fara línu eftir línu og gera nýjan streng sem endurraðaði hópunum í heimilisfang, póstnúmer, símanúmer, kenninafn og að lokum eiginnafn og millinafn með neðantaldri for-lykku:

out_list = []
    for lina in linur:
        first_name, last_name, address, city, phone = regex.findall(lina)[0]

        line_string = f'{address}\t{city}\t{phone}\t{last_name}, {first_name}'
        out_list.append(line_string)

    return out_list

