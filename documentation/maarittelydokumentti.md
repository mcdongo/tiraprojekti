# Määrittelydokumentti

Sovellus tulee vertailemaan Dijkstran ja JPS -algoritmien suorituskykyä ja tehokkuutta navigoidessa pikselikartoissa koordinaateista toiseen.

Valitsin Dijkstran ja JPS, koska tunsin jo entuudestaan Dijkstran ja se on suhteellisen simppeli, alkuperäinen ajatukseni tälle projektille (navigointisovellus autoliikenteessä) osoittautui liian työlääksi vaihdoin projektin aiheen ja toisen vertailtavan algoritmin IDA*:stä JPS:n. Molemmat pyrkivät kuitenkin samaan lopputulokseen. Aikavaativuusoletuksena on O(n+m log m).

Kartat lataan [MovingAiLabsin](https://www.movingai.com/benchmarks/)-sivulta. Ohjelmassa on tulkki, joka lukee karttadataa ja sen sopivaksi matriisiestiykseksi. Sovellus vastaanottaa lähtökoordinaatit ja loppukoordinaatit.
 
Käytän projektissa Pythonia. Hallitsen pääasiassa vain Pythonia. Opinto-ohjelmani on Tietojenkäsittelytieteen kandidaatti.
Projektin kielenä tulee toimimaan suomi. Koodi, dokumentaatio ym. tulee kaikki olemaan suomeksi.

