from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard


class CartaNumero(ColoredCard):
    def __init__(self, numero, colore):
        self.numero = numero
        self.colore = colore
        super().__init__(colore, CardProperty.NUMBER)

    def __str__(self):
        return "(t: %s, p: %s, c : %s, n: %d )" % (self.type, self.type_property, self.colore, self.numero)