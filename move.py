def tic_tac_toe_move_check_syntax(move = False):
    if len(move) != 2: return False
    move = move.lower()
    if move[0] in ["a", "b", "c"] and move[1] in ["1", "2", "3"]:
        move = move.replace("a", "1")
        move = move.replace("b", "2")
        move = move.replace("c", "3")
        return [int(move[0])-1, int(move[1])-1]
    elif move[0] in ["1", "2", "3"] and move[1] in ["a", "b", "c"]:
        move = move[::-1]
        move = move.replace("a", "1")
        move = move.replace("b", "2")
        move = move.replace("c", "3")
        return [int(move[0])-1, int(move[1])-1]
    else: return False

def tic_tac_toe_move_check_availability(move = False, game_progress = False):
    try:
        if game_progress[move[0]][move[1]] == False: return move
        else: return False
    except:
        return False
    
def tic_tac_toe_move_check_result(game_progress = False):
    try:
        if game_progress[0][0] == game_progress[0][1] == game_progress[0][2] and game_progress[0][0] != False:
            return ["a1", "a2", "a3"]
        elif game_progress[1][0] == game_progress[1][1] == game_progress[1][2] and game_progress[1][0] != False:
            return ["b1", "b2", "b3"]
        elif game_progress[2][0] == game_progress[2][1] == game_progress[2][2] and game_progress[2][0] != False:
            return ["c1", "c2", "c3"]
        elif game_progress[0][0] == game_progress[1][0] == game_progress[2][0] and game_progress[0][0] != False:
            return ["a1", "b1", "c1"]
        elif game_progress[0][1] == game_progress[1][1] == game_progress[2][1] and game_progress[0][1] != False:
            return ["a2", "b2", "c2"]
        elif game_progress[0][2] == game_progress[1][2] == game_progress[2][2] and game_progress[0][2] != False:
            return ["a3", "b3", "c3"]
        elif game_progress[0][0] == game_progress[1][1] == game_progress[2][2] and game_progress[0][0] != False:
            return ["a1", "b2", "c3"]
        elif game_progress[0][2] == game_progress[1][1] == game_progress[2][0] and game_progress[0][2] != False:
            return ["a3", "b2", "c1"]
        elif False not in game_progress[0] and False not in game_progress[1] and False not in game_progress[2]: return "draw"
        else: return False
    except:
        return False