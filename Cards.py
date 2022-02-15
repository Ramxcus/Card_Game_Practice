import random as rand
deck = []

class Deck:
    def __init__():
        shape = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        for suit in shape:
            for face in value:
                deck.append([suit, face])
        return deck

    #Drawing cards
    def draw_card(size, bool):
        hand = []

        if size >= 1:
            i = 1
            while i <= size:
                i += 1
                j = rand.randint(0, len(deck))
                if j == 0:
                    card = deck[j]
                else:
                    card = deck[j-1]
                deck.remove(card)
                hand.append(card)
            return hand
        
        while bool == False:
            try:
                draw = int(input("\nHow many cards do you want to draw: "))
                i = 1
                while i <= draw:
                    if (draw <= 52):
                        if (draw >= 1):
                            j = rand.randint(0, len(deck))
                            card = deck[j-1]
                            deck.remove(card)
                            hand.append(card)
                            i += 1
                            bool = True
                    elif (draw > 52): 
                        break
            except ValueError:
                print("Not a valid input\n")

        return hand

    #Convert face cards to numerical value
    def check_face(card):
        if(card == "Ace"):
            return '14'
        if(card == "King"):
            return '13'
        if(card == "Queen"):
            return '12'
        if(card == "Jack"):
            return '11'
        else:
            return card