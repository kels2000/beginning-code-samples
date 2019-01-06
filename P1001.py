#Kelsi Fulton
#P1001
#This is my code to shuffle a deck of cards

#import random to use randrange for deck
import random

#define shuffle function
def shuffle(deck, numShuffles):
    #initialize i for loop
    i = 1
    #get length of deck for randrange
    deckLength = len(deck)
    #goes through loop specified # of times
    while i <= numShuffles:
        #assigns index number to card
        card1 = random.randrange(deckLength) 
        #assigns index number to card
        card2 = random.randrange(deckLength)
        
        #if they are the same, change the index for a card
        while card1==card2:
            card2 = random.randrange(deckLength)
        #sets j equal to the placement of card 1    
        j = deck[card1]
        #sets card 1 equal to the placement of card 2
        deck[card1] = deck[card2]
        #sets card 2 equal to j (the placement of card 1)
        deck[card2] = j
        #iterate i 
        i += 1
    
def main():
    #all cards in a deck
    cards = [ "1D", "1S", "1C", "1H",
              "2D", "2S", "2C", "2H",
            "3D", "3S", "3C", "3H",
            "4D", "4S", "4C", "4H",
               "5D", "5S", "5C", "5H",
            "6D", "6S", "6C", "6H",
            "7D", "7S", "7C", "7H",
            "8D", "8S", "8C", "8H",
            "9D", "9S", "9C", "9H",
            "10D", "10S", "10C", "10H",
            "JD", "JS", "JC", "JH",
            "QD", "QS", "QC", "QH",
            "KD", "KS", "KC", "KH" ]
    
    #prints deck of cards
    print(cards)
    #asks for how many times to shuffle
    numShuffles = int(input('How many times do you want to shuffle the deck? '))
    #calls shuffle function
    shuffle(cards, numShuffles)
    #prints shuffled deck
    print(cards)

main()