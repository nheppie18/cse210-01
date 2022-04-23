"""
Author: Nate Hepworth
Tic-Tac-Toe Assignment
"""
game_continues = True
winner = None
def make_board():
    board = []
    for tile in range(1, 10):
        board.append(tile)
    return board

def display_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def player_turn(player, board):
    tile = int(input(f"Player {player} please choose a tile (1-9): "))
    while tile >= 10:
        tile = int(input("Please choose a number between 1-9: "))
    while board[tile - 1] == 'x' or board[tile - 1] == 'o':
        tile = int(input("Tile is already taken please choose a different one (1-9):"))
    board[tile - 1] = player

def player_switch(player):
    if player == "o":
        return "x"
    elif player == "x":
        return "o"

def check_winner(board):
    global winner
    global game_continues
    if (board[0] == board[1] == board[2]):
        winner = board[0]
        game_continues = False
    elif (board[3] == board[4] == board[5]):
        winner = board[3]
        game_continues = False
    elif (board[6] == board[7] == board[8]):
        winner = board[6]
        game_continues = False
    elif (board[0] == board[3] == board[6]):
        winner = board[0]
        game_continues = False
    elif (board[1] == board[4] == board[7]):
        winner = board[1]
        game_continues = False
    elif (board[2] == board[5] == board[8]):
        winner = board[2]
        game_continues = False
    elif (board[0] == board[4] == board[8]):
        winner = board[4]
        game_continues = False
    elif (board[2] == board[4] == board[6]):
        winner = board[2]
        game_continues = False
    else:
        winner = None
        game_continues = True
    return winner

def check_if_game_end(board):
    check_winner(board)
    check_tie()
count = 0
def check_tie():
    global game_continues
    global count
    count += 1
    if count == 9:
        game_continues = False
        print("Tie!")
    return

def main():
    player = player_switch("x")
    board = make_board()
    while game_continues:
        player = player_switch(player)
        display_board(board)
        player_turn(player, board)
        check_if_game_end(board)
    display_board(board)
    if winner != None:
        print(f"Player {winner} has won this round!")
    print("Game Over")

if __name__ == "__main__":
    main()
