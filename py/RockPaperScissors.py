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
    print("the game is now starting")
else:
    print("try again")
    quit()

inputInGame = input("enter rock paper or scissors: ")
if inputInGame.lower() == "rock" or inputInGame.lower() == "r":
    rps = "rock"
elif inputInGame.lower() == "paper" or inputInGame.lower() == "p":
    rps = "paper"
elif inputInGame.lower() == "scissors" or inputInGame.lower() == "s":
    rps = "scissors"
else:
    quit()

def random_ai():
    random_num = random.randint(1, 3)

    if random_num == 1:
        string_rps = "rock"
        return string_rps
    elif random_num == 2:
        string_rps = "paper"
        return string_rps
    elif random_num == 3:
        string_rps = "scissors"
        return string_rps


rps_AI = random_ai()
print(rps_AI)

player_score = 0
ai_score = 0

if rps == "rock" and rps_AI == "rock":
    print("the computer chose rock")
    print("tie")
elif rps == "paper" and rps_AI == "paper":
    print("the computer chose paper")
    print("tie")
elif rps == "scissors" and rps_AI == "scissors":
    print("the computer chose scissors")
    print("tie")
elif rps == "rock" and rps_AI == "paper":
    print("the computer chose paper")
    print("You lose")
    ai_score = ai_score + 1
elif rps == "paper" and rps_AI == "scissors":
    print("the computer chose scissors")
    print("You lose")
    ai_score = ai_score + 1
elif rps == "scissors" and rps_AI == "rock":
    print("the computer chose rock")
    print("You lose")
    ai_score = ai_score + 1
elif rps == "rock" and rps_AI == "scissors":
    print("the computer chose scissors")
    print("You win")
    player_score = player_score + 1
elif rps == "paper" and rps_AI == "rock":
    print("the computer chose rock")
    print("You win")
    player_score = player_score + 1
elif rps == "scissors" and rps_AI == "paper":
    print("the computer chose paper")
    print("You win")
    player_score = player_score + 1


def scores():
    if player_score > ai_score:
        print("Winning")
        print("Your score is", player_score)
        print("Computer score is", ai_score)
    elif ai_score > player_score:
        print("losing")
        print("Your score is", player_score)
        print("Computer score is", ai_score)
    elif ai_score == player_score:
        print("equal")
        print("Your score is", player_score)
        print("Computer score is", ai_score)


scores()
