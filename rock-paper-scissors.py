import random

player1 = input('Select rock, paper or scissors: ').lower()
player2 = random.choice(['rock', 'paper', 'scissors']).lower()

print(f'Player 2 selected: {player2}.')

if (player1 == 'rock' and player2 == 'paper')\
        or (player1 == 'paper' and player2 == 'scissors')\
        or (player1 == 'scissors' and player2 == 'rock'):
    print('Player 2 won')
elif player1 == player2:
    print('Tie')
else:
    print('Player 1 won')