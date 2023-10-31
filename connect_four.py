#Trinity Saunders
#10/3/2023
#CONNECT 4 LAB
#help from TA Lucas Mach in office hrs zoom

#asking the user for what the height and length of the board


def empty_board(): #board without any chips
    print("\n- - - - -\n- - - - -\n- - - - -\n- - - - -\n")
    pass



def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board[i][j], end=" ")
        print()
    print()


def initialize_board(num_rows, num_cols):
    return [["-" for _ in range(num_cols)] for _ in range(num_rows)]
    pass

def insert_chip(board, col, chip_type): #prompts for a chip to be given and places it on the board
    row = len(board) - 1
    for i in range(len(board) - 1, -1, -1):
        if board[i][col] == "-":
            board[i][col] = chip_type
            row = i
            break
    return row
    pass

def check_if_winner(board, col, row, chip_type):
    count = 0
    for j in range(len(board[0])):
        if board[row][j] == chip_type:
            count += 1
            if count == 4:
                return True # if someone has won
        else:
            count = 0
    count = 0
    for i in range(len(board)):
        if board[i][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0


    return False #if theres no winnter yet


def draw_game_yes(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '-':
                return False
    return True

if __name__ =="__main__":



    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))

    board = initialize_board(num_rows, num_cols)
    print_board(board)  # print board to console
    print("Player 1: x ")
    print("Player 2: o\n")

    player1_token = "x"
    player2_token = "o"

    game_playrun= False
    while not game_playrun:
        res = False
        print("Player 1: Which column would you like to choose?")
        col = int(input())
        row = insert_chip(board, col, player1_token)
        print_board(board)

        res = check_if_winner(board, col, row, player1_token) #cheks for winner
        if res:
            print("\nPlayer 1 won the game!")    #check if no winner/draw
            break






        draw_game = draw_game_yes(board)
        if draw_game:                                                #draw game message
            print("\nDraw. Nobody wins.")
            break


        print("Player 2: Which column would you like to choose?")       #player 2 pick
        col = int(input())
        row = insert_chip(board, col, player2_token)
        print_board(board)

        #check to see if player 2 won the game
        res = check_if_winner(board, col, row, player2_token)
        if res:
            print("\nPlayer 2 won the game!")
            break


        #check if no winner/draw
        draw_game = draw_game_yes(board)
        if draw_game:
            print("\nDraw. Nobody wins.")        #check if no winner/draw
            break