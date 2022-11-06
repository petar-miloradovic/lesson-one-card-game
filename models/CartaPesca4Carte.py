from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard


class CartaPesca2Carte(ColoredCard):
    def __init__(self):
        super().__init__(CardProperty.PLUS_FOUR)

    def __str__(self):
        return "(t: %s, p: %s)" % (self.type, self.type_property)