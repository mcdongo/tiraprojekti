class Level:
    """Luokka, joka pitää kirjaa mitä kartan koordinaateista ja datasta.

    attr: _level_map (List): matriisiesityksessä oleva karttadata
    """

    def __init__(self, level_map):
        """Metodi, joka toteutetaan oliota luodessa.

        args:
            level_map (List): matriisiesityksessä oleva karttadata
        """
        self._level_map = level_map

    def get_level_map(self):
        """Metodi, joka palauttaa karttadatan.

        returns:
            _level_map (List): matriisiesityksessä oleva karttadata
        """
        return self._level_map

    def get_coordinate(self, y, x):
        """Metodi, joka palauttaa tietyn koordinaatin merkin kartasta.

        args:
            y (int): koordinaatti y-akselilla
            x (int): koordinaatti x-akselilla
        returns:
            _level_map[y][x] (str): jokin merkki, mikä kuvaa siinä 
                sijainnissa olevaa asiaa
        """
        return self._level_map[y][x]

    def edit_coordinate(self, y, x, value):
        """Metodi, joka muokkaa halutuissa koordinaateissa olevaa kohtaa
            halutuksi arvoksi

        args:
            y (int): koordinaatti y-akselilla
            x (int): koordinaatti x-akselilla
            value (str): haluttu merkki, millä korvataan vanha
                (y,x)-koordinaateissa sijaitseva merkki
        """
        self._level_map[y][x] = value
