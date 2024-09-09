# Svar

Skrifið tvær reglulegar segðir til að finna kennitölur einstaklinga og fyrirtækja í texta.

# Lausn

Eftirfarandi reglulega segð má nota til þess að finna kennitölu einstaklings:

    \b[0-3]\d{6}-\d{4}\b

Þessi segð tekur fram 10 stafa tölur þar sem að fyrsta talan er á bilinu 0-3. Ástæðan fyrir því er sú að fyrstu tveir stafir kennitölu er fæðingardagur einstaklings og fyrri tala fæðingardaga getur aldrei verið hærri en 3.

Til þess að finna kennitölur fyrirtækja í texta, má nota svipaðan en aðeins umritaða reglulega segð:

    \b[4-7]\d{6}-\d{4}\b

Líkt og fyrri segð, þá finnur hún tölu með 10 tölustöfum, en nú er fyrsti stafurinn á bilinu 4-7. Ástæðan fyrir því er að líkt og með kennitölu einstaklings byggjast fyrstu tveir tölustafirnir á "fæðingu" fyrirtækisins (fyrsti alltaf á bilinu 1-3), en þegar um fyrirtæki að ræða, þá er tölunni 4 alltaf bætt við fyrsta stafinn. Því færist bilið í 4-7.