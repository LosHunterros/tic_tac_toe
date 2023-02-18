
def check_winning_move(board,symbol):

    for i in range(3):
        if board[i][0] == board[i][1] == symbol and board[i][2] == False:
            return (i, 2)
        if board[i][0] == board[i][2] == symbol and board[i][1] == False:
            return (i, 1)
        if board[i][1] == board[i][2] == symbol and board[i][0] == False:
            return (i, 0)
        if board[0][i] == board[1][i] == symbol and board[2][i] == False:
            return (2, i)
        if board[0][i] == board[2][i] == symbol and board[1][i] == False:
            return (1, i)
        if board[1][i] == board[2][i] == symbol and board[0][i] == False:
            return (0, i)

    if board[0][0] == board[1][1] == symbol and board[2][2] == False:
        return (2, 2)
    if board[0][0] == board[2][2] == symbol and board[1][1] == False:
        return (1, 1)
    if board[1][1] == board[2][2] == symbol and board[0][0] == False:
        return (0, 0)
    if board[0][2] == board[1][1] == symbol and board[2][0] == False:
        return (2, 0)
    if board[0][2] == board[2][0] == symbol and board[1][1] == False:
        return (1, 1)
    if board[1][1] == board[2][0] == symbol and board[0][2] == False:
        return (0, 2)

    return 0

def check_blocking_move(board,symbol):
    if symbol=='x':
        opposite='o'
    else:
        opposite='x'
    for i in range(3):
        if board[i][0] == board[i][1] == opposite and board[i][2] == False:
            return (i, 2)
        if board[i][0] == board[i][2] == opposite and board[i][1] == False:
            return (i, 1)
        if board[i][1] == board[i][2] == opposite and board[i][0] == False:
            return (i, 0)
        if board[0][i] == board[1][i] == opposite and board[2][i] == False:
            return (2, i)
        if board[0][i] == board[2][i] == opposite and board[1][i] == False:
            return (1, i)
        if board[1][i] == board[2][i] == opposite and board[0][i] == False:
            return (0, i)

    if board[0][0] == board[1][1] == opposite and board[2][2] == False:
        return (2, 2)
    if board[0][0] == board[2][2] == opposite and board[1][1] == False:
        return (1, 1)
    if board[1][1] == board[2][2] == opposite and board[0][0] == False:
        return (0, 0)
    if board[0][2] == board[1][1] == opposite and board[2][0] == False:
        return (2, 0)
    if board[0][2] == board[2][0] == opposite and board[1][1] == False:
        return (1, 1)
    if board[1][1] == board[2][0] == opposite and board[0][2] == False:
        return (0, 2)

    return 0

def check_fork(board,symbol):
    if ((board[0][2] or board[0][1])==symbol) and ((board[1][0] or board[2][0])==symbol) and board[0][0]==False:
        return (0,0)

    if ((board[0][0] or board[0][2])==symbol) and ((board[1][1] or board[2][1])==symbol) and board[0][1]==False:
        return (0,1)

    if ((board[0][0] or board[0][1])==symbol) and ((board[1][2] or board[2][2])==symbol) and board[0][2]==False:
        return (0,2)

    if ((board[0][0] or board[2][0])==symbol) and ((board[1][1] or board[1][2])==symbol) and board[1][0]==False:
        return (1,0)

    if ((board[0][1] or board[2][1])==symbol) and ((board[1][0] or board[1][2])==symbol) and board[1][1]==False:
        return (1,1)

    if ((board[0][2] or board[2][2])==symbol) and ((board[1][0] or board[1][1])==symbol) and board[1][2]==False:
        return (1,2)

    if ((board[0][0] or board[1][0])==symbol) and ((board[2][1] or board[2][2])==symbol) and board[2][0]==False:
        return (2,0)

    if ((board[0][1] or board[1][1])==symbol) and ((board[2][0] or board[2][2])==symbol) and board[2][1]==False:
        return (2,1)

    if ((board[0][2] or board[1][2])==symbol) and ((board[2][0] or board[2][1])==symbol) and board[2][2]==False:
        return (2,2)

    if ((board[0][1] or board[0][2])==symbol) and ((board[1][1] or board[2][2])==symbol) and board[0][0]==False:
        return (0,0)

    if ((board[1][0] or board[2][0])==symbol) and ((board[1][1] or board[2][2])==symbol) and board[0][0]==False:
        return (0,0)

    if ((board[0][0] or board[0][1])==symbol) and ((board[1][1] or board[2][1])==symbol) and board[0][2]==False:
        return (0,2)

    if ((board[1][2] or board[2][2])==symbol) and ((board[1][1] or board[2][1])==symbol) and board[0][2]==False:
        return (0,2) 

    if ((board[0][2] or board[1][2])==symbol) and ((board[1][1] or board[0][0])==symbol) and board[2][2]==False:
        return (2,2)

    if ((board[2][0] or board[2][1])==symbol) and ((board[1][1] or board[0][0])==symbol) and board[2][2]==False:
        return (2,2)  

    if ((board[0][0] or board[1][0])==symbol) and ((board[1][1] or board[0][2])==symbol) and board[2][0]==False:
        return (2,0) 

    if ((board[2][1] or board[2][2])==symbol) and ((board[1][1] or board[0][2])==symbol) and board[2][0]==False:
        return (2,0) 

    return 0

def check_fork_block(board,symbol):
    if symbol=='x':
        opposite='o'
    else:
        opposite='x'

    if ((board[0][2] or board[0][1])==opposite) and ((board[1][0] or board[2][0])==opposite) and board[0][0]==False:
        return (0,0)

    if ((board[0][0] or board[0][2])==opposite) and ((board[1][1] or board[2][1])==opposite) and board[0][1]==False:
        return (0,1)

    if ((board[0][0] or board[0][1])==opposite) and ((board[1][2] or board[2][2])==opposite) and board[0][2]==False:
        return (0,2)

    if ((board[0][0] or board[2][0])==opposite) and ((board[1][1] or board[1][2])==opposite) and board[1][0]==False:
        return (1,0)

    if ((board[0][1] or board[2][1])==opposite) and ((board[1][0] or board[1][2])==opposite) and board[1][1]==False:
        return (1,1)

    if ((board[0][2] or board[2][2])==opposite) and ((board[1][0] or board[1][1])==opposite) and board[1][2]==False:
        return (1,2)

    if ((board[0][0] or board[1][0])==opposite) and ((board[2][1] or board[2][2])==opposite) and board[2][0]==False:
        return (2,0)

    if ((board[0][1] or board[1][1])==opposite) and ((board[2][0] or board[2][2])==opposite) and board[2][1]==False:
        return (2,1)

    if ((board[0][2] or board[1][2])==opposite) and ((board[2][0] or board[2][1])==opposite) and board[2][2]==False:
        return (2,2)

    if ((board[0][1] or board[0][2])==opposite) and ((board[1][1] or board[2][2])==opposite) and board[0][0]==False:
        return (0,0)

    if ((board[1][0] or board[2][0])==opposite) and ((board[1][1] or board[2][2])==opposite) and board[0][0]==False:
        return (0,0)

    if ((board[0][0] or board[0][1])==opposite) and ((board[1][1] or board[2][1])==opposite) and board[0][2]==False:
        return (0,2)

    if ((board[1][2] or board[2][2])==opposite) and ((board[1][1] or board[2][1])==opposite) and board[0][2]==False:
        return (0,2) 

    if ((board[0][2] or board[1][2])==opposite) and ((board[1][1] or board[0][0])==opposite) and board[2][2]==False:
        return (2,2)

    if ((board[2][0] or board[2][1])==opposite) and ((board[1][1] or board[0][0])==opposite) and board[2][2]==False:
        return (2,2)  

    if ((board[0][0] or board[1][0])==opposite) and ((board[1][1] or board[0][2])==opposite) and board[2][0]==False:
        return (2,0) 

    if ((board[2][1] or board[2][2])==opposite) and ((board[1][1] or board[0][2])==opposite) and board[2][0]==False:
        return (2,0) 

    return 0

def center(board):
    if board[1][1]==False:
        return (1,1)
    else:
        return 0

def emptyLine(board,symbol):
    if board[0][0]==symbol and board[0][1]==board[0][2]==False:
        return(0,2)
    elif board[0][1]==symbol and board[0][0]==board[0][2]==False:
        return(0,2)
    elif board[0][2]==symbol and board[0][0]==board[0][1]==False:
        return(0,0)
    elif board[1][0]==symbol and board[1][1]==board[1][2]==False:
        return(1,1)
    elif board[1][1]==symbol and board[1][0]==board[1][2]==False:
        return(1,0)
    elif board[1][2]==symbol and board[1][0]==board[1][1]==False:
        return(1,1)
    elif board[2][0]==symbol and board[2][1]==board[2][2]==False:
        return(2,2)
    elif board[2][1]==symbol and board[2][0]==board[2][2]==False:
        return(2,2)
    elif board[2][2]==symbol and board[2][0]==board[2][1]==False:
        return(2,0)
    
    return 0

def oppositeCorner(board,symbol):
    if symbol=='x':
        opposite='o'
    else:
        opposite='x'
    if board[0][0]==opposite and board[2][2]==False:
        return (2,2)
    elif board[0][2]==opposite and board[2][0]==False:
        return (2,0)
    elif board[2][2]==opposite and board[0][0]==False:
        return (0,0)
    elif board[2][0]==opposite and board[0][2]==False:
        return (0,2)
    else:
        return 0

def emptyCorner(board):
    if board[2][2]==False:
        return (2,2)
    elif board[2][0]==False:
        return (2,0)
    elif board[0][0]==False:
        return (0,0)
    elif board[0][2]==False:
        return (0,2)
    else:
        return 0

def emptySide(board):
    if board[0][1]==False:
        return (0,1)
    elif board[1][2]==False:
        return (1,2)
    elif board[2][1]==False:
        return (2,1)
    elif board[0][1]==False:
        return (0,1)
    else:
        return 0

def get_unbeatable_ai_coordinates_hard(board,symbol):
    if check_winning_move(board,symbol):
        return check_winning_move (board,symbol)
    elif check_blocking_move(board,symbol):
        return check_blocking_move(board,symbol)
    elif check_fork(board,symbol):
        return check_fork(board,symbol)
    elif check_fork_block(board,symbol):
        return check_fork_block(board,symbol)
    elif center(board):
        return center(board)
    elif emptyLine(board,symbol):
        return emptyLine(board,symbol)
    elif oppositeCorner(board,symbol):
        return oppositeCorner(board,symbol)
    elif emptyCorner(board):
        return emptyCorner(board)
    elif emptySide(board):
        return emptySide(board)
