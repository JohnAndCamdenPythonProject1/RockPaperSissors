import random
random1 = random.randint(1,3)

stringRPC = "blank"
if random1 == 1:
    stringRPC = "Rock"
elif random1 == 2:
    stringRPC = "Paper"
elif random1 == 3:
    stringRPC = "Scissors"

print(stringRPC)
