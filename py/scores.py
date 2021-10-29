def scores():
    player_score = 0
    ai_score = 0
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

