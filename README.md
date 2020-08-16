# Games_of_Chance
Coin flip, cho han, card picking and roulette implementation.

## Tutorial for each game
* __coin_flip(guess, bet_amount) :__ Simple rand int algorithm. Result is either 1 or 2. Guess can be Head or Tails, bet_amount is an integer value. If you guessed right you earn bet_amount, otherwise1 you loose bet_amount.
* __cho_han(guess, bet_amount) :__ Two rand int generation. Checks if the sum of these two numbers is even or odd. Guess can be Even or Odd, bet_amount is an integer value. If you have guessed right you earn bet_amount, otherwise you loose bet_amount.
* __card_pick(bet_amount) :__ Two players pick cards. If the value of your card is bigger than the enemy you earn bet_amount, otherwise you loose bet_amount. If values of the cards are equal you won't loose or earn anything. 
* __roulette_game(guess, bet) :__ You can not bet a negative value or any amount that exceeds your money. Roulette rules are applied. Guess can be either string or integer. 
  * Double zero ("00") payout gives bet * 35. (__Example:__ roulette_game(00, 10) gives 350)
  * Zero ("0") payout gives bet * 35. (__Example:__ roulette_game(0, 10) gives 350)
  * Straight up payout also gives bet * 35. (__Example:__ roulette_game(15, 20) gives 750)
  * Other wins (even win, odd win) gives bet.
  * You can't loose more than your bet.