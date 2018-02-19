from Deck import *
import re


class Hand(object):

    def __init__(self, deck):
        self.deck = deck
        self.deck.shuffle()
        self.hand = []
        self.dealersHand = []
        self.playerTotal = 0
        self.dealerTotal = 0

    def initialDeal(self):
        print("\nYour Hand:")
        i = 0
        while i < 2:
            card = self.deck.getDeck().pop(0)
            i += 1

            print("\t" + str(card))
            self.hand.append(str(card))
        print("total = " + str(self.getPlayerTotal()))

    def dealerHand(self):
        print("\nDealers Hand:")
        i = 0
        while i < 2:
            card = self.deck.getDeck().pop(0)
            i += 1

            self.dealersHand.append(str(card))

        print("\t" + str(self.dealersHand[0]))
        print("\tUnknown second Dealer card...")
        if self.getDealerTotal() == 21:
            print("Dealer wins, Game over")
            return

    def getPlayerTotal(self):
        i = 0
        while i < 2:
            card = str(self.hand[i])

            if re.match("2", str(card)):
                self.playerTotal += 2
            elif re.match("3", str(card)):
                self.playerTotal += 3
            elif re.match("4", str(card)):
                self.playerTotal += 4
            elif re.match("5", str(card)):
                self.playerTotal += 5
            elif re.match("6", str(card)):
                self.playerTotal += 6
            elif re.match("7", str(card)):
                self.playerTotal += 7
            elif re.match("8", str(card)):
                self.playerTotal += 8
            elif re.match("9", str(card)):
                self.playerTotal += 9
            elif re.match("10|Jack|Queen|King", str(card)):
                self.playerTotal += 10
            i += 1
        if re.match("Ace", self.hand[0]):
            choice = int(input("would you like the ace to be a 1 or an 11\n"))
            if choice == 11:
                self.playerTotal += 11
            elif choice == 1:
                self.playerTotal += 1
        if re.match("Ace", self.hand[1]):
            choice = int(input("would you like the ace to be a 1 or an 11\n"))
            if choice == 11:
                self.playerTotal += 11
            elif choice == 1:
                self.playerTotal += 1
        return self.playerTotal

    def getDealerTotal(self):
        i = 0
        while i < 2:
            card = str(self.dealersHand[i])

            if re.match("2", str(card)):
                self.dealerTotal += 2
            elif re.match("3", str(card)):
                self.dealerTotal += 3
            elif re.match("4", str(card)):
                self.dealerTotal += 4
            elif re.match("5", str(card)):
                self.dealerTotal += 5
            elif re.match("6", str(card)):
                self.dealerTotal += 6
            elif re.match("7", str(card)):
                self.dealerTotal += 7
            elif re.match("8", str(card)):
                self.dealerTotal += 8
            elif re.match("9", str(card)):
                self.dealerTotal += 9
            elif re.match("10|Jack|Queen|King", str(card)):
                self.dealerTotal += 10
            i += 1

        if re.match("Ace", self.dealersHand[0]) or re.match("Ace", self.dealersHand[1]):
            if self.dealerTotal + 11 > 21:
                choice = 1
                self.dealerTotal += choice
            elif self.dealerTotal + 11 <= 21:
                choice = 11
                self.dealerTotal += choice
        return self.dealerTotal

    def hit(self):
        choice = ""
        if self.playerTotal == 21:
            print("21! You win!!")
            return

        while self.playerTotal != 21 and choice == "yes":
            choiceHit = input("\nWould you like to hit? ['yes', 'no']\n")
            if choiceHit == "yes":
                self.hand.append(str(self.deck.getDeck().pop(0)))
                if re.match("Ace", str(self.hand[2])):
                    choice = int(input("would you like the ace to be a 1 or an 11\n"))
                    if choice == 11:
                        self.playerTotal += 11
                    elif choice == 1:
                        self.playerTotal += 1
                print("\n")
                for card in self.hand:
                    print("\t" + card)
                if re.match("2", str(self.hand[len(self.hand) - 1])):
                    self.playerTotal += 2
                elif re.match("3", str(self.hand[len(self.hand) - 1])):
                    self.playerTotal += 3
                elif re.match("4", str(self.hand[len(self.hand) - 1])):
                    self.playerTotal += 4
                elif re.match("5", str(self.hand[len(self.hand) - 1])):
                    self.playerTotal += 5
                elif re.match("6", str(self.hand[len(self.hand) - 1])):
                    self.playerTotal += 6
                elif re.match("7", str(self.hand[len(self.hand) - 1])):
                    self.playerTotal += 7
                elif re.match("8", str(self.hand[len(self.hand) - 1])):
                    self.playerTotal += 8
                elif re.match("9", str(self.hand[len(self.hand) - 1])):
                    self.playerTotal += 9
                elif re.match("10|Jack|Queen|King", str(self.hand[len(self.hand) - 1])):
                    self.playerTotal += 10
                print("total = " + str(self.playerTotal) + "\n")
                if self.playerTotal > 21:
                    print("You Busted and the house wins. :(")
                    break
                #choice = input("\nWould you like to Hit again?\n")
            elif choiceHit == "no":
                # print("\nDealers hand is...")
                # for card in self.dealersHand:
                    # print("\t" + card)
                break

    def hitDealer(self):
        self.dealersHand.append(str(self.deck.getDeck().pop(0)))
        if re.match("Ace", str(self.dealersHand[len(self.dealersHand) - 1])):
            if self.dealerTotal + 11 > 21:
                choice = 1
                self.dealerTotal += choice
            elif self.dealerTotal + 11 <= 21:
                choice = 11
                self.dealerTotal += choice
        print("\nDealers Hand:")
        for card in self.dealersHand:
            print("\t" + card)
        if re.match("2", str(self.dealersHand[len(self.dealersHand) - 1])):
            self.dealerTotal += 2
        elif re.match("3", str(self.dealersHand[len(self.dealersHand) - 1])):
            self.dealerTotal += 3
        elif re.match("4", str(self.dealersHand[len(self.dealersHand) - 1])):
            self.dealerTotal += 4
        elif re.match("5", str(self.dealersHand[len(self.dealersHand) - 1])):
            self.dealerTotal += 5
        elif re.match("6", str(self.dealersHand[len(self.dealersHand) - 1])):
            self.dealerTotal += 6
        elif re.match("7", str(self.dealersHand[len(self.dealersHand) - 1])):
            self.dealerTotal += 7
        elif re.match("8", str(self.dealersHand[len(self.dealersHand) - 1])):
            self.dealerTotal += 8
        elif re.match("9", str(self.dealersHand[len(self.dealersHand) - 1])):
            self.dealerTotal += 9
        elif re.match("10|Jack|Queen|King", str(self.dealersHand[len(self.dealersHand) - 1])):
            self.dealerTotal += 10
        print("\ntotal = " + str(self.dealerTotal))
        if self.dealerTotal > 21:
            print("Dealer Busted, player wins!")
            return

    def dealersPlay(self):
        while self.dealerTotal <= 21 and self.playerTotal > self.dealerTotal:
            self.hitDealer()
        if self.dealerTotal < self.playerTotal:
            print("Dealer looses.\nDealer's loosing hand, with a total of: " + str(self.dealerTotal))
            for card in self.dealersHand:
                print(card)
            print("\nPlayers winning hand, with a total of: " + str(self.playerTotal))
            for card in self.hand:
                print(card)
        elif self.dealerTotal > 21:
            print("Dealer Busted and Player wins\nDealer's loosing hand, with a total of: " +
                                 str(self.dealerTotal))
            for card in self.dealersHand:
                print(card)
            print("\nPlayers winning hand:")
            for card in self.hand:
                print(card)
        elif self.playerTotal == self.dealerTotal:
            print("Tie Game, no money exchanged.\nDealer's hand: ")
            for card in self.dealersHand:
                print(card)
            print("\nPlayers hand:")
            for card in self.hand:
                print(card)
        if self.dealerTotal > self.playerTotal:
            print("Dealer wins. Winning hand is:")
            for card in self.dealersHand:
                print("\t" + card)
            print("\nPlayers Loosing Hand:")
            for card in self.hand:
                print("\t" + card)

def main():
    responce = input("Would You like to play a game of Black Jack? ['yes', 'no']\n")
    while responce == "yes":
        deck = Deck()
        hand = Hand(deck)
        hand.initialDeal()
        hand.dealerHand()
        hand.hit()
        hand.dealersPlay()

main()