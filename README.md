# Games_of_Chance
Coin flip, cho han, card picking and roulette implementation

## Tutorial for each game
* coin_flip(guess, bet_amount) : Simple rand int algorithm. Result is either 1 or 2. Guess can be Head or Tails, bet_amount is an integer value. If you guessed right you earn bet_amount, otherwise1 you loose bet_amount.
* cho_han(guess, bet_amount) : Two rand int generation. Checks if the sum of these two numbers is even or odd. Guess can be Even or Odd, bet_amount is an integer value. If you guessed right you earn bet_amount, otherwise1 you loose bet_amount.
* card_pick(bet_amount) : Two players pick cards. If the value of your card is bigger than the enemy you earn bet_amount, otherwise you loose bet_amount. If values of the cards are equal you won't loose or earn anything. 
* roulette(guess, bet) : You can not bet a negative value or any amount that exceeds your money. Roulette rules are applied. Guess can be either string or integer. 
  Double zero ("00") payout gives bet * 35. 
