from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard


class CartaDivieto(ColoredCard):
    def __init__(self, colore):
        self.colore = colore
        super().__init__(colore, CardProperty.PROHIBITION)

    def __str__(self):
        return "(t: %s, p: %s, c : %s)" % (self.type, self.type_property, self.colore)