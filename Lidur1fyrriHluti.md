# Liður 1

Skrifið tvær reglulegar segðir til að finna kennitölur einstaklinga og fyrirtækja í texta.

# Lausn

Eftirfarandi reglulega segð má nota til þess að finna kennitölu einstaklings:

    \b(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])(\d{2})-(\d{2})(\d{1})([89]|0)

Þessi segð tekur fram 10 stafa tölur þar sem að fyrsta talan er á bilinu 0-3. Ástæðan fyrir því er sú að fyrstu tveir stafir kennitölu er fæðingardagur einstaklings og fyrri tala fæðingardaga getur aldrei verið hærri en 3. Síðan út frá fyrstu tölunni er þeirri næstu skipt í tilvik, tilvik 0 þá getur önnur talan verið á bilinu 1-9, tilvik 1 og 2 þá getur hún verið á bilinu 0-9, tilvik 3 þá er hún annaðhvort 0 eða 1. Næstu tvær tölur eru ákvarðaðar af fæðingarmánuði einstaklings og líkt og með fæðingardeginum þá er skipt í tvö tilvik þar sem fyrri talan getur verið 0 eða 1. Í tilviki 0 getur hún verið á bilinu 0-9 en í tilviki 1 getur hún bara verið 0-2. Næstu tveir stafir kennitölunnar eru seinustu tveir tölustafir fæðingarárs. Þær tvær tölur geta verið hvaða tala sem er, því er notað d{2}. Næstu 3 tölur geta einnig verið hvaða tölur sem er, næstu tvær eru svokallaðar vartölur og talan á eftir því er reiknað af fyrri tölunum með Modulus 11 (á bilinu 0-9). Lokatalan er svo ákvörðuð af fæðingaröld einstaklings og getur hún einungis verið 8, 9 eða 0.

Til þess að finna kennitölur fyrirtækja í texta, má nota svipaðan en aðeins umritaða reglulega segð:

    \b(4|5|6|7)([0-9])(0[1-9]|1[0-2])(\d{2})-(\d{2})(\d{1})([89]|0)\b

Segð til þess að finna kennitölu fyrirtækis er uppbyggð nákvæmlega eins og fyrir einstaklings þar sem reglur um þeirra kennitölu er nákvæmlega eins. Þó er ein breyting, alltaf er bætt við 4 við fyrsta tölustaf í kennitölunni, því er eina breytingin að bilið fyrir fyrstu töluna fer úr 0-3 í 4-7.