class Reader:
    """Luokka, jonka vastuulla on lukea .map-päätteisten tiedostojen dataa
    ja muuttaa se listaan matriisiesityksenä muulle ohjelmalle käytettäväksi.

    attr:
        path (str): string-muuttuja, missä on halutun kartan tiedostosijainti.
    """

    def __init__(self, path):
        """Metodi toteutetaan oliota luodessa.
        Luo oliolle oman muuttujan mihin tallentaa tiedostosijainnin.

        args:
            path (str): string-muuttuja, missä on halutun kartan tiedostosijainti.
        """
        self.path = path

    def read(self):
        """Metodi, joka lukee kartan raakadatan .map-päätteisestä tiedostosta.

        returns:
            List: kartan raakadata muutettuna listamuotoon (jokainen tiedoston rivi on 
            yksi listan alkioista).
        raises:
            SystemExit: viestillä "Väärä tiedostonimi tai -sijainti",
                        mikäli sen nimistä tiedostoa ei löydy.
        """
        try:
            with open(self.path, "r") as file:
                return file.read().splitlines()
        except Exception:
            raise SystemExit("Väärä tiedostonimi tai -sijainti")

    def parse_data(self):
        """Metodi, joka muuttaa raakadatasta saadun listan matriisiesitykseksi.

            Ohjelman käyttämissä .map -tiedostoissa on kolmella ensimmäisellä rivillä
            jotain muuta kuin suoraan karttadataa (esim: kartan korkeus ja leveys),
            ja tämä metodi ottaa ne talteen. Metodi kutsuu ensin read-metodia,
            joka palauttaa tälle raakadatan. Tämän jälkeen metodi muuttaa raakadatan
            matriisiesityksenä toimivaan listaan.

        returns:
            height (int): kartan korkeus pikseleinä.
            width (int): kartan leveys pikseleinä.
            self.data (List): kartan data matriisiesityksenä.
        """
        self.data = self.read()
        self.data.pop(0)
        height = int(self.data.pop(0).split(" ")[1]) + 50
        width = int(self.data.pop(0).split(" ")[1]) * 2
        self.data.pop(0)
        temp = []
        for y in range(len(self.data)):
            temp.append(list(self.data[y]))
        self.data = temp

        return height, width, self.data
