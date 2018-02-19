class Card(object):
    
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.isFace(self.value)
    
    def getValue(self):
        return self.value
    
    def getSuit(self):
        return self.suit
    
    def __str__(self):
        return "{} of {}'s".format(self.value, self.suit)
        
    def isFace(self, value):
        self.card = value
        if self.card == 1 or self.card > 10:
            if self.card == 1:
                self.value = "Ace"
            elif self.card == 11:
                self.value = "Jack"
            elif self.card == 12:
                self.value = "Queen"
            elif self.card == 13:
                self.value = "King"
        return self.value