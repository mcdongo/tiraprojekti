# Toteutusdokumentti
Ohjelma on toteuttu Pythonilla ja visualisoinnissa käytän Pythonin Pygame-kirjastoa. Ohjelmaa ohjaa main.py-moduulissa oleva Main-olio. Olio luo kaikki tarpeelliset oliot visualisoinnille, kuten:
 - Clock, joka vastaa ajankulun käsittelystä visualisoinnissa
 - EventQueue, joka vastaa käyttäjän antamista syötteistä
 - Reader, joka vastaa datan muuttaminen tiedostosta matriisiesitykseksi
 - 2 kappaletta Level-olioita, jotka pitävät kirjaa sekä JPS- että Dijkstran algoritmien **erillisistä** karttadatoista
 - Renderer, joka vastaa siitä että Pygame-ikkunalle piirtyy ja päivittyy visualisointi 60 kertaa sekunnissa
 - Loop, joka vastaa käytännössä ohjelman pyörimisestä. Luo itselleen Dijkstra- ja JPS-oliot, jotka vastaavat algoritmien toiminnasta. Loop-olio käsittelee käyttäjän syötteet ja kutsuu Renderer-oliota päivittämään visualisointia

 ## Tila- ja aikavaativuudet
 Dijkstran algoritmin aikavaativuus on pahimmassa tapauksessa O(n²), koska ohjelmassa käytetään matriisiesityksiä mallintamaan verkkoja. 

 ## Lähteet

 - [MovingAiLabs](https://www.movingai.com/benchmarks/)
 - [Online Graph Pruning for Pathfinding on Grid Maps](http://users.cecs.anu.edu.au/~dharabor/data/papers/harabor-grastien-aaai11.pdf)
 - [Wikipedia, Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
 - [Wikipedia, A* algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
 - [Wikipedia, Jump point search](https://en.wikipedia.org/wiki/Jump_point_search)
 - [Tirakirja](https://raw.githubusercontent.com/hy-tira/tirakirja/master/tirakirja.pdf)
 - [Youtube](https://www.youtube.com/watch?v=__ZLnTwYNPk)