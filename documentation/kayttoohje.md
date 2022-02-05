# Käyttöohjedokumentti

Ohjelman virtuaaliympäristö tulee asentaa ennen ohjelman ajamista. Tämän vuoksi juurihakemistossa komentoriviltä tulee ajaa seuraava komento:

> poetry install

Ohjelmaa saa testattua käynnistämällä sen ajamalla juurihakemistossa

> poetry run invoke start

Vaihtoehtoisesti myös ohjelman voi suoraan ajaa src-hakemistosta:

> python3 main.py

Huom! Tällöin täytyy olla virtuaaliympäristössä, johon pääsee ajamalla juurihakemistossa seuraavan komennon

> poetry shell

Avattua sovelluksen tällaisen ikkunan pitäisi avautua:
![Sovellusikkuna](/documentation/ikkuna.png)
Valitse aloituspiste klikkaamalla vasemmasta "ruudusta" jotain valkoista tai tummansinistä pikseliä (nämä ovat pisteitä, joita pitkin voit kulkea). Tämän jälkeen toista lopetuspisteelle ja algoritmi tekee työnsä, jonka jälkeen algoritmin käymät pikselit alkavat piirtyä näytölle. Voit valita uudet koordinaatit vasta, kun vanha on piirtynyt loppuun asti. Kun suljet ohjelman, komentoriville päivittyy lopuksi reittien alku- ja loppukoordinaatit sekä minimiaskelien määrä päästäkseen loppupisteeseen. Vasemmassa alareunassa on nappula, joka vaihtaa haluttua tarkastelua lyhimmän reitin ja algoritmin kokonaan käyneen polun välillä.

Testit pääsee ajamaan komentoriviltä juurihakemistosta:

> poetry run invoke test

Koodin siisteyden tarkastelun pylint-kirjaston avulla saa vuorostaan ajamalla juurihakemistossa:

> poetry run invoke lint