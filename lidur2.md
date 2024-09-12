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

Les bæði há- og lágstafi, tölustafi, punkt, undirstrik, %, og mínus. Seinasti plúsinn fyrir utan hornklofann segir að það sem er inní hornklofanum þarf að koma allavega einu sinni fram, má koma oftar. Að lokum kemur @ eftir notandanafninu. 

[a-zA-Z0-9-]+\.
Þetta skilgreinir lénsheitið á undan punktinum (t.d. hi eða new-world). Leyfilegt er að hafa há- og lágstafi, tölustafi og bandstrik. Aftur þýðir + merkið að innan hornklofans geti komið einu sinni eða oftar fram. Að lokum þarf backslash að vera á undan punkti svo punkturinn þýði ekki hvaða staf sem er heldur bókstaflega punkt.


[a-zA-Z]{2,6}
Þetta tryggir að lénsheitið (t.d. .is, .us) sé á milli 2 og 6 stafa langt. Ólöglegt ef það er lengra. 

(?:\.[a-zA-Z]{2,6})? 
Leyfir valfrjálsan annan punkt með lénsheita-viðbót að lengd 2 til 6 stafa. Það gerir ráð fyrir netföngum með tveimur lénsheitum líkt og „edu.com“.
Spurningarmerkið á eftir hópnum þýðir að það þurfi ekki að koma fram. 










