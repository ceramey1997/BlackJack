from Card import *
from random import shuffle

class Deck(object):

    def __init__(self):
        self.deck = []
        self.build()

    def build(self):
        for suit in ["Spade", "Club", "Heart", "Diamond"]:
            for value in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                self.deck.append(Card(value, suit))

    def showDeck(self):
        for card in self.deck:
            print(card)

    def shuffle(self):
        return shuffle(self.deck)

    def getDeck(self):
        return self.deck