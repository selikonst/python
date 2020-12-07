class Card:
    values = [None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    suits = ["Diamonds","Hearts","Spades","Clubs"]
    def __init__(self,v,s):
#        print("A card created. ")
        self.value = v
        self.suit = s
    def __repr__(self):
        return self.values[self.value] +" of " +self.suits[self.suit]
    def __lt__(self,other):
        if self.value < other.value:
            return True
        elif self.value == other.value:
            if self.suit < other.suit:
                return True
            else:
                return False
        else:
            return False
    def __gt__(self,other):
        if self.value > other.value:
            return True
        elif self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False
        else:
            return False
#card = Card(2,2)
#print(card)

import random
class Deck:
    def __init__(self):
#        print("A deck created. ")
        self.cards = []
        for i in range(2,15):
            for j in range(0,4):
                self.cards.append(Card(i,j))
        random.shuffle(self.cards)
    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
#deck = Deck()
#print(deck.cards)

class Player:
    def __init__(self,name):
        print("A player created. ")
        self.name = name
        self.wins = 0

class Game:
    def __init__(self):
        print("A game created. ")
        self.player1 = Player(input("Enter the first player name: "))
        self.player2 = Player(input("Enter the second player name: "))
        self.deck = Deck()
    def play_game(self):
        print("A game started. ")
        while len(self.deck.cards) >=49:
            reply = input("Etner \"X\" to exit or \"Enter\" to start: ")
            if  reply == "X":
                break
#            print(self.player1.name)
#            print(self.player2.name)
#            print(self.deck.remove_card())
#            print(self.deck.remove_card())
            player1card = self.deck.remove_card()
            player2card = self.deck.remove_card()
            print(self.player1.name," has ",player1card)
            print(self.player2.name," has ",player2card)
            if player1card > player2card:
                self.player1.wins += 1
                print(self.player1.name,"win! ")
            else:
                self.player2.wins += 1
                print(self.player2.name,"win! ")
            print(self.player1.name," has ",self.player1.wins," wins")
            print(self.player2.name," has ",self.player2.wins," wins")
        print("\n")
        print("Game over. {} win! ".format(self.winner(self.player1,self.player2)))
    def winner(self,player1,player2):
        if self.player1.wins > self.player2.wins:
            return self.player1.name
        if self.player1.wins < self.player2.wins:
            return self.player2.name
        return "Nobody"

game = Game()
#print(game.deck.cards)
game.play_game()
