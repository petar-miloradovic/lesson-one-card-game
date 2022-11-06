from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard


class CartaPesca2Carte(ColoredCard):
    def __init__(self, colore):
        self.colore = colore
        super().__init__(colore, CardProperty.PLUS_TWO)

    def __str__(self):
        return "(t: %s, p: %s, c : %s)" % (self.type, self.type_property, self.colore)