# Viikkoraportti 5

Rehellisesti sanottuna en saanut paljon aikaan tällä viikolla. JPS:n toteuttaminen osoittautui paljon suuremmaksi ja vaikeammaksi työksi kuin osasin odottaa. Suurin osa ajasta, jonka käytin tällä viikolla projektin parissa kului JPS:n toiminnan tutkimiseen ja ymmärtämiseen. Yritin luoda algoritmia, mutta se ei ole vielä toistaiseksi onnistunut. Väitän kuitenkin nyt ymmärtäväni kunnolla miten sen kuuluisi toimia. Seuraavalla viikolla aion nostaa tuntimäärää mitä vietän työn parissa paljon, jotta saisin toimivan version toteutettua. Selvästikin aika, jonka varasin tälle viikolle ei riittänyt. 


Kaikesta huolimatta refaktoroin koodia ja tein pieniä muutoksia sovelluksen toimiviin osiin. Nyt visualisointi toimii paljon nopeammin, sillä aikaisemmin listat, joissa oli algoritmien kaikki läpikäydyt solmut sisälsi duplikaatteja, jonka vuoksi visualisointi pyöri hitaasti. Nyt algoritmien toiminnan valmistuttua olio palauttaa listan, josta on duplikaatit poistettu. Loin algorithm_base.py moduulin, joka sisältää isäntäluokan Algorithm, missä on molempien algoritmien käyttämiä metodeja ja muuttujia. Molemmissa algoritmiluokissa oli toistuvaa koodia, joten koin tarpeelliseksi muuttaa niitä niin, että ne perivät yhteisen luokan ominaisuudet. Vaihdoin Dijkstran algoritmin käyttämään myös prioriteettijonoa, minkä vuoksi Dijkstran algoritmin koodi selkeytyi huomattavasti.


Aikaa olen käyttänyt tällä viikolla 7h. En pystynyt tällä viikolla varaamaan niin paljoa aikaa projektin parissa kuin muilla viikoilla henkilökohtaisista syistä.