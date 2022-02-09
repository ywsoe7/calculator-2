import random

def user_choice_game(name):
    
    random_number = random.randint(1, 100)

    your_guess = int(input('Guess a whole number between 1-100: '))

    count = 1
 
    while your_guess != random_number:
        count += 1
        
        try:
            print(int(your_guess))
        except:
            your_guess = int((input("Please input a number: "))) 

        if your_guess < 1 or your_guess > 100:
            your_guess = input(f"That's not in the range, please input a number between 1-100: ")

        if your_guess > random_number:
            print(int(input(f"Sorry, your guess is too high. Please choose a number below {your_guess}: ")))
        
        elif your_guess < random_number:
            print(int(input(f"Sorry, your guess is too low. Please choose a number above {your_guess}: ")))

    if your_guess == random_number:
        if count == 1:
            print(f"WOW!!! You guessed it in just ONE try! {name}, go treat yourself to some icecream!")
        else:
            print(f"Congratulations, {name}! You have guessed the correct answer in {count} tries.") 

best_score = None
try_limit = 5
computer_guess = False

print('Hi! Welcome! What is your name?')
name = input('Type in your name: ')

print(f'Okay {name}, do you want the computer to guess your number?')
user_choice = input('Yes or No: ')

if user_choice == "Yes":
    computer_guess == True

else:
    #create a lets_play_a_game func

    user_choice_game(name)
     #call user input function
    # min_range = 1
    # max_range = 100
#user input function game below:
 #set how many tries the user gets and restart the game 


print(user_choicegame(name))
