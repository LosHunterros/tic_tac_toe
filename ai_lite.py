import random

def  get_random_ai_coordinates(game_progress):

    coordinate_1 = random.randint(0,2)
    coordinate_2 = random.randint(0,2)
    
    if game_progress[coordinate_1][coordinate_2] == False: return (coordinate_1,coordinate_2)
    else: 
        get_random_ai_coordinates(game_progress)

