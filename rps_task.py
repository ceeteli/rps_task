import random


result_list = ['rock', 'paper', 'scissors']
user = input('Enter your game choice here: ').lower()

if user in result_list:
    print('User chose {}'.format(user))
    computer = random.choice(result_list)
    print('Computer chose {}'.format(computer))
    
    user_index = result_list.index(user)
    computer_index = result_list.index(computer)

    if user_index == 0 and computer_index == 2:
        print('User wins!')
    elif user_index > computer_index:
        print('User wins!')
    elif user_index < computer_index:
        print('Computer wins')
    elif user_index == computer_index:
        print('It\'s a draw!')

        while user_index == computer_index:
            user = input('Enter your game choice here: ').lower()

            if user in result_list:
                print('User chose {}'.format(user))
            computer = random.choice(result_list)
            print('Computer chose {}'.format(computer))

            user_index = result_list.index(user)
            computer_index = result_list.index(computer)

            if user_index == 0 and computer_index == 2:
                print('User wins!')
            elif user_index > computer_index:
                print('User wins!')
            elif user_index < computer_index:
                print('Computer wins')            
else:
    print('Wrong choice')
