import random
difficulties = None
score = 0
tries = 0

def initialize_game(level):
    random_integer = random.randint(1,100)
    print(f'Random integer value is {random_integer}')
    print(f'You have initialize the {'easy' if level == 0 else "hard"} level')
    if(level == 0):
        tries = 10
        print('Easy Level')
    else:
        tries = 5
        print('Hard Level')
    try:
        while(tries != 0):
            print('Enter the random value you think is correct.')
            user_prediction = input()
            if(random_integer == int(user_prediction)):
                print('Wow you made it.')
                score = 1
                break
                
            else:
                print('Sorry you made the wrong decision')
                tries -= 1
            
    except ValueError:
        print('Invalid Input. Please input the number')
      


print(f'You have chosen the difficulties of {difficulties}')
print('This is simple number guessing game made using python.')


while(difficulties !=0 or difficulties != 1):
    print(f'{difficulties}')
    print('In order to start, enter the number 0 or 1, \n 0 - Easy Level \n 1 - Hard Level')
    user_input = input()
    try:
        difficulties=int(user_input)
        if (int(difficulties) == 0 or int(difficulties) == 1):
            print(f'{difficulties}')
            initialize_game(difficulties)
            break
        else:
            print('Your Entered the wrong value')
    except ValueError:
        print('Invalid Input. Please enter a number.')
       



# initialize_game()
