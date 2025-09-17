secret_value=49
while True:
    user_input=int(input("Guess the number:"))
    if user_input==secret_value:
        print("Correct! You win !")
        break
    elif user_input>secret_value:
        print("Too high,try again")
    else:
        print("Too low,try again")