#Camden Levy and John Castilloux
import random

AUTHOR1 = "Camden"        # constants
AUTHOR2 = "John"

for x in "Game programmed by", AUTHOR1, AUTHOR2:            # for loop to begin
    print(x)
print("------------------------------------")
print("Rock Paper Scissors game\nCompete against the AI and gain score ")       # starting messages
print("-----------------------------------------------------------------")
print("To play competitive Rock Paper Scissors, you must type Play to continue.")

input1 = input("Type play to begin ")       # play input
if input1.lower() == "Play" or "P":        # parses through user input to start the game
    print("Game Begins")
    print("-----------------------------")
    inputRounds = int(input("How many rounds would you like to play? "))    # input number of rounds you want to play
    print("-----------------------------")
else:
    print("Try again")
    quit()

if inputRounds > 0:      # parses through input by user to make sure number of rounds are valid
    print("The game is now starting")
else:
    print("Try again")
    quit()

rounds = 0          # declare variables
player_score = 0
ai_score = 0
ties = 0

while rounds < inputRounds:     # loops until rounds are equal with number of rounds inputted by user
    inputInGame = input("Enter rock paper or scissors: ")        # user input with no case sensitivity
    if inputInGame.lower() == "rock" or inputInGame.lower() == "r":
        rps = "rock"
    elif inputInGame.lower() == "paper" or inputInGame.lower() == "p":
        rps = "paper"
    elif inputInGame.lower() == "scissors" or inputInGame.lower() == "s":
        rps = "scissors"
    else:
        quit()


    def random_ai():        # random generator assigning number value to rock, paper, or scissor
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


    rps_AI = random_ai()       # grabs result from random_ai function

    if rps == "rock" and rps_AI == "rock":      # game logic, win/lose/tie for each possible combo
        print("The computer chose rock")
        print("Tie")
        print("---------------------------------------")
        ties = ties +1
        rounds = rounds + 1
    elif rps == "paper" and rps_AI == "paper":
        print("The computer chose paper")
        print("Tie")
        print("---------------------------------------")
        ties = ties +1
        rounds = rounds + 1
    elif rps == "scissors" and rps_AI == "scissors":
        print("The computer chose scissors")
        print("Tie")
        print("---------------------------------------")
        ties = ties + 1
        rounds = rounds + 1
    elif rps == "rock" and rps_AI == "paper":
        print("The computer chose paper")
        print("You lose")
        print("---------------------------------------")
        ai_score = ai_score + 1
        rounds = rounds + 1
    elif rps == "paper" and rps_AI == "scissors":
        print("The computer chose scissors")
        print("You lose")
        print("---------------------------------------")
        ai_score = ai_score + 1
        rounds = rounds + 1
    elif rps == "scissors" and rps_AI == "rock":
        print("The computer chose rock")
        print("You lose")
        print("---------------------------------------")
        ai_score = ai_score + 1
        rounds = rounds + 1
    elif rps == "rock" and rps_AI == "scissors":
        print("The computer chose scissors")
        print("You win")
        print("---------------------------------------")
        player_score = player_score + 1
        rounds = rounds + 1
    elif rps == "paper" and rps_AI == "rock":
        print("The computer chose rock")
        print("You win")
        print("---------------------------------------")
        player_score = player_score + 1
        rounds = rounds + 1
    elif rps == "scissors" and rps_AI == "paper":
        print("The computer chose paper")
        print("You win")
        print("---------------------------------------")
        player_score = player_score + 1
        rounds = rounds + 1


def scores():      # function that compiles player scores & win/lose ratio at end of the entire game
    percent = ((player_score / rounds) * 100)
    if player_score > ai_score:
        print("Total games played:", inputRounds)
        print("You won")
        print("Your score is", player_score)
        print("Computer score is", ai_score)
        print("Number of ties", ties)
        print("You are winning ", round(percent, 3), "% of the time")
    elif ai_score > player_score:
        print("Total games played:", inputRounds)
        print("You lost")
        print("Your score is", player_score)
        print("Computer score is", ai_score)
        print("Number of ties", ties)
        print("you are winning ", round(percent, 3), "% of the time")
    elif ai_score == player_score:
        print("Total games played:", inputRounds)
        print("The score is equal, no winner")
        print("Your score is", player_score)
        print("Computer score is", ai_score)
        print("Number of ties", ties)
        print("You are winning ", round(percent, 3), "% of the time")


scores()       # prints scores function after while loop finishes all rounds

print("----------------------------------------")
print("Developed by", AUTHOR1, "and", AUTHOR2)     # end note for player

