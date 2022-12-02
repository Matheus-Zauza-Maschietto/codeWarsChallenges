"""
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:
We want our function to return:

-1 if the board is not yet finished AND no one has won yet (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
"""

def is_solved(board):
    has_empty_square = False

    for linha in range(3):
        if 0 not in board[linha]:
            match sum(board[linha]):
                case 3:
                    return 1
                case 6:
                    return 2
        else:
            has_empty_square = True

    for coluna in range(3):
        if 0 not in [board[0][coluna], board[1][coluna], board[2][coluna]]:
            match sum([board[0][coluna], board[1][coluna], board[2][coluna]]):
                case 3:
                    return 1
                case 6:
                    return 2

    diag1, diag2 = 0, 0
    for diagonal in range(3):
        if board[diagonal][diagonal] != 0:
            diag1 += board[diagonal][diagonal]
        else:
            diag1 = 0

        if board[2-diagonal][2-diagonal] != 0:
            diag2 += board[2-diagonal][2-diagonal]
        else:
            diag2 = 0
    
    if diag1 == 3 or diag2 == 3:
        return 1
    elif diag1 == 6 or diag2 == 6:
        return 2

    if has_empty_square:
        return -1
    return 0

print(is_solved([[0, 0, 1],
                 [0, 1, 2],
                 [2, 1, 0]]))