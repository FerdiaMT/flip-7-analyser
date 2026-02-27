from enum import Enum

class card_type(Enum):
    NORMAL = "Normal"
    FREEZE = "Freeze"
    FLIP_THREE = "Flip Three"
    SECOND_CHANCE = "Second Chance"
    PLUS = "Plus X"
    TIMES_TWO = "Times Two"


class Card:
    def __init__(self, type:card_type, value:int=0):
        self.type = type
        self.value = value 
    def to_string(self)->str:
        if self.type == card_type.NORMAL:
            return str(self.value)
        elif self.type == card_type.PLUS:
            return "+ " + str(self.value)
        else:
            return self.card_type