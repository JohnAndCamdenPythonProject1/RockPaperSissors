#Camden Levy and John Castilloux
import random


print("Rock Paper Scissors game\nCompete against the AI and gain score ")
print("-----------------------------------------------------------------")
print("To play competitive Rock Paper Scissors, you must type Play to continue.")

input1 = input("Type play to begin ")
if input1.lower() == "Play" or "P":
    print("Game Begins")
    game = 1
else:
    print("try again")
    quit()

if game == 1:
    inputRounds = int(input("How many rounds would you like to play? "))

if inputRounds > 0:
    startGame = 1
else:
    print("try again")
    quit()

if startGame == 1:
    print("the game is now starting")

inputInGame = input("enter rock paper or scissors: ")
if inputInGame.lower() == "rock" or inputInGame.lower() == "r":
    rpc = "rock"
elif inputInGame.lower() == "paper" or inputInGame.lower() == "p":
    rpc = "paper"
elif inputInGame.lower() == "scissors" or inputInGame.lower() == "s":
    rpc = "scissors"
else:
    quit()

print("test user input", rpc)


def random_ai():
    random_num = random.randint(1, 3)

    if random_num == 1:
        string_rpc = "rock"
        return string_rpc
    elif random_num == 2:
        string_rpc = "paper"
        return string_rpc
    elif random_num == 3:
        string_rpc = "scissors"
        return string_rpc


print("test AI", random_ai())

if rpc == "rock" and random_ai() == "rock":
    print("the computer chose rock")
    print("tie")
elif rpc == "paper" and random_ai() == "paper":
    print("the computer chose paper")
    print("tie")
elif rpc == "scissors" and random_ai() == "scissors":
    print("the computer chose scissors")
    print("tie")
elif rpc == "rock" and random_ai() == "paper":
    print("the computer chose paper")
    print("You lose")
elif rpc == "paper" and random_ai() == "scissors":
    print("the computer chose scissors")
    print("You lose")
elif rpc == "scissors" and random_ai() == "rock":
    print("the computer chose rock")
    print("You lose")
elif rpc == "rock" and random_ai() == "scissors":
    print("the computer chose scissors")
    print("You win")
elif rpc == "paper" and random_ai() == "rock":
    print("the computer chose rock")
    print("You win")
elif rpc == "scissors" and random_ai() == "paper":
    print("the computer chose paper")
    print("You win")

# player_score += 1

def scores():
    player_score = 0
    ai_score = 0
    if player_score > ai_score:
        print("winning")
    elif ai_score > player_score:
        print("losing")
    elif ai_score == player_score:
        print("equal")




# intRounds = intRounds + 1
# if Winner == True:
# intScore = intScore + 1


# intRounds = 0
# intScore = 0