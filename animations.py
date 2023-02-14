import time
from random import randint

import functions

def tic_tac_toe_animations(text_lines = {}, game_progress = False, animations_settings = False):
    '''
    Show actual stat of the game with messages and optional animations
    How to configure

    Messages to users
    text_lines = {
        0: "", // string of skip this index
        1: "", // string of skip this index
        2: "", // string of skip this index
        3: "", // string of skip this index
        4: "", // string of skip this index
        5: "", // string of skip this index
        6: "", // string of skip this index
        7: "", // string of skip this index
        8: "", // string of skip this index
        9: "", // string of skip this index
        10: "", // string of skip this index
        11: "", // string of skip this index
        12: ""  // string of skip this index
    }

    2 dimensions list with actual values of game fields, eg.:
    game_progress = [
        [ "o", "o", "o" ],
        [ "x", "x", "x" ],
        [ False, False, False ]
    ]
    or False to empty or "random" to display all fields in random state

    Which elements have to be animated
    animations_settings = {
        "border": False, // True or False - overall border
        "lines": False, // True or False - lines separating game fields
        "game_progress": False, // True, False or list of fields to animate (eg. ["a1", "b2", "c3"]) - value of game fields
        "coordinates": False, // True or False - numbers and letters symbolizing rows and columns
        "text_title": False, // True or False - Title od the game
        "text_lines": False, // True, False or list of lines to animate (eg. [2, 4, 6, 8]) - Messages to users
        "text_footer": False // True or False - Footer with information about quiting
    }
    '''

    # Validating argument text_lines
    i = 0
    while i < 13:
        try:
            if not isinstance(text_lines[i], str):
                text_lines[i] = ""
        except:
            text_lines[i] = ""
        i += 1

    # Validating argument game_progress
    if game_progress == False:
        game_progress = [[False, False, False], [False, False, False], [False, False, False]]
    elif game_progress == "random":
        game_progress = [[randint(0, 2), randint(0, 2), randint(0, 2)], [randint(0, 2), randint(0, 2), randint(0, 2)], [randint(0, 2), randint(0, 2), randint(0, 2)]]
    try:
        game_progress[0][0]
        game_progress[0][1]
        game_progress[0][2]
        game_progress[1][0]
        game_progress[1][1]
        game_progress[1][2]
        game_progress[2][0]
        game_progress[2][1]
        game_progress[2][2]
    except:
        game_progress = [[False, False, False], [False, False, False], [False, False, False]]
    i = 0
    while i < 3:
        j = 0
        while j < 3:
            if game_progress[i][j] == 1:
                game_progress[i][j] = "o"
            elif game_progress[i][j] == 2:
                game_progress[i][j] = "x"
            elif game_progress[i][j] != "o" and game_progress[i][j] != "x":
                game_progress[i][j] = False
            j += 1
        i += 1
    
    # Validating argument animations_settings
    if not isinstance(animations_settings, dict):
        animations = {
            "border": False,
            "lines": False,
            "game_progress": True,
            "coordinates": False,
            "text_title": False,
            "text_lines": False,
            "text_footer": False
        }
    else:
        try:
            if animations_settings["border"] != True: animations_settings["border"] = False
        except:
            animations_settings["border"] = False
        try:
            if animations_settings["lines"] != True: animations_settings["lines"] = False
        except:
            animations_settings["lines"] = False
        try:
            if animations_settings["game_progress"] != True and not isinstance(animations_settings["game_progress"], list): animations_settings["game_progress"] = False
        except:
            animations_settings["game_progress"] = False
        try:
            if animations_settings["coordinates"] != True: animations_settings["coordinates"] = False
        except:
            animations_settings["coordinates"] = False
        try:
            if animations_settings["text_title"] != True: animations_settings["text_title"] = False
        except:
            animations_settings["text_title"] = False
        try:
            if animations_settings["text_lines"] != True and not isinstance(animations_settings["text_lines"], list): animations_settings["text_lines"] = False
        except:
            animations_settings["text_lines"] = False
        try:
            if animations_settings["text_footer"] != True: animations_settings["text_footer"] = False
        except:
            animations_settings["text_footer"] = False

    # Graphic representation of O and X symbols
    graphic_sign = {}
    graphic_sign["x"] = [
        "▄▄   ▄▄",
        " ▐█ █▌ ",
        "  ▐█▌  ",
        " ▐█ █▌ ",
        "▀▀   ▀▀"
    ]
    graphic_sign["o"] = [
        "  ▄▄▄  ",
        " █▌ ▐█ ",
        "█▌   ▐█",
        " █▌ ▐█ ",
        "  ▀▀▀  "
    ]
    graphic_sign[False] = [
        "       ",
        "       ",
        "       ",
        "       ",
        "       "
    ]

    # Empty game visualization to successive fill it and creat next "frames" of animation
    graphic_final = [
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 ",
        "                                                                                                 "
    ]
    for i, line in enumerate(graphic_final):
        graphic_final[i] = list(line)

    # Filled template from which chars will be taken to successive "frames" of animation
    graphic_begin = [
        "▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄",
        "█                                                                                               █",
        "█        ▀█▀ █ ▐█▀   ▀█▀  █  ▐█▀   ▀█▀  █  █▀▀                 1           2           3        █",
        "█         █  █ █      █  ▐ ▌ █      █  █ █ █                         ╥           ╥              █",
        "█         █  █ █      █  █▄█ █      █  █ █ █▀               "+graphic_sign[game_progress[0][0]][0]+"  ║  "+graphic_sign[game_progress[0][1]][0]+"  ║  "+graphic_sign[game_progress[0][2]][0]+"     █",
        "█         █  █ ▐█▄    █  █ █ ▐█▄    █   █  █▄▄              "+graphic_sign[game_progress[0][0]][1]+"  ║  "+graphic_sign[game_progress[0][1]][1]+"  ║  "+graphic_sign[game_progress[0][2]][1]+"     █",
        "█                                                      A    "+graphic_sign[game_progress[0][0]][2]+"  ║  "+graphic_sign[game_progress[0][1]][2]+"  ║  "+graphic_sign[game_progress[0][2]][2]+"     █",
        "█ "+functions.string_fill(text_lines[0], 52)+"      "+graphic_sign[game_progress[0][0]][3]+"  ║  "+graphic_sign[game_progress[0][1]][3]+"  ║  "+graphic_sign[game_progress[0][2]][3]+"     █",
        "█ "+functions.string_fill(text_lines[1], 52)+"      "+graphic_sign[game_progress[0][0]][4]+"  ║  "+graphic_sign[game_progress[0][1]][4]+"  ║  "+graphic_sign[game_progress[0][2]][4]+"     █",
        "█ "+functions.string_fill(text_lines[2], 52)+"   ╞═══════════╬═══════════╬═══════════╡  █",
        "█ "+functions.string_fill(text_lines[3], 52)+"      "+graphic_sign[game_progress[1][0]][0]+"  ║  "+graphic_sign[game_progress[1][1]][0]+"  ║  "+graphic_sign[game_progress[1][2]][0]+"     █",
        "█ "+functions.string_fill(text_lines[4], 52)+"      "+graphic_sign[game_progress[1][0]][1]+"  ║  "+graphic_sign[game_progress[1][1]][1]+"  ║  "+graphic_sign[game_progress[1][2]][1]+"     █",
        "█ "+functions.string_fill(text_lines[5], 52)+" B    "+graphic_sign[game_progress[1][0]][2]+"  ║  "+graphic_sign[game_progress[1][1]][2]+"  ║  "+graphic_sign[game_progress[1][2]][2]+"     █",
        "█ "+functions.string_fill(text_lines[6], 52)+"      "+graphic_sign[game_progress[1][0]][3]+"  ║  "+graphic_sign[game_progress[1][1]][3]+"  ║  "+graphic_sign[game_progress[1][2]][3]+"     █",
        "█ "+functions.string_fill(text_lines[7], 52)+"      "+graphic_sign[game_progress[1][0]][4]+"  ║  "+graphic_sign[game_progress[1][1]][4]+"  ║  "+graphic_sign[game_progress[1][2]][4]+"     █",
        "█ "+functions.string_fill(text_lines[8], 52)+"   ╞═══════════╬═══════════╬═══════════╡  █",
        "█ "+functions.string_fill(text_lines[9], 52)+"      "+graphic_sign[game_progress[2][0]][0]+"  ║  "+graphic_sign[game_progress[2][1]][0]+"  ║  "+graphic_sign[game_progress[2][2]][0]+"     █",
        "█ "+functions.string_fill(text_lines[10], 52)+"      "+graphic_sign[game_progress[2][0]][1]+"  ║  "+graphic_sign[game_progress[2][1]][1]+"  ║  "+graphic_sign[game_progress[2][2]][1]+"     █",
        "█ "+functions.string_fill(text_lines[11], 52)+" C    "+graphic_sign[game_progress[2][0]][2]+"  ║  "+graphic_sign[game_progress[2][1]][2]+"  ║  "+graphic_sign[game_progress[2][2]][2]+"     █",
        "█ "+functions.string_fill(text_lines[12], 52)+"      "+graphic_sign[game_progress[2][0]][3]+"  ║  "+graphic_sign[game_progress[2][1]][3]+"  ║  "+graphic_sign[game_progress[2][2]][3]+"     █",
        "█                                                           "+graphic_sign[game_progress[2][0]][4]+"  ║  "+graphic_sign[game_progress[2][1]][4]+"  ║  "+graphic_sign[game_progress[2][2]][4]+"     █",
        "█ "+functions.string_fill("Wpisz 'Quit' aby zakończyć grę", 52)+"               ╨           ╨              █",
        "█                                                                                               █",
        "▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀"
    ]

    animation_frames = {}

    # Localization of border chars in animation order
    animation_frames["border"] = []
    i = 0
    while i < 97:
        animation_frames["border"].append([[0,i]])
        i += 1
    i = 0
    while i < 24:
        animation_frames["border"].append([[i,96]])
        i += 1
    i = 96
    while i >= 0:
        animation_frames["border"].append([[23,i]])
        i -= 1
    i = 23
    while i >= 0:
        animation_frames["border"].append([[i,0]])
        i -= 1

    # Localization of lines chars in animation order
    animation_frames["lines"] = []
    i = 0
    while i < 19:
        animation_frames["lines"].append([[3+i,69]])
        i += 1
    i = 18
    while i >= 0:
        animation_frames["lines"].append([[3+i,81]])
        i -= 1
    i = 0
    while i < 37:
        animation_frames["lines"].append([[9,57+i]])
        i += 1
    i = 36
    while i >= 0:
        animation_frames["lines"].append([[15,57+i]])
        i -= 1

    # Localization of game_progress chars in animation order
    animation_frames["a1"] = []
    if game_progress[0][0] != False:
        i = 4
        j = 60
        animation_frames["a1"].append([[i,j],[i,j+1],[i,j+2],[i,j+3],[i,j+4],[i,j+5],[i,j+6]])
        animation_frames["a1"].append([[i+1,j],[i+1,j+1],[i+1,j+2],[i+1,j+3],[i+1,j+4],[i+1,j+5],[i+1,j+6]])
        animation_frames["a1"].append([[i+2,j],[i+2,j+1],[i+2,j+2],[i+2,j+3],[i+2,j+4],[i+2,j+5],[i+2,j+6]])
        animation_frames["a1"].append([[i+3,j],[i+3,j+1],[i+3,j+2],[i+3,j+3],[i+3,j+4],[i+3,j+5],[i+3,j+6]])
        animation_frames["a1"].append([[i+4,j],[i+4,j+1],[i+4,j+2],[i+4,j+3],[i+4,j+4],[i+4,j+5],[i+4,j+6]])
    animation_frames["a2"] = []
    if game_progress[0][1] != False:
        i = 4
        j = 72
        animation_frames["a2"].append([[i,j],[i,j+1],[i,j+2],[i,j+3],[i,j+4],[i,j+5],[i,j+6]])
        animation_frames["a2"].append([[i+1,j],[i+1,j+1],[i+1,j+2],[i+1,j+3],[i+1,j+4],[i+1,j+5],[i+1,j+6]])
        animation_frames["a2"].append([[i+2,j],[i+2,j+1],[i+2,j+2],[i+2,j+3],[i+2,j+4],[i+2,j+5],[i+2,j+6]])
        animation_frames["a2"].append([[i+3,j],[i+3,j+1],[i+3,j+2],[i+3,j+3],[i+3,j+4],[i+3,j+5],[i+3,j+6]])
        animation_frames["a2"].append([[i+4,j],[i+4,j+1],[i+4,j+2],[i+4,j+3],[i+4,j+4],[i+4,j+5],[i+4,j+6]])
    animation_frames["a3"] = []
    if game_progress[0][2] != False:
        i = 4
        j = 84
        animation_frames["a3"].append([[i,j],[i,j+1],[i,j+2],[i,j+3],[i,j+4],[i,j+5],[i,j+6]])
        animation_frames["a3"].append([[i+1,j],[i+1,j+1],[i+1,j+2],[i+1,j+3],[i+1,j+4],[i+1,j+5],[i+1,j+6]])
        animation_frames["a3"].append([[i+2,j],[i+2,j+1],[i+2,j+2],[i+2,j+3],[i+2,j+4],[i+2,j+5],[i+2,j+6]])
        animation_frames["a3"].append([[i+3,j],[i+3,j+1],[i+3,j+2],[i+3,j+3],[i+3,j+4],[i+3,j+5],[i+3,j+6]])
        animation_frames["a3"].append([[i+4,j],[i+4,j+1],[i+4,j+2],[i+4,j+3],[i+4,j+4],[i+4,j+5],[i+4,j+6]])
    animation_frames["b1"] = []
    if game_progress[1][0] != False:
        i = 10
        j = 60
        animation_frames["b1"].append([[i,j],[i,j+1],[i,j+2],[i,j+3],[i,j+4],[i,j+5],[i,j+6]])
        animation_frames["b1"].append([[i+1,j],[i+1,j+1],[i+1,j+2],[i+1,j+3],[i+1,j+4],[i+1,j+5],[i+1,j+6]])
        animation_frames["b1"].append([[i+2,j],[i+2,j+1],[i+2,j+2],[i+2,j+3],[i+2,j+4],[i+2,j+5],[i+2,j+6]])
        animation_frames["b1"].append([[i+3,j],[i+3,j+1],[i+3,j+2],[i+3,j+3],[i+3,j+4],[i+3,j+5],[i+3,j+6]])
        animation_frames["b1"].append([[i+4,j],[i+4,j+1],[i+4,j+2],[i+4,j+3],[i+4,j+4],[i+4,j+5],[i+4,j+6]])
    animation_frames["b2"] = []
    if game_progress[1][1] != False:
        i = 10
        j = 72
        animation_frames["b2"].append([[i,j],[i,j+1],[i,j+2],[i,j+3],[i,j+4],[i,j+5],[i,j+6]])
        animation_frames["b2"].append([[i+1,j],[i+1,j+1],[i+1,j+2],[i+1,j+3],[i+1,j+4],[i+1,j+5],[i+1,j+6]])
        animation_frames["b2"].append([[i+2,j],[i+2,j+1],[i+2,j+2],[i+2,j+3],[i+2,j+4],[i+2,j+5],[i+2,j+6]])
        animation_frames["b2"].append([[i+3,j],[i+3,j+1],[i+3,j+2],[i+3,j+3],[i+3,j+4],[i+3,j+5],[i+3,j+6]])
        animation_frames["b2"].append([[i+4,j],[i+4,j+1],[i+4,j+2],[i+4,j+3],[i+4,j+4],[i+4,j+5],[i+4,j+6]])
    animation_frames["b3"] = []
    if game_progress[1][2] != False:
        i = 10
        j = 84
        animation_frames["b3"].append([[i,j],[i,j+1],[i,j+2],[i,j+3],[i,j+4],[i,j+5],[i,j+6]])
        animation_frames["b3"].append([[i+1,j],[i+1,j+1],[i+1,j+2],[i+1,j+3],[i+1,j+4],[i+1,j+5],[i+1,j+6]])
        animation_frames["b3"].append([[i+2,j],[i+2,j+1],[i+2,j+2],[i+2,j+3],[i+2,j+4],[i+2,j+5],[i+2,j+6]])
        animation_frames["b3"].append([[i+3,j],[i+3,j+1],[i+3,j+2],[i+3,j+3],[i+3,j+4],[i+3,j+5],[i+3,j+6]])
        animation_frames["b3"].append([[i+4,j],[i+4,j+1],[i+4,j+2],[i+4,j+3],[i+4,j+4],[i+4,j+5],[i+4,j+6]])
    animation_frames["c1"] = []
    if game_progress[2][0] != False:
        i = 16
        j = 60
        animation_frames["c1"].append([[i,j],[i,j+1],[i,j+2],[i,j+3],[i,j+4],[i,j+5],[i,j+6]])
        animation_frames["c1"].append([[i+1,j],[i+1,j+1],[i+1,j+2],[i+1,j+3],[i+1,j+4],[i+1,j+5],[i+1,j+6]])
        animation_frames["c1"].append([[i+2,j],[i+2,j+1],[i+2,j+2],[i+2,j+3],[i+2,j+4],[i+2,j+5],[i+2,j+6]])
        animation_frames["c1"].append([[i+3,j],[i+3,j+1],[i+3,j+2],[i+3,j+3],[i+3,j+4],[i+3,j+5],[i+3,j+6]])
        animation_frames["c1"].append([[i+4,j],[i+4,j+1],[i+4,j+2],[i+4,j+3],[i+4,j+4],[i+4,j+5],[i+4,j+6]])
    animation_frames["c2"] = []
    if game_progress[2][1] != False:
        i = 16
        j = 72
        animation_frames["c2"].append([[i,j],[i,j+1],[i,j+2],[i,j+3],[i,j+4],[i,j+5],[i,j+6]])
        animation_frames["c2"].append([[i+1,j],[i+1,j+1],[i+1,j+2],[i+1,j+3],[i+1,j+4],[i+1,j+5],[i+1,j+6]])
        animation_frames["c2"].append([[i+2,j],[i+2,j+1],[i+2,j+2],[i+2,j+3],[i+2,j+4],[i+2,j+5],[i+2,j+6]])
        animation_frames["c2"].append([[i+3,j],[i+3,j+1],[i+3,j+2],[i+3,j+3],[i+3,j+4],[i+3,j+5],[i+3,j+6]])
        animation_frames["c2"].append([[i+4,j],[i+4,j+1],[i+4,j+2],[i+4,j+3],[i+4,j+4],[i+4,j+5],[i+4,j+6]])
    animation_frames["c3"] = []
    if game_progress[2][2] != False:
        i = 16
        j = 84
        animation_frames["c3"].append([[i,j],[i,j+1],[i,j+2],[i,j+3],[i,j+4],[i,j+5],[i,j+6]])
        animation_frames["c3"].append([[i+1,j],[i+1,j+1],[i+1,j+2],[i+1,j+3],[i+1,j+4],[i+1,j+5],[i+1,j+6]])
        animation_frames["c3"].append([[i+2,j],[i+2,j+1],[i+2,j+2],[i+2,j+3],[i+2,j+4],[i+2,j+5],[i+2,j+6]])
        animation_frames["c3"].append([[i+3,j],[i+3,j+1],[i+3,j+2],[i+3,j+3],[i+3,j+4],[i+3,j+5],[i+3,j+6]])
        animation_frames["c3"].append([[i+4,j],[i+4,j+1],[i+4,j+2],[i+4,j+3],[i+4,j+4],[i+4,j+5],[i+4,j+6]])

    # Localization of coordinates chars in animation order
    animation_frames["coordinates"] = []
    animation_frames["coordinates"].append([[2,63]])
    animation_frames["coordinates"].append([[2,75]])
    animation_frames["coordinates"].append([[2,87]])
    animation_frames["coordinates"].append([[6,55]])
    animation_frames["coordinates"].append([[12,55]])
    animation_frames["coordinates"].append([[18,55]])

    # Localization of text_title chars in animation order
    animation_frames["text_title"] = []
    i = 0
    while i < 37:
        animation_frames["text_title"].append([[2,9+i],[3,9+i],[4,9+i],[5,9+i]])
        i += 1

    # Localization of text_lines chars in animation order
    animation_frames["text_lines"] = []
    i = 0
    while i < 13:
        animation_frames["text_lines"].append([])
        if len(text_lines[i]) > 0:
            j = 1
            while graphic_begin[i+7][j] == " ":
                j += 1
            k = j
            while j < k + len(text_lines[i]):
                animation_frames["text_lines"][i].append([[i+7,j]])
                j += 1
        i += 1

    # Localization of text_footer chars in animation order
    animation_frames["text_footer"] = []
    i = 0
    while i < 30:
        animation_frames["text_footer"].append([[21,13+i]])
        i += 1

    # Adding frames to animation or instantly to game visualization depending of animation settings

    animation = []

    if animations_settings["border"]:
        for frame in animation_frames["border"]:
            animation.append(frame)
    else:
        for frame in animation_frames["border"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]

    if animations_settings["lines"]:
        for frame in animation_frames["lines"]:
            animation.append(frame)
    else:
        for frame in animation_frames["lines"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]

    if animations_settings["game_progress"] == True or ( isinstance(animations_settings["game_progress"], list) and "a1" in animations_settings["game_progress"] ):
        for frame in animation_frames["a1"]:
            animation.append(frame)
    else:
        for frame in animation_frames["a1"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]
    if animations_settings["game_progress"] == True or ( isinstance(animations_settings["game_progress"], list) and "a2" in animations_settings["game_progress"] ):
        for frame in animation_frames["a2"]:
            animation.append(frame)
    else:
        for frame in animation_frames["a2"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]
    if animations_settings["game_progress"] == True or ( isinstance(animations_settings["game_progress"], list) and "a3" in animations_settings["game_progress"] ):
        for frame in animation_frames["a3"]:
            animation.append(frame)
    else:
        for frame in animation_frames["a3"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]
    if animations_settings["game_progress"] == True or ( isinstance(animations_settings["game_progress"], list) and "b1" in animations_settings["game_progress"] ):
        for frame in animation_frames["b1"]:
            animation.append(frame)
    else:
        for frame in animation_frames["b1"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]
    if animations_settings["game_progress"] == True or ( isinstance(animations_settings["game_progress"], list) and "b2" in animations_settings["game_progress"] ):
        for frame in animation_frames["b2"]:
            animation.append(frame)
    else:
        for frame in animation_frames["b2"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]
    if animations_settings["game_progress"] == True or ( isinstance(animations_settings["game_progress"], list) and "b3" in animations_settings["game_progress"] ):
        for frame in animation_frames["b3"]:
            animation.append(frame)
    else:
        for frame in animation_frames["b3"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]
    if animations_settings["game_progress"] == True or ( isinstance(animations_settings["game_progress"], list) and "c1" in animations_settings["game_progress"] ):
        for frame in animation_frames["c1"]:
            animation.append(frame)
    else:
        for frame in animation_frames["c1"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]
    if animations_settings["game_progress"] == True or ( isinstance(animations_settings["game_progress"], list) and "c2" in animations_settings["game_progress"] ):
        for frame in animation_frames["c2"]:
            animation.append(frame)
    else:
        for frame in animation_frames["c2"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]
    if animations_settings["game_progress"] == True or ( isinstance(animations_settings["game_progress"], list) and "c3" in animations_settings["game_progress"] ):
        for frame in animation_frames["c3"]:
            animation.append(frame)
    else:
        for frame in animation_frames["c3"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]

    if animations_settings["coordinates"]:
        for frame in animation_frames["coordinates"]:
            animation.append(frame)
    else:
        for frame in animation_frames["coordinates"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]

    if animations_settings["text_title"]:
        for frame in animation_frames["text_title"]:
            animation.append(frame)
    else:
        for frame in animation_frames["text_title"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]

    for i, line in enumerate(animation_frames["text_lines"]):
        if animations_settings["text_lines"] == True or ( isinstance(animations_settings["text_lines"], list) and i in animations_settings["text_lines"] ):
            for frame in line:
                animation.append(frame)
        else:
            for frame in line:
                for frame_pixel in frame:
                    graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]

    if animations_settings["text_footer"]:
        for frame in animation_frames["text_footer"]:
            animation.append(frame)
    else:
        for frame in animation_frames["text_footer"]:
            for frame_pixel in frame:
                graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]

    functions.clear()

    # Executing animations 

    for frame in animation:
        functions.clear()
        for frame_pixel in frame:
            graphic_final[frame_pixel[0]][frame_pixel[1]] = graphic_begin[frame_pixel[0]][frame_pixel[1]]
        print("\n".join(map(lambda x: ("").join(x), graphic_final)))
        time.sleep(0.01)

    # Print whole 

    functions.clear()
    print("\n".join(map(lambda x: ("").join(x), graphic_begin)))