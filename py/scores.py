def scores():
    player_score = 0
    ai_score = 0
    if player_score > ai_score:
        print("winning")
    elif ai_score > player_score:
        print("losing")
    elif ai_score == player_score:
        print("equal")