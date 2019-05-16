score_names = ["Love", "Fifteen", "Thirty", "Forty", "Advantage Player 1",
               "Advantage Player 2", "Deuce", "Win for Player 1", "Win for Player 2"]


def tennis_score(player1_points, player2_points):
    if player1_points == player2_points and player1_points <= 2:
        return "{0}-All".format(score_names[player1_points])
    elif player1_points >= 3 and player1_points == player2_points:
        return "Deuce"
    elif player1_points <= 3 and player2_points <= 3:
        return "{0}-{1}".format(score_names[player1_points],
                                score_names[player2_points])
    elif player1_points >= 4 and player2_points == player1_points - 1:
        return "Advantage Player 1"
    elif player1_points == player2_points - 1 and player2_points >= 5:
        return "Advantage Player 2"
    elif player1_points - player2_points == 2 or player1_points - player2_points == 4:
        return "Win for Player 1"
    elif player2_points - player1_points == 2 and player2_points >= 4:
        return "Win for Player 2"
