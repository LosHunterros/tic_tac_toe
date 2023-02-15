from copy import deepcopy

from functions import *
from menu import *
from animations import *
from move import *

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

while True:
    settings = tic_tac_toe_menu(1, 1)

    player = {
        1: {"type": settings[0], "name": settings[2], "sign": "x"},
        2: {"type": settings[1], "name": settings[3], "sign": "o"}
    }
    player_active = 1

    text_lines = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "Rozpoczynamy grę!",
        7: "",
        8: "",
        9: "",
        10: "",
        11: "",
        12: ""
    }
    game_progress = [[False, False, False], [False, False, False], [False, False, False]]
    animations_settings = {
        "border": False,
        "lines": False,
        "game_progress": False,
        "coordinates": False,
        "text_title": False,
        "text_lines": True,
        "text_footer": False
    }
    tic_tac_toe_animations(text_lines, game_progress, animations_settings)

    time.sleep(1)

    game_progress = [["o", "o", "o"], ["o", "o", "o"], ["o", "o", "o"]]
    animations_settings = {
        "border": False,
        "lines": False,
        "game_progress": False,
        "coordinates": False,
        "text_title": False,
        "text_lines": False,
        "text_footer": False
    }
    tic_tac_toe_animations(text_lines, game_progress, animations_settings)

    time.sleep(0.5)

    game_progress = [[False, False, False], [False, False, False], [False, False, False]]
    tic_tac_toe_animations(text_lines, game_progress, animations_settings)

    time.sleep(0.5)

    game_progress = [["x", "x", "x"], ["x", "x", "x"], ["x", "x", "x"]]
    tic_tac_toe_animations(text_lines, game_progress, animations_settings)

    time.sleep(0.5)

    game_progress = [[False, False, False], [False, False, False], [False, False, False]]
    tic_tac_toe_animations(text_lines, game_progress, animations_settings)

    time.sleep(1)

    game_progress = [[False, False, False], [False, False, False], [False, False, False]]
    result = False

    while result == False:
        text_lines = {
            0: "",
            1: "Ruch wykonuje:",
            2: player[player_active]["name"],
            3: "",
            4: "Wstawiany znak:",
            5: graphic_sign[player[player_active]["sign"]][0],
            6: graphic_sign[player[player_active]["sign"]][1],
            7: graphic_sign[player[player_active]["sign"]][2],
            8: graphic_sign[player[player_active]["sign"]][3],
            9: graphic_sign[player[player_active]["sign"]][4],
            10: "",
            11: "Podaj współrzędne do wstawienia znaku",
            12: ""
        }
        animations_settings = {
            "border": False,
            "lines": False,
            "game_progress": False,
            "coordinates": False,
            "text_title": False,
            "text_lines": True,
            "text_footer": False
        }
        tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        move = input_with_quit("Podaj współrzędne do wstawienia znaku: ")

        move = tic_tac_toe_move_check_syntax(move)

        while move == False:

            text_lines = {
                0: "",
                1: "Ruch wykonuje:",
                2: player[player_active]["name"],
                3: "",
                4: "Wstawiany znak:",
                5: graphic_sign[player[player_active]["sign"]][0],
                6: graphic_sign[player[player_active]["sign"]][1],
                7: graphic_sign[player[player_active]["sign"]][2],
                8: graphic_sign[player[player_active]["sign"]][3],
                9: graphic_sign[player[player_active]["sign"]][4],
                10: "",
                11: "Błędne współrzędne!",
                12: ""
            }
            animations_settings = {
                "border": False,
                "lines": False,
                "game_progress": False,
                "coordinates": False,
                "text_title": False,
                "text_lines": [11],
                "text_footer": False
            }
            tic_tac_toe_animations(text_lines, game_progress, animations_settings)

            time.sleep(2)

            text_lines = {
                0: "",
                1: "Ruch wykonuje:",
                2: player[player_active]["name"],
                3: "",
                4: "Wstawiany znak:",
                5: graphic_sign[player[player_active]["sign"]][0],
                6: graphic_sign[player[player_active]["sign"]][1],
                7: graphic_sign[player[player_active]["sign"]][2],
                8: graphic_sign[player[player_active]["sign"]][3],
                9: graphic_sign[player[player_active]["sign"]][4],
                10: "",
                11: "Podaj współrzędne do wstawienia znaku",
                12: ""
            }
            tic_tac_toe_animations(text_lines, game_progress, animations_settings)

            move = input_with_quit("Podaj współrzędne do wstawienia znaku: ")
            move = tic_tac_toe_move_check_syntax(move)

        move = tic_tac_toe_move_check_availability(move, game_progress)

        while move == False:

            text_lines = {
                0: "",
                1: "Ruch wykonuje:",
                2: player[player_active]["name"],
                3: "",
                4: "Wstawiany znak:",
                5: graphic_sign[player[player_active]["sign"]][0],
                6: graphic_sign[player[player_active]["sign"]][1],
                7: graphic_sign[player[player_active]["sign"]][2],
                8: graphic_sign[player[player_active]["sign"]][3],
                9: graphic_sign[player[player_active]["sign"]][4],
                10: "",
                11: "Wskazane pole jest już zajęte!",
                12: ""
            }
            animations_settings = {
                "border": False,
                "lines": False,
                "game_progress": False,
                "coordinates": False,
                "text_title": False,
                "text_lines": [11],
                "text_footer": False
            }
            tic_tac_toe_animations(text_lines, game_progress, animations_settings)

            time.sleep(2)

            text_lines = {
                0: "",
                1: "Ruch wykonuje:",
                2: player[player_active]["name"],
                3: "",
                4: "Wstawiany znak:",
                5: graphic_sign[player[player_active]["sign"]][0],
                6: graphic_sign[player[player_active]["sign"]][1],
                7: graphic_sign[player[player_active]["sign"]][2],
                8: graphic_sign[player[player_active]["sign"]][3],
                9: graphic_sign[player[player_active]["sign"]][4],
                10: "",
                11: "Podaj współrzędne do wstawienia znaku",
                12: ""
            }
            tic_tac_toe_animations(text_lines, game_progress, animations_settings)

            move = input_with_quit("Podaj współrzędne do wstawienia znaku: ")
            move = tic_tac_toe_move_check_syntax(move)
            move = tic_tac_toe_move_check_availability(move, game_progress)

        game_progress[move[0]][move[1]] = player[player_active]["sign"]

        text_lines = {
            0: "",
            1: "Ruch wykonuje:",
            2: player[player_active]["name"],
            3: "",
            4: "Wstawiany znak:",
            5: graphic_sign[player[player_active]["sign"]][0],
            6: graphic_sign[player[player_active]["sign"]][1],
            7: graphic_sign[player[player_active]["sign"]][2],
            8: graphic_sign[player[player_active]["sign"]][3],
            9: graphic_sign[player[player_active]["sign"]][4],
            10: "",
            11: "Podaj współrzędne do wstawienia znaku",
            12: ""
        }
        animations_settings = {
            "border": False,
            "lines": False,
            "game_progress": [str(move[0]).replace("0", "a").replace("1", "b").replace("2", "c") + str(move[1]+1)],
            "coordinates": False,
            "text_title": False,
            "text_lines": False,
            "text_footer": False
        }
        tic_tac_toe_animations(text_lines, game_progress, animations_settings)

        result = tic_tac_toe_move_check_result(game_progress)

        if result == "draw":
            time.sleep(1)

            text_lines = {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "Koniec gry",
                5: "",
                6: "",
                7: "",
                8: "REMIS!",
                9: "",
                10: "",
                11: "",
                12: ""
            }
            animations_settings = {
                "border": False,
                "lines": False,
                "game_progress": [str(move[0]).replace("0", "a").replace("1", "b").replace("2", "c") + str(move[1]+1)],
                "coordinates": False,
                "text_title": False,
                "text_lines": True,
                "text_footer": False
            }
            tic_tac_toe_animations(text_lines, game_progress, animations_settings)

            time.sleep(2)

        elif isinstance(result, list):
            result_numbers = map(lambda x: x.replace("a", "1").replace("b", "2").replace("c", "3") , result)
            game_progress_reduced = deepcopy(game_progress)
            for number in result_numbers: game_progress_reduced[int(number[0])-1][int(number[1])-1] = False

            time.sleep(0.5)

            animations_settings = {
                "border": False,
                "lines": False,
                "game_progress": False,
                "coordinates": False,
                "text_title": False,
                "text_lines": False,
                "text_footer": False
            }
            tic_tac_toe_animations(text_lines, game_progress_reduced, animations_settings)

            time.sleep(0.5)

            tic_tac_toe_animations(text_lines, game_progress, animations_settings)

            time.sleep(0.5)

            tic_tac_toe_animations(text_lines, game_progress_reduced, animations_settings)

            time.sleep(0.5)

            tic_tac_toe_animations(text_lines, game_progress, animations_settings)

            time.sleep(0.5)

            tic_tac_toe_animations(text_lines, game_progress_reduced, animations_settings)

            time.sleep(0.5)

            tic_tac_toe_animations(text_lines, game_progress, animations_settings)

            time.sleep(1)

            text_lines = {
                0: "",
                1: "",
                2: "",
                3: "",
                4: "Koniec gry",
                5: "",
                6: "",
                7: "ZWYCIĘZCA:",
                8: player[player_active]["name"],
                9: "",
                10: "",
                11: "",
                12: ""
            }
            animations_settings = {
                "border": False,
                "lines": False,
                "game_progress": False,
                "coordinates": False,
                "text_title": False,
                "text_lines": True,
                "text_footer": False
            }
            tic_tac_toe_animations(text_lines, game_progress, animations_settings)

            time.sleep(2)

        if player_active == 1: player_active = 2
        else: player_active = 1