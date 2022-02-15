from Cards import Deck

hand = []
menuInput = ""

while (menuInput != "0"):
    Deck.__init__()
    menuInput = input("Main Menu:\n\n"
            "1..................High card, low card\n"
            "2..................Texas Holdem\n"
            "3..................Draw cards\n"
            "0..................Quit\n"
            "Pick a game: ")
    print("----------------------------------------------------------------")

    #High card, low card game
    if(menuInput == "1"):
        #Grabbing cards from deck
        hand = Deck.draw_card(1, True)
        bot_draw = Deck.draw_card(1, True)
        
        try:
            #Specifying the card face and assigning it a value
            print("\nPlayer card: {}\nOpponents card: {}".format(hand[0][1], bot_draw[0][1]))
            player_card = Deck.check_face(hand[0][1])
            bot_card = Deck.check_face(bot_draw[0][1])

            #Rules of the game
            if(int(player_card) > int(bot_card)):
                print("You win!\n")
            elif(int(player_card)==(int(bot_card))):
                print("Draw!\n")
            else: print("You lost!\n")

        except(ValueError): print("Error!")
        print("----------------------------------------------------------------")

    #Texas Holdem
    elif(menuInput == "2"):
        table_cards = []
        bot = []

        #Dealing cards to players
        hand = Deck.draw_card(2, True)

        #Dealing cards to bots
        try_bool = False
        while try_bool == False:
            try:
                j = int(input("\nHow many bots would you like to play against: "))
                i = 0
                if(j<=21) and (j >= 0):
                    while i < j:
                        bot.append(Deck.draw_card(2, True))
                        i += 1
                    try_bool = True
            except ValueError:
                print("Not a valid input\n")

        #Deal the flop
        table_cards = Deck.draw_card(5, True)
        print("\nThe dealer has dealt the table cards:")
        for card in table_cards:
            print(card)
        
        #Show hands
        print("\nPlayers hand: ", hand)
        i = 1
        for bot_hand in bot:
            print("\nBot {}: ".format(i), bot_hand)
            i += 1
        print("----------------------------------------------------------------")

    #Draw cards based on user input
    elif(menuInput == "3"):
        hand = Deck.draw_card(0, False)
        print(hand, "\n")

        print("----------------------------------------------------------------")

    #Exit program
    elif(menuInput == "0"): break