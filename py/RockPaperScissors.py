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

intRounds = 0
intScore = 0
if startGame == 1:
    print("the game is now starting")
    # while intRounds < inputRounds:

inGameRPC = 0
inputInGame = input("enter rock paper or scissors: ")
if inputInGame.lower() == "rock" or "r":
    inGameRPC = 1
    print(inGameRPC)
elif inputInGame.lower() == "paper" or "p":
    inGameRPC = 2
    print(inGameRPC)
elif inputInGame.lower() == "scissors" or "s":
    inGameRPC = 3
    print(inGameRPC)
else:
    quit()




        # intRounds = intRounds + 1
        #
        # if boolWinner == True:
        #     intScore = intScore + 1
