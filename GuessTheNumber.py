import random

n = random.randint(1, 100)
count = 1
guess_chances = 10
player_name = input("Hi there! What's your name? ")

print('Nice to meet you, ' + player_name + '!')

answer = input('Would you like to play a guessing game with me? ')
if answer.lower() == 'no':
    print('Alright, maybe next time. Have a great day!')
elif answer.lower() == 'yes':
    print('Alright, ' + player_name + ', let me think of a number between 1 and 100, and you have 10 chances to guess it. Let\'s get started!')
    while 1 <= guess_chances:
        num = int(eval(input("Guess the number: ")))
        if num > n:
            print('Your guess was too high. Try a lower number than ', num)
        elif num < n:
            print('Your guess was too low. Try a higher number than ', num)
        else:
            print('YOU WIN!')
            print('You guessed the number in ' + str(count) + ' attempts!')
            break
        guess_chances -= 1
        print(guess_chances, 'guesses left.')
        count += 1

    print("GAME OVER")
    print("The number was ", n)
    print('Thanks for playing! Have a wonderful day, ' + player_name + '!')

else:
    print('Sorry, I didn\'t quite understand your response. Please try again.')
