from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard


class CartaCambioGiro(ColoredCard):
    def __init__(self, colore):
        self.colore = colore
        super().__init__(colore, CardProperty.CHANGE_LAP)

    def __str__(self):
        return "(t: %s, p: %s, c : %s)" % (self.type, self.type_property, self.colore)