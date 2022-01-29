# Viikkoraportti 2
Aloitin tämän viikon vaihtamalla aiheeni, sillä openstreetmapsista karttadatan muuttaminen oikeaan muotoon olisi tarvinnut aivan likkaa työtä. Tämän vuoksi aiheenani on nyt Dijkstran ja JPS:n vertailu keskenään käyttäen [MovingAiLabsin](https://www.movingai.com/benchmarks/) karttoja. Tarkalleen käytän pelin Warcraft 3 karttoja.

Tällä viikolla olen päässyt jo hiukan vauhtiin. Olen toteuttanut visualisoinnin Pygame-kirjastolla, joka myös mahdollistaa sen, että reitinhakua varten halutut koordinaatit voidaan valita hiirellä, eikä niitä tarvitse kirjoittaa. (Tämä ominaisuus on jokseenkin buginen kyllä vielä, jos klikkaa "ruudun" ulkopuolelta ohjelma kaatuu). Toistaiseksi vain Dijkstran algoritmin toiminallisuus on osittain tehty. Ohjelma tallentaa jokaisen solmun, jossa algoritmi käy, eikä ollenkaan lyhyintä reittiä vielä. Loin myös pari testiä Dijkstran algoritmille testattavaksi. Mielestäni ei ole hirveän mielekästä testata visualisointia ja en ole oikein varma miten se kuuluisi edes toteuttaa, joten pitäydyn vain sovelluslogiikan testaamisessa. Loin myös suurimmalle osalle metodeista ja luokista dokumentaatiot docstring-tyylisesti.

Ohjelman virtuaaliympäristö tulee asentaa ennen ohjelman ajamista. Tämän vuoksi juurihakemistossa komentoriviltä tulee ajaa seuraava komento:

> poetry install

Ohjelmaa saa testattua käynnistämällä sen ajamalla juurihakemistossa

> poetry run invoke start

Vaihtoehtoisesti myös ohjelman voi suoraan ajaa src-hakemistosta:

> python3 main.py

ja tällaisen ikkunan pitäisi avautua:
![Sovellusikkuna](/documentation/ikkuna.png)
Valitse aloituspiste klikkaamalla vasemmasta "ruudusta" jotain valkoista tai tummansinistä pikseliä (nämä ovat pisteitä, joita pitkin voit kulkea). Tämän jälkeen toista lopetuspisteelle ja algoritmi tekee työnsä, jonka jälkeen algoritmin käymät pikselit alkavat piirtyä näytölle. Voit valita uudet koordinaatit vasta, kun vanha on piirtynyt loppuun asti. Kun suljet ohjelman, komentoriville päivittyy lopuksi reittien alku- ja loppukoordinaatit sekä minimiaskelien määrä päästäkseen loppupisteeseen.

Ensi viikolla aion tehdä runsaasti lisää testejä, parannella visualisointia ja luoda tai ainakin pyrkiä luomaan valmis versio JPS-algoritmista. Lisään myös github-repoon testikattavuusraportin codecovin avulla.
Ajatuksena oli, että näytölle piirtyy vierekkäin Dijkstran ja JPS:n visualisointi, jotka pyörivät sitten rinta rinnan. Testit pääsee ajamaan komentoriviltä juurihakemistosta:
    > poetry run invoke test
Koodin siisteyden tarkastelun pylint-kirjaston avulla saa vuorostaan ajamalla juurihakemistossa:
    > poetry run invoke lint
Aikaa olen käyttänyt tällä viikolla 15 tuntia.