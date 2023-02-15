import sys
from random import randint

from functions import *
from animations import *

def tic_tac_toe_menu(player_1_settings = 1, player_2_settings = 1):

    operation=0

    player_1_name = "Player 'X'"
    player_2_name = "Player 'O'"

    text_lines = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: "",
        10: "",
        11: "",
        12: ""
    }
    game_progress = [
        [ randint(0, 2), randint(0, 2), randint(0, 2) ],
        [ randint(0, 2), randint(0, 2), randint(0, 2) ],
        [ randint(0, 2), randint(0, 2), randint(0, 2) ]
    ]
    animations_settings = {
        "border": True,
        "lines": True,
        "game_progress": True,
        "coordinates": True,
        "text_title": True,
        "text_lines": True,
        "text_footer": True
    }
    tic_tac_toe_animations(text_lines, game_progress, animations_settings)

    while operation != 1:

        player_config_operation = 1

        if player_1_settings == 1:
            player_1_settings_description = "Człowiek"
        elif player_1_settings == 2:
            player_1_settings_description = "SI poziom łatwy"
        elif player_1_settings == 3:
            player_1_settings_description = "SI poziom średni"
        else:
            player_1_settings_description = "SI poziom trudny"
        
        if player_2_settings == 1:
            player_2_settings_description = "Człowiek"
        elif player_2_settings == 2:
            player_2_settings_description = "SI poziom łatwy"
        elif player_2_settings == 3:
            player_2_settings_description = "SI poziom średni"
        else:
            player_2_settings_description = "SI poziom trudny"

        text_lines = {
            0: "",
            1: "",
            2: "Menu",
            3: player_1_name + " to " +  player_1_settings_description,
            4: player_2_name + " to " +  player_2_settings_description,
            5: "",
            6: "1. Graj",
            7: "2. Konfiguruj ustawienia dla "+ player_1_name,
            8: "3. Konfiguruj ustawienia dla "+ player_2_name,
            9: "",
            10: "Wybierz opcję z menu",
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

        operation = input_with_quit("Wybierz opcję z menu: ")

        if operation.isdigit() and int(operation) == 1:
            return [player_1_settings, player_2_settings, player_1_name, player_2_name]

        elif operation.isdigit() and int(operation) == 2:

            while int(player_config_operation)!=3:

                text_lines = {
                    0: "",
                    1: "",
                    2: "Konfiguracja ustawień dla "+ player_1_name,
                    3: "",
                    4: "",
                    5: "1. Nickname",
                    6: "2. Czy gracz jest człowiekiem czy SI",
                    7: "3. Powrót do menu głównego",
                    8: "",
                    9: "",
                    10: "Wybierz opcję z menu",
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

                player_config_operation = input_with_quit("Wybierz opcję z menu: ")

                if player_config_operation.isdigit() and int(player_config_operation) == 1:

                    text_lines = {
                        0: "",
                        1: "",
                        2: "Konfiguracja ustawień dla "+ player_1_name,
                        3: "",
                        4: "",
                        5: "",
                        6: "",
                        7: "Podaj nick dla "+ player_1_name,
                        8: "",
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
                        "text_lines": [7],
                        "text_footer": False
                    }
                    tic_tac_toe_animations(text_lines, game_progress, animations_settings)

                    player_1_name_temp = input_with_quit("Podaj nick dla "+ player_1_name +": ")
                    if player_1_name_temp.strip() != "": player_1_name = player_1_name_temp.strip()

                elif player_config_operation.isdigit() and int(player_config_operation) == 2:

                    text_lines = {
                        0: "",
                        1: "",
                        2: "Konfiguracja ustawień dla "+ player_1_name,
                        3: "",
                        4: "1. Człowiek",
                        5: "2. AI poziom łatwy",
                        6: "3. AI poziom średni",
                        7: "4. AI poziom trudny",
                        8: "",
                        9: "",
                        10: "Wybierz opcję z menu",
                        11: "",
                        12: ""
                    }
                    animations_settings = {
                        "border": False,
                        "lines": False,
                        "game_progress": False,
                        "coordinates": False,
                        "text_title": False,
                        "text_lines": [4, 5, 6, 7, 10],
                        "text_footer": False
                    }
                    tic_tac_toe_animations(text_lines, game_progress, animations_settings)

                    player_1_settings = int(input_with_quit("Wybierz opcję z menu: "))

        elif operation.isdigit() and int(operation) == 3:

            while int(player_config_operation)!=3:

                text_lines = {
                    0: "",
                    1: "",
                    2: "Konfiguracja ustawień dla "+ player_2_name,
                    3: "",
                    4: "",
                    5: "1. Nickname",
                    6: "2. Czy gracz jest człowiekiem czy SI",
                    7: "3. Powrót do menu głównego",
                    8: "",
                    9: "",
                    10: "Wybierz opcję z menu",
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

                player_config_operation = input_with_quit("Wybierz opcję z menu: ")

                if int(player_config_operation) == 1:

                    text_lines = {
                        0: "",
                        1: "",
                        2: "Konfiguracja ustawień dla "+ player_2_name,
                        3: "",
                        4: "",
                        5: "",
                        6: "",
                        7: "Podaj nick dla "+ player_2_name,
                        8: "",
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
                        "text_lines": [7],
                        "text_footer": False
                    }
                    tic_tac_toe_animations(text_lines, game_progress, animations_settings)

                    player_2_name_temp = input_with_quit("Podaj nick dla "+ player_2_name +": ")
                    if player_2_name_temp.strip() != "": player_2_name = player_2_name_temp.strip()

                elif int(player_config_operation) == 2:
 
                    text_lines = {
                        0: "",
                        1: "",
                        2: "Konfiguracja ustawień dla "+ player_2_name,
                        3: "",
                        4: "1. Człowiek",
                        5: "2. AI poziom łatwy",
                        6: "3. AI poziom średni",
                        7: "4. AI poziom trudny",
                        8: "",
                        9: "",
                        10: "Wybierz opcję z menu",
                        11: "",
                        12: ""
                    }
                    animations_settings = {
                        "border": False,
                        "lines": False,
                        "game_progress": False,
                        "coordinates": False,
                        "text_title": False,
                        "text_lines": [4, 5, 6, 7, 10],
                        "text_footer": False
                    }
                    tic_tac_toe_animations(text_lines, game_progress, animations_settings)

                    player_2_settings = int(input_with_quit("Wybierz opcję z menu: "))