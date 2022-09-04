import json

with open('me-capitals.json', 'r') as f:
    data = json.load(f)

total = len(data["cards"])

player = False
#stretch goal - created while loop to ask player to play again after game ends
while player == False:

    score = 0

    for i in data["cards"]:
        guess = input(i["q"] + " > ")
        answer = i["a"]
        #stretch goal - addressed case sensitivity with .lower() to compare guess and answer in lower case
        if guess.lower() == answer.lower():
            score += 1
            print(f"Correct! Current score: {score}/{total}")
        else:
            print("Incorrect! The correct answer was", i["a"])
            print(f"Current score: {score}/{total}")
    #stretch goal - end game message to print total score
    print(f"Thanks for playing! You scored: {score}/{total}")

    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
        player = False
    else:
        break
