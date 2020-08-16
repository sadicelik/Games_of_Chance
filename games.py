import random

money = 100

#Write your game of chance functions here
def coin_flip(guess, bet_amount):
    print("Playing Coin Flip game...")
    rand_int = random.randint(1, 2)
    result = ""
    if rand_int == 1:
        result = "Heads"
    else:
        result = "Tails"
    
    print("Outcome is %s." %result)
    
    if result == guess:
        print("You have guessed %s, you won!" %guess)
        return bet_amount
    else:
        print("You have guessed %s, you lost!" %guess)
        return -bet_amount
    
def cho_han(guess, bet_amount):
    print("Playing Cho-Han game...")
    rand_int1 = random.randint(1, 6)
    rand_int2 = random.randint(1, 6)
    sum_of_nums = rand_int1 + rand_int2
    print("Outcome is %i" %sum_of_nums)
    result = ""
    
    if sum_of_nums % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
        
    if result == guess:
        print("You have guessed %s, you won!" %guess)
        return bet_amount
    else:
        print("You have guessed %s, you lost!" %guess)
        return -bet_amount
        
def card_pick(bet_amount):
    print("Playing Card Picking game...")
    player1_card = random.randint(1, 13)
    player2_card = random.randint(1, 13)
    print("Your card: %i" %player1_card)
    print("Your enemy's card: %i" %player2_card)
    
    if player1_card > player2_card:
        print("You have won!")
        return bet_amount
    elif player1_card == player2_card:
        print("It's a tie!")
        return 0
    else:
        print("You have lost!")
        return -bet_amount
                
def roulette_game(guess, bet):
#Bet can't be negative or more than your balance
    if bet < 0:
        print("Your bet must be greater than zero. Please try again.\n")
    elif bet > money:
        print("You don't have that much money. Please try again.\n")

    else:
    # Start game and store result of spin
        spin = random.randint(0,37)
        if spin == 37:
          spin = "00"
        elif spin == 0:
          spin = 0
        elif spin % 2 ==0:
          even_odd = "even"
        elif spin % 2 != 0:
          even_odd = "odd"
 
    # Check even/odd results after concluding guess was a string
        if isinstance(guess,str):
          #Even win
          if guess.lower() == "even" and even_odd == "even":
            print("The roll was a(n) " + str(spin) + " which is even.")
            print("You won " + str(bet) + " dollars!\n")
            return bet
          #Even lost
          elif guess.lower() == "even" and even_odd == "odd":
            print("The roll was a(n) " + str(spin) + " which is odd.")
            print("Better luck next time!")
            print("You lost " + str(bet) + " dollars.\n")   
            return -bet
          #Odd win
          elif guess.lower() == "odd" and even_odd == "odd":
            print("The roll was a(n) " + str(spin) + " which is odd.")
            print("You won " + str(bet) + " dollars!\n")
            return bet
          #Odd lost
          elif guess.lower() == "odd" and even_odd == "even":
            print("The roll was a(n) " + str(spin) + " which is even.")
            print("Better luck next time!")
            print("You lost " + str(bet) + " dollars.\n")   
            return -bet
          #00 won
          elif guess == "00" and spin == "00":
            print("The roll was a 00!!!")
            double_zero_payout = bet*35
            print("You won " + str(double_zero_payout) + " dollars!\n")
            return double_zero_payout
          else:
            print("You guessed a(n) " + str(guess) + " would be rolled and a(n) " + str(spin) + " was rolled")
            print("Better luck next time!")
            print("You lost " + str(bet) + " dollars.\n")  
            return -bet
    
    # Check number results
    
        elif guess == 0 and spin == 0:
          print("The roll was a 0!!!")
          zero_payout = bet*35
          print("You won " + str(zero_payout) + " dollars!\n") 
          return zero_payout  
        elif guess == spin:
          print("You guessed a(n) " + str(guess) + " would be rolled and a(n) " + str(spin) + " was rolled")
          straight_up_payout = bet*35
          print("You win " + str(straight_up_payout) + " dollars!")
          return straight_up_payout
        else:
          print("You guessed a(n) " + str(guess) + " would be rolled and a(n) " + str(spin) + " was rolled")
          print("Better luck next time!")
          print("You lost " + str(bet) + " dollars.\n")  
          return  -bet


#Call your game of chance functions here
#roulette_game(0, 10)