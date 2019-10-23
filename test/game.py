import random

str = ""

while str != "exit":
    maximum_number = int(input('Enter maximum number> '))
    computer_number = random.randint(1, maximum_number)
    number_of_attempts = int(input('Enter number of attempts> '))

    for count_of_attempts in range(0, number_of_attempts):
        user_number = int(input('Enter number> '))

        if user_number > computer_number:
            print('The number is greater than the hidden')
        elif user_number < computer_number:
            print('The number is less than the hidden')
        else:
            print('You guessed')
            break
    else:
        print('Attempts ended')

    str = input('The game is over. To exit write \"exit\" ')