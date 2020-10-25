class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def getValue(self):
        '''Gets the value of the card'''
        try:
            return int(self.value)

        except ValueError:
            if self.value != "A":
                return 10
            else:
                return 11 #Will change to 1 if total passes 21
