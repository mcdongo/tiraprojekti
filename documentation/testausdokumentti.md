# Testausdokumentti
[![codecov](https://codecov.io/gh/mcdongo/tiraprojekti/branch/main/graph/badge.svg?token=GQKHKG6PZ4)](https://codecov.io/gh/mcdongo/tiraprojekti)

Testikattavuus on nähtävillä klikkaamalla ylläolevaa badgea. Testejä on luotu vain algoritmien toiminnallisuudelle, koska ei ole millään tavalla järkevää eikä mieleäkästä testata käyttöliittymää ja visualisointia. Testit on tehty unittestillä ja ne löytyy src/tests/ -hakemistosta. Loin pienen esimerkkikartan, jota testit käyttävät. Testit tarkistavat antaako algoritmi oikeat vastaukset oikeilla syötteillä (testikartta on hyvin pieni sen takia, että testit voi luoda helposti, koska ei tarvitse itse alkaa miettimään hirveämmin millaisia polkuja algoritmin tulisi kulkea ja miten monella askeleella). Testejä voi käydä itse tarkastelemassa esimerkiksi dijkstra_test.py -tiedostosta.

Testit pääsee ajamaan juurihakemistosta seuraavalla komennolla:

> poetry run invoke test

![coverage-report](/documentation/coverage_report.png)