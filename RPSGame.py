# rock, paper, scissors game

import sys
import random

win = 0
loss = 0
tie = 0

print('Welcome to the Rock, Paper, Scissors Game!')


# paper beats rock
# rock beats scissors
# scissors beats rock

while True:
    current_scores = print(str(win) + ' Wins ' +
                           str(loss) + ' Losses ' + str(tie) + ' Ties')
    while True:
        game_list = ['r', 'p', 's']
        # randomly generates computer's choice from the game list
        computer_choice = random.choice(game_list)
        user_input = input(
            str('Enter your move: (r)ock (p)aper (s)cissors or (q)uit game: '))
        if user_input == 'q':
            print('awe, see you next time :(')
            sys.exit()  # quits the game
        elif user_input == 'r' or user_input == 's' or user_input == 'p':
            break  # break out of the user_input loop
        print('Please only type one of r, p, s, or q')

    # player's choice
    if user_input == 'r':
        print('🗿 Rock versus...')
    elif user_input == 's':
        print('✂️ Scissors versus...')
    elif user_input == 'p':
        print('📄 Paper versus...')

    # computer choice
    if computer_choice == 'r':
        print('Rock 🗿')
    elif computer_choice == 's':
        print('Scissors ✂️')
    elif computer_choice == 'p':
        print('📄 Paper')

    if user_input == 'r' and computer_choice == 'p':
        print('you lose!')
        loss += 1
        print('paper beats ')
        print(current_scores)

    elif user_input == 'r' and computer_choice == 's':
        print('you win!')
        print('')
        win += 1
        print(current_scores)

    elif user_input == 'p' and computer_choice == 's':
        print('you lose!')
        loss += 1
        print(current_scores)

    elif user_input == 'p' and computer_choice == 'r':
        print('you win!')
        win += 1
        print(current_scores)

    elif user_input == 's' and computer_choice == 'r':
        print('you lose!')
        loss += 1
        print(current_scores)

    elif user_input == 's' and computer_choice == 'p':
        print('you win!')
        win += 1
        print(current_scores)

    elif user_input == computer_choice:
        print('It''s a tie!')
        tie += 1
        print(current_scores)
