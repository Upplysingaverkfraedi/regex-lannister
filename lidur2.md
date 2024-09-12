# Liður 2
í þessum lið átti að útfæra eina reglulega segð í Python sem gat fundið öll eftirfarandi lögleg netföng úr textaskránni email.txt 
* Lögleg email: helgaingim@hi.is, hei2@hi.is, john.smith@new-world.us, python101@regex101.edu.com og john.smith@new-world
* Ólögleg email: @noaddress.com, plainaddress, of@langt.domainnafn, jane.doe@@hi.is, username@.com, email@domain..com

### Lausn

Eftirfarandi regluleg segð má nota til þess að lesa lögleg email: 
r^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,6})?$. 

##### Nánari útskýring: 

^ merkir byrjun strengs og $ enda strings. 

[a-zA-Z0-9._%+-]+@

Fyrsti hornklofinn táknar notandanafn emails sem má bæði hafa há- og lágstafi, tölustafi, punkt, undirstrik, %, og mínus. Plúsinn fyrir utan hornklofann segir að það sem er inní hornklofanum má koma einu sinni eða oftar fram. Að lokum kemur @ eftir notandanafninu. Líkt og helgaingim@ og hei2@

[a-zA-Z0-9-]+\.
Næsti hornklofi skilgreinir lénið þ.e.a.s. hi eða new-world sem dæmi má nefna. Leyfilegt er að hafa há- og lágstafi, tölustafi og bandstrik. Plúsmerkið fyrir aftan hornklofann þýðir það sama og áður, allt innan hornklofans kemur fram einu sinni eða oftar. Að lokum er backslash og punktur sem merkir bókstaflega punkt en ekki hvaða staf sem er þar sem \ kemur á undan punkti. 

[a-zA-Z]{2,6}
Les rótarlénið (t.d. .is, .us) sem má vera bókstafir (í há- og lágstöfum) og 2 og 6 stafa langt. 

(?:\.[a-zA-Z]{2,6})? 
Gerir ráð fyrir netföngum með undirléni þ.e.a.s. tveimur lénsheitum líkt og „edu.com“ að lengd 2 til 6 stafa. 
Spurningarmerkið á eftir hópnum þýðir að það er valfrjálst, þ.e. þarf ekki að hafa undirlén. 










