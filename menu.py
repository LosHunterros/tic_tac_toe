import sys

from functions import *

def fill_space(n,string_1,string_2):
    return ((n - len(string_1)) - len(string_2))*" "

def tic_tac_toe_menu(player_1_settings = 1, player_2_settings = 1):

    operation=0

    player_1_name = "Player_1"
    player_2_name = "Player_2"

    while operation != 1:

        player_config_operation = 1

        if player_1_settings == 1:
            player_1_settings_description = "Człowiek"
        elif player_1_settings == 2:
            player_1_settings_description = "AI poziom łatwy"
        elif player_1_settings == 3:
            player_1_settings_description = "AI poziom średni"
        else:
            player_1_settings_description = "AI poziom trudny"
        
        if player_2_settings == 1:
            player_2_settings_description = "Człowiek"
        elif player_2_settings == 2:
            player_2_settings_description = "AI poziom łatwy"
        elif player_2_settings == 3:
            player_2_settings_description = "AI poziom średni"
        else:
            player_2_settings_description = "AI poziom trudny"

        clear()
        print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
        print("█                                                     █")
        print("█      Witaj w grze Tic Tac Toe!                      █")
        print("█                                                     █")
        print("█              Menu                                   █")
        print("█      "+ player_1_name + " to " +  player_1_settings_description + fill_space(43, player_1_name, player_1_settings_description) + "█", sep = "")
        print("█      "+ player_2_name + " to " +  player_2_settings_description + fill_space(43, player_2_name, player_2_settings_description) + "█", sep = "")
        print("█                                                     █")
        print("█      1. Graj                                        █")
        print("█      2. Konfiguruj ustawienia dla "+ player_1_name + fill_space(18, player_1_name, "") + "█", sep="")
        print("█      3. Konfiguruj ustawienia dla "+ player_2_name + fill_space(18, player_2_name, "") + "█", sep="")
        print("█                                                     █")
        print("█        Wpisz 'Quit' aby zakończyć grę               █")
        print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
        print("")
        operation = input("Wybierz opcję z menu: ")

        if operation.isdigit() and int(operation) == 1:
            return [player_1_settings, player_2_settings, player_1_name, player_2_name]

        elif operation.isdigit() and int(operation) == 2:

            while int(player_config_operation)!=3:
                clear()
                print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
                print("█                                                     █")
                print("█      Konfiguracja ustawień dla "+ player_1_name + fill_space(21, player_1_name, "") + "█", sep="")
                print("█                                                     █")
                print("█      1. Nickname                                    █")
                print("█      2. Czy Player_1 jest człowiekiem czy AI        █")
                print("█      3. Powrót do menu                              █")
                print("█                                                     █")
                print("█        Wpisz 'Quit' aby zakończyć grę               █")
                print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                print("")

                player_config_operation = input("Podaj opcje ustawień: ")

                if player_config_operation.isdigit() and int(player_config_operation) == 1:
                    player_1_name = input("Podaj nick dla Player_1: ")

                elif player_config_operation.isdigit() and int(player_config_operation) == 2:
                    clear()
                    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
                    print("█                                                     █")
                    print("█      Konfiguracja ustawień dla "+ player_1_name + fill_space(21, player_1_name, "") + "█", sep="")
                    print("█                                                     █")
                    print("█      1. Człowiek                                    █")
                    print("█      2. AI poziom łatwy                             █")
                    print("█      3. AI poziom średni                            █")
                    print("█      4. AI poziom trudny                            █")
                    print("█                                                     █")
                    print("█        Wpisz 'Quit' aby zakończyć grę               █")
                    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                    print("")
                    player_1_settings = int(input("Wybierz opcje kim jest Player_1: "))

                elif not player_config_operation.isdigit() and player_config_operation == "quit":
                    print ("Koniec gry")
                    sys.exit(0)

        elif operation.isdigit() and int(operation) == 3:

            while int(player_config_operation)!=3:
                clear()
                print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
                print("█                                                     █")
                print("█      Konfiguracja ustawień dla "+ player_2_name + fill_space(21, player_2_name, "") + "█", sep="")
                print("█                                                     █")
                print("█      1. Nickname                                    █")
                print("█      2. Czy Player_2 jest człowiekiem czy AI        █")
                print("█      3. Powrót do menu                              █")
                print("█                                                     █")
                print("█        Wpisz 'Quit' aby zakończyć grę               █")
                print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                print("")
                player_config_operation = input("Podaj opcje ustawień: ")

                if int(player_config_operation) == 1:
                    player_2_name = input("Podaj nick dla Player_2: ")

                elif int(player_config_operation) == 2:
                    clear()
                    print("▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
                    print("█                                                     █")
                    print("█      Konfiguracja ustawień dla "+ player_2_name + fill_space(21, player_2_name, "") + "█", sep="")
                    print("█                                                     █")
                    print("█      1. Człowiek                                    █")
                    print("█      2. AI poziom łatwy                             █")
                    print("█      3. AI poziom średni                            █")
                    print("█      4. AI poziom trudny                            █")
                    print("█                                                     █")
                    print("█        Wpisz 'Quit' aby zakończyć grę               █")
                    print("▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀")
                    print("")
                    player_2_settings = int(input("Wybierz opcje kim jest Player_2: "))

                elif not player_config_operation.isdigit() and player_config_operation == "quit":
                    print ("Koniec gry")
                    sys.exit(0)

        elif isinstance(operation, str) and operation.lower()=="quit":
            print ("Koniec gry")
            sys.exit(0)