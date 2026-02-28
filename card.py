from enum import Enum

class card_type(Enum):
    NORMAL = "Normal"
    FREEZE = "frz"
    FLIP_THREE = "flp"
    SECOND_CHANCE = "scd"
    PLUS = "Plus X"
    TIMES_TWO = "*2"
    ERROR="ERROR"


class Card:
    def __init__(self, type:card_type, value:int=0):
        self.type = type
        self.value = value 
    def to_string(self)->str:
        if self.type == card_type.NORMAL:
            return str(self.value)
        elif self.type == card_type.PLUS:
            return "+" + str(self.value)
        else:
            return self.type.value

class CardInputError(Card):
    def __init__(self, error:str):
        self.error = error
    def to_string(self)->str:
        return self.error