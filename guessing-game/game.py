import random

print('Hi! Welcome! What is your name?')
name = input('Type in your name: ')

random_number = random.randint(1, 100)

your_guess = int(input('Guess a whole number between 1-100: '))

try:
    print(int(your_guess))
except:
    your_guess = int((input("Please input a number: ")))

low = 0
high = 101
count = 1

while your_guess != random_number:
    count += 1
        
    if your_guess > random_number:
        high = your_guess
        try:
            your_guess = int(input(f"Sorry, your guess is too high. Please choose a number below {high}: "))
        except:
            your_guess = int((input("Please input a number: ")))

    elif your_guess < random_number:
        low = your_guess
        try:
            your_guess = int(input(f"Sorry, your guess is too low. Please choose a number above {low}: "))
        except:
            your_guess = int((input("Please input a number: ")))


if your_guess == random_number:
    if count == 1:
        print(f"WOW!!! You guessed it in just ONE try! {name}, go treat yourself to some icecream!")
    else:
        print(f"Congratulations, {name}! You have guessed the correct answer in {count} tries.")