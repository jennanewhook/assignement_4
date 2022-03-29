def new_board():
    empty_board = [
        [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' '],
        ['8', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '8'],
        ['7', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '7'],
        ['6', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '6'],
        ['5', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '5'],
        ['4', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '4'],
        ['3', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '3'],
        ['2', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '2'],
        ['1', ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], ['□', None], '1'],
        [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', ' ']
    ]
    return empty_board
    
def colour(board, square):
    row_j, column_k = (i for i in square)
    row = (ord(row_j) - 96)
    column = (9 - int(column_k))
    return board[column][row][1]
    
def count_pieces(board, colour):
    count = 0
    for i in board:
        for n in i:
            if n[1] == colour:
                count += 1
    return count

def piece(board, square):
    row_j, column_k = (i for i in square)
    row = (ord(row_j) - 96)
    column = (9 - int(column_k))
    
    return board[column][row][0]

def place_piece(board, square, colour, piece):
    row_j, column_k = (i for i in square)
    row = (ord(row_j) - 96)
    column = (9 - int(column_k))
    board[column][row] = [piece, colour]
    
def pretty(board):
    view_board = []
    for i in board:
        for n in i:
            r.append(n[0])
        view_board.append(r)
        
    for i in view_board:
        print(' '.join(i))
        
        

            