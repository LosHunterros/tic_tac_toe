from os import system, name
import time
from sys import exit

import animations

def clear():
 
    if name=='nt':
        _ = system('cls')
    else:
        _ = system('clear')

def string_fill(string_original, lenght, align="center"):
    if len(string_original) > lenght:
        string_original = string_original[0:lenght]
    
    if align == "left":
        return string_original + ( lenght - len(string_original) ) * " "
    elif align == "right":
        return ( lenght - len(string_original) ) * " " + string_original
    else:
        return ( ( lenght - len(string_original) ) // 2 ) * " " + string_original + ( lenght - ( ( lenght - len(string_original) ) // 2 ) - len(string_original) ) * " "

def input_with_quit(question = ""):
    answer = input(question)
    if answer.lower() == "quit":
        text_lines = {
            4: "Dziękujemy za grę"
        }
        game_progress = [
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, False ]
        ]
        animations_settings = {
            "game_progress": False,
            "text_lines": True
        }
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.01)
        game_progress = [
            [ "o", False, False ],
            [ False, False, False ],
            [ False, False, False ]
        ]
        animations_settings = {
            "game_progress": True,
            "text_lines": False
        }
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, "o", False ],
            [ False, False, False ],
            [ False, False, False ]
        ]
        animations_settings = {
            "game_progress": False,
            "text_lines": False
        }
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, False, "o" ],
            [ False, False, False ],
            [ False, False, False ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, False, False ],
            [ "o", False, False ],
            [ False, False, False ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ "x", False, False ],
            [ False, "o", False ],
            [ False, False, False ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, "x", False ],
            [ False, False, "o" ],
            [ False, False, False ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, False, "x" ],
            [ False, False, False ],
            [ "o", False, False ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, False, False ],
            [ "x", False, False ],
            [ False, "o", False ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, False, False ],
            [ False, "x", False ],
            [ False, False, "o" ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, False, False ],
            [ False, False, "x" ],
            [ False, False, False ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, False, False ],
            [ False, False, False ],
            [ "x", False, False ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, False, False ],
            [ False, False, False ],
            [ False, "x", False ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, "x" ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        game_progress = [
            [ False, False, False ],
            [ False, False, False ],
            [ False, False, False ]
        ]
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        time.sleep(0.1)
        text_lines = {
            4: "Dziękujemy za grę",
            8: "Zapraszamy ponownie!"
        }
        animations_settings = {
            "text_lines": [8]
        }
        animations.tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        exit()
    return answer