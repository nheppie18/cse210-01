"""
Author: Nate Hepworth
Tic-Tac-Toe Assignment
"""

def make_board():
    board = []
    for tile in range(9):
        board.append(tile)
    return board

def display_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+--+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+--+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def player_turn(player, board):
    tile = int(input(f"Player {player} please choose a tile (0-8): "))
    board[tile] = player

def player_switch(player):
    if player == "o":
        return "x"
    elif player == "x":
        return "o"

def winner(board):
    if (board[0] == board[1] == board[2]):
        winner = board[0]
    elif (board[3] == board[4] == board[5]):
        winner = board[3]
    elif (board[6] == board[7] == board[8]):
        winner = board[6]
    elif (board[0] == board[3] == board[6]):
        winner = board[0]
    elif (board[1] == board[4] == board[7]):
        winner = board[1]
    elif (board[2] == board[5] == board[8]):
        winner = board[2]
    elif (board[0] == board[4] == board[8]):
        winner = board[4]
    elif (board[2] == board[4] == board[6]):
        winner = board[2]
        return winner

def main():
    player = player_switch("o")
    board = make_board()
    count = 0
    while count != 9 or not winner(board):
        display_board(board)
        player_turn(player, board)
        player = player_switch(player)
        count += 1
    display_board(board)
    print("Game Over")

if __name__ == "__main__":
    main()
