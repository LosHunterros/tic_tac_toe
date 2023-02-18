import copy as cp

class Cell:
    def __init__(self, location, max_val):
        self.location = location 
        self.max_val = max_val

def check_horizontal(board, row, sign):
     
    sign = sign
    if sign=='o':
        opposed='x'
    else:
        opposed='o'
    v = 0
    unfilled = 0
    for i in range(3): 
        if board[row][i] != opposed:
            unfilled += 1
            if board[row][i] == sign:
                v += 1
    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v
    
def check_vertical(board, col,sign):
    sign = sign
    if sign=='o':
        opposed='x'
    else:
        opposed='o'
    v = 0
    unfilled = 0
    for i in range(3): 
        if board[i][col] != opposed:
            unfilled += 1
            if board[i][col] == sign:
                v += 1
    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def left_diagonal(board, row, col,sign):
    sign = sign
    if sign=='o':
        opposed='x'
    else:
        opposed='o'
    v = 0
    unfilled = 0
    if row == col:
        for i in range(3):
            if board[i][i] != opposed:
                unfilled += 1
                if board[i][i] == sign:
                    v += 1
    if unfilled == 3:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v


def right_diagonal(board, row, col,sign):
    sign = sign
    if sign=='o':
        opposed='x'
    else:
        opposed='o'
    v = 0
    unfilled = 0
    state = False
    for i in range(len(board)):
        if board[i][abs(i-2)] == board[row][col]:
            state = True
        if board[i][abs(i-2)] != opposed:
            unfilled += 1
            if board[i][abs(i-2)] == sign:
                v +=1
    if unfilled == 3 and state == True:
        if v == 2:
            v = 10
        else:
            v += 1
    elif unfilled < 3:
        v = 0
    return v

def max_val(board, location,sign):
    maxval=0
    if board[location[0]][location[1]] != 'o' and board[location[0]][location[1]] != 'x':
        maxval += check_horizontal(board, location[0],sign) 
        maxval += check_vertical(board, location[1],sign) 
        maxval += left_diagonal(board, location[0], location[1],sign)
        maxval += right_diagonal(board, location[0], location[1],sign)
    
    return maxval

def get_unbeatable_ai_coordinates(board,sign):
    uboard = cp.deepcopy(board)
    for i in range(len(uboard)):
        for j in range(len(uboard[i])):
            if uboard[i][j] != 'x' and uboard[i][j] != 'o':
                uboard[i][j] = Cell([i,j], 0)
                uboard[i][j].max_val = max_val(board, [i, j],sign)
    coordinates=[]
    maximum=0
    for i in range(len(uboard)):
        for j in range(len(uboard[i])):
            if uboard[i][j] != 'x' and uboard[i][j] != 'o' and maximum<= uboard[i][j].max_val:
                maximum=uboard[i][j].max_val
                coordinates=uboard[i][j].location

    return coordinates
