import os
import time
import random


def welcome():
    for i in range(0, 11):
        print("-", end="")
    print()
    print("- ДОБРО ПОЖАЛОВАТЬ В ИГРУ ДИЛОВАРА -", end="")
    print()
    for i in range(0, 11):
        print("-", end="")
    print()
    input("Нажмите ENTER, чтобы начать\n")
    option()


def option():
    for i in range(0, 21):
        print("-", end="")
    print()
    print("1)Камень Ножницы Бумага\n2)Крестики-нолики")
    for i in range(0, 21):
        print("-", end="")
    print()
    chc = int(input("Введите номер вашего выбора: "))
    if chc == 1:
        stonepaperscissor()
    elif chc == 2:
        tictactoemenu()
    else:
        welcome()


def stonepaperscissor():
    print("КАМЕНЬ, НОЖНИЦЫ, БУМАГА")
    print("Вы будете соревноваться с компьютером")
    print("Участник, первым набравший 5 очков, объявляется победителем.")
    print("Для камня введите 0")
    print("Для бумаги введите 1")
    print("Для ножниц введите 2")
    print("Чтобы завершить игру и вернуться в главное меню, введите -1")
    user = 0
    comp = 0
    cnt = 0
    choice_play = ["Камень", "Ножницы", "Бумага"]
    while user < 5 and comp < 5 and cnt < 25:
        cnt += 1
        a = int(input("Введите свой выбор ="))
        for i in range(0, 20):
            print("*", end="")
        print()
        if a == -1:
            print("Спасибо за игру!")
            welcome()
            break
        b = random.choice([0, 1, 2])
        if a == 0 and b == 1:
            comp += 1
        elif a == 0 and b == 2:
            user += 1
        elif a == 1 and b == 0:
            user += 1
        elif a == 1 and b == 2:
            comp += 1
        elif a == 2 and b == 0:
            comp += 1
        elif a == 2 and b == 1:
            user += 1
        print("Вы:", choice_play[a])
        print("Компьютер:", choice_play[b])
        print("Результаты")
        print("Вы=", user, "\t Компьютер=", comp)
        for i in range(0, 20):
            print("*", end="")
        print()
        if(user > comp and user == 5):
            print("Поздравляем!! Вы Победитель!")
        elif(user < comp and comp == 5):
            print("Не повезло, приходите еще!")
        elif(user == comp and cnt >= 25):
            print("Ничья")


def tictactoemenu():
    print("Добро пожаловать в крестики-нолики")
    for i in range(0, 21):
        print("-", end="")
    print()
    print("1)Два игрока\n2)Один игрок")
    for i in range(0, 21):
        print("-", end="")
    print()
    chc = int(input("Введите номер: "))
    if chc == 1:
        two_player()
    elif chc == 2:
        single_player()
    else:
        option()


def two_player():
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def rules():
        print("Добро пожаловать в крестики-нолики")
        print("Это игра для двух игроков, где USER1 — это X, а USER2 — это O.")
        print("Введите свой вариант от 1 до 9")
        print("""
                1 | 2 | 3
                ---|---|---
                4 | 5 | 6
                ---|---|---
                7 | 8 | 9
                """)

    def print_board():
        print("   |   |   ")
        print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
        print("   |   |   ")

    def is_winner(board, player):
        if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
                (board[3] == player and board[5] == player and board[7] == player):
            return True
        else:
            return False

    def is_board_full(board):
        if " " in board:
            return False
        else:
            return True

    while True:
        os.system("очистить")
        rules()
        print_board()

        # user 1
        choice = input("Выберите пустое место для X: ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print("Место уже занято")
            time.sleep(1)
        # for user 1 to win
        if is_winner(board, "X"):
            os.system("очистить")
            rules()
            print_board()
            print("USER1 Выиграл")
            break

        os.system("очистить")
        rules()
        print_board()

        if is_board_full(board):
            print("Ничья")
            break

        # user 2
        choice = input("Выберите пустое место для O: ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "O"
        else:
            print("Место уже занято")
            time.sleep(1)
        # for user 2 to win
        if is_winner(board, "O"):
            os.system("очистить")
            rules()
            print_board()
            print("USER2 Выиграл")
            break

        if is_board_full(board):
            print("Ничья")
            break


def single_player():
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def rules():
        print("Добро пожаловать в крестики-нолики")
        print("Это одиночная игра, в которой вы X, а компьютер O.")
        print("Введите свой вариант от 1 до 9")
        print("""
                1 | 2 | 3
                ---|---|---
                4 | 5 | 6
                ---|---|---
                7 | 8 | 9
                """)

    def print_board():
        print("   |   |   ")
        print(" "+board[1]+" | "+board[2]+" | "+board[3]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[4]+" | "+board[5]+" | "+board[6]+" ")
        print("   |   |   ")
        print("---|---|---")
        print("   |   |   ")
        print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
        print("   |   |   ")

    def is_winner(board, player):
        if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
                (board[3] == player and board[5] == player and board[7] == player):
            return True
        else:
            return False

    def is_board_full(board):
        if " " in board:
            return False
        else:
            return True

    def get_computer_move(board, player):

        # check for a win
        for i in range(1, 10):
            if board[i] == " ":
                board[i] = player
                if is_winner(board, player):
                    return i
                else:
                    board[i] = " "

        # проверка блока столбцов
        for i in [1, 2, 3]:
            if board[i] == "X" and board[i+3] == "X" and board[i+6] == " ":
                return i+6
            if board[i+3] == "X" and board[i+6] == "X" and board[i] == " ":
                return i
            if board[i] == "X" and board[i+6] == "X" and board[i+3] == " ":
                return i+3

        # проверка блока строк
        for i in [1, 4, 7]:
            if board[i] == "X" and board[i+1] == "X" and board[i+2] == " ":
                return i+2
            if board[i+1] == "X" and board[i+2] == "X" and board[i] == " ":
                return i
            if board[i] == "X" and board[i+2] == "X" and board[i+1] == " ":
                return i+1

        # проверка диагонального блока
        if board[1] == "X" and board[5] == "X" and board[9] == " ":
            return 9
        if board[9] == "X" and board[5] == "X" and board[1] == " ":
            return 1
        if board[1] == "X" and board[9] == "X" and board[5] == " ":
            return 5
        if board[3] == "X" and board[5] == "X" and board[7] == " ":
            return 7
        if board[7] == "X" and board[5] == "X" and board[3] == " ":
            return 3
        if board[3] == "X" and board[7] == "X" and board[5] == " ":
            return 5

        if board[5] == " ":
            return 5
        while True:
            move = random.randint(1, 9)
            if board[move] == " ":
                return move
            return 5

    while True:
        os.system("очистить")
        rules()
        print_board()

        # user 1
        choice = input("Выберите пустое место для X: ")
        choice = int(choice)
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print("Место уже занято")
            time.sleep(1)
        # for user 1 to win
        if is_winner(board, "X"):
            os.system("очистить")
            rules()
            print_board()
            print("Поздравляем! Вы выиграли!")
            break

        os.system("очистить")
        rules()
        print_board()

        if is_board_full(board):
            print("Ничья")
            break

        # user 2
        choice = get_computer_move(board, "O")
        if board[choice] == " ":
            board[choice] = "O"
        else:
            print("Место уже занято")
            time.sleep(1)
        # for user 2 to win
        if is_winner(board, "O"):
            os.system("очистить")
            rules()
            print_board()
            print("КОМПЬЮТЕР побеждает!")
            break

        if is_board_full(board):
            print("Ничья")
            break


welcome()
print("\n")
option()
