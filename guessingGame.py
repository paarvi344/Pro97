chances = 5

introString = input("Guess a number between 1 and 9: ")
print(introString)

while chances < 5 :
    if guess == number :
        print("Congrats you won!!")
        break
    if not chances < 5:
        print("You lose, the number is ", number)
