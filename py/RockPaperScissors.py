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
#
# if rpc == 1:
#     inGameRPC = "rock"
# elif rpc == 2:
#     inGameRPC = "paper"
# elif rpc == 3:
#     inGameRPC = "scissors"
# else:
#     quit()
#
# print(inGameRPC)


        # intRounds = intRounds + 1
        #
        # if boolWinner == True:
        #     intScore = intScore + 1


# intRounds = 0
# intScore = 0