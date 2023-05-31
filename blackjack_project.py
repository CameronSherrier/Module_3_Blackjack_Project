import random

deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52]
dealer = []
player = []
x = []
y = []
z = []

class Blackjack():

    def __init__(self):
        self = self

    def shuffleCards(self):
        print("Shuffling cards...")
        random.shuffle(deck_dict)
        print("The cards have been shuffled.")
    
    def dealCards(self):
        print("We will now deal out the cards")
        z = random.randint(1, 13)
        x.append(z)
        z = random.randint(1, 13)
        x.append(z)
        z = random.randint(1, 13)
        y.append(z)
        z = random.randint(1, 13)
        y.append(z)

    def giveCardsToPlayers(self):
        dealer.extend(x)
        player.extend(y)

    def hitForPlayer(self):
        z = []
        z = random.randint(1, 13)
        player.append(z)
        if sum(player) > 21: 
            print("bust!")
        else:
            pass
    
    def hitForDealer(self):
        z = []
        z = random.randint(1, 13)
        dealer.append(z)
        if sum(dealer) > 21: 
            print("bust!")
        else:
            pass

my_blackjack = Blackjack()

def run():
    print("Let's begin!")
    my_blackjack.dealCards()
    my_blackjack.giveCardsToPlayers()
    print(f'Dealer = {dealer[0]}')
    print(f'Player = {player}')
    
    flag = True
    while flag:
        
        if sum(player) == 21:
            print("Player has Blackjack!")
            print("You win!")
            flag = False

        response = input("What would you like to do? [Hit, Stay or View] ")

        if sum(player) > 21:
            print("Player bust!")
            flag = False
        elif response.lower() == 'hit':
            my_blackjack.hitForPlayer()
            print(f'You have {player}.')
            if sum(player) > 21:
                print("Player bust!")
                flag = False
        elif response.lower() == 'stay':
            print(f'The dealer has {dealer}.')
            print(f'You have {player}.')
            flag = False
        elif response.lower() == 'view':
            print(dealer[0])
            print(player)
        else:
            print("Not a valid input. Please try again.")
    
    second_flag = True
    while second_flag:

        print("It is now the dealer's turn.")
        if sum(dealer) < 21:
            my_blackjack.hitForDealer()
        elif sum(dealer) > 21:
            print("Dealer bust!")
        
        second_flag = False
    
    if sum(player) > sum(dealer) and sum(player) <= 21:
        print(player)
        print(dealer)
        print("you win!")
    elif sum(player) < sum(dealer) and sum(player) <= 21:
        print(player)
        print(dealer)
        print("You lose!")
    elif sum(player) > sum(dealer) and sum(player) > 21:
        print(player)
        print(dealer)
        print("You lose!")
    elif sum(player) < sum(dealer) and sum(player) > 21:
        print(player)
        print(dealer)
        print("You lose!")
    elif sum(player) < sum(dealer) and sum(dealer) <= 21:
        print(player)
        print(dealer)
        print("You lose!")
    elif sum(player) < sum(dealer) and sum(dealer) > 21:
        print(player)
        print(dealer)
        print("You win!")

run()
    
