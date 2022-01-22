# Määrittelydokumentti

Sovellus tulee vertailemaan IDA*:n ja Dijkstran algoritmien suorituskykyä ja tehokkuutta navigoidessa katuosoitteiden välillä autoliikenteessä. Tulen hyödyntämään moelemmissa algoritmeissa Pythonin omaa heap-tietorakennetta.

Valitsin Dijkstran ja IDA*:n, koska tunsin jo entuudestaan Dijkstran ja se on suhteellisen simppeli, mutta IDA* vaikuttaa monimutkaisemmalta ja on minulle uusi. Molemmat pyrkivät kuitenkin samaan lopputulokseen. Aikavaativuusoletuksena on O(n+m log m).

Kartat lataan [OpenStreetMap](https://www.openstreetmap.org/)-palvelusta. Luon oman tulkin, joka lukee karttadataa ja muuttaa tiet verkoiksi. Sovellus vastaanottaa lähtöosoitteen ja halutun päätösosoitteen.
 
Käytän projektissa Pythonia. Hallitsen pääasiassa vain Pythonia. Opinto-ohjelmani on Tietojenkäsittelytieteen kandidaatti.
Projektin kielenä tulee toimimaan suomi. Koodi, dokumentaatio ym. tulee kaikki olemaan suomeksi.

## Lähteet

- https://www.openstreetmap.org/
- https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
- https://en.wikipedia.org/wiki/Iterative_deepening_A*
- http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
