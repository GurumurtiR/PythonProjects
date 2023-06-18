# NUMBER GUESSING GAME

secret_number = 9
guess_count = 0

while guess_count < 4:
    guess = int(input('guess:'))
    guess_count = guess_count + 1

    if guess == secret_number:
        print(('you won!'))
        break
    else:
        print("sorry you guessed all wrong")
