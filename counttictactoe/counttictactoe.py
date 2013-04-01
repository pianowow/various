from copy import copy

#goal: count how many distinct games of tic tac toe can exist
#secondary goal: assuming X goes first, how many does X win, O win, are drawn?
#ignore rotational/reflective symmetry
#at most nine moves, 5 by X, 4 by O

#need structure to represent the state of a board
board = [0, 0, 0,
         0, 0, 0,
         0, 0, 0] #all empty

#I'll represent X with 1 and O with -1 (this makes determining whose move it is easier)

#need function to determine whose turn it is
def whose_turn(board):
    if sum(board) == 0:
        return 1
    else:
        return -1

#need structure to represent a move
move = 3 #mark the third space with whoever's turn it is

#want a funciton to print a board pretty
def print_board(board):
    line = ''
    player = 'X'
    for i,space in enumerate(board):
        if space == 0:
            player = ' '
        elif space == 1:
            player = 'X'
        elif space == -1:
            player = 'O'
        if i%3 == 2:
            line = line + ' '+ player
            print(line)
            if i != 8:
                print('------------')
            line = ''
        else:
            line = line + ' '+ player + ' |'

#need function to make a move
def make_move(board, move):
    newboard = copy(board)
    player = whose_turn(newboard)
    if newboard[move] == 0:
        newboard[move] = player
    #print_board(board)
    return newboard

#need funciton to get a list of legal moves
def moves(board):
    movelist = []
    for i,space in enumerate(board):
        if space == 0:
            movelist.append(i)
    return movelist

#need to know if the game is over.  Returns 1 for X wins, -1 for O wins, 0 for game still going, .5 for draw
def game_status(board):
    #horizontal top
    if board[0] != 0 and board[0] == board[1] and board[0] == board[2]:
        return board[0]
    #horizontal middle
    if board[3] != 0 and board[3] == board[4] and board[3] == board[5]:
        return board[3]
    #horizontal bottom
    if board[6] != 0 and board[6] == board[7] and board[6] == board[8]:
        return board[6]
    #vertical left
    if board[0] != 0 and board[0] == board[3] and board[0] == board[6]:
        return board[0]
    #vertical middle
    if board[1] != 0 and board[1] == board[4] and board[1] == board[7]:
        return board[1]
    #vertical right
    if board[2] != 0 and board[2] == board[5] and board[2] == board[8]:
        return board[2]
    #diagonal 1
    if board[0] != 0 and board[0] == board[4] and board[0] == board[8]:
        return board[0]
    #diagonal 2
    if board[2] != 0 and board[2] == board[4] and board[2] == board[6]:
        return board[2]
    #if we got this far the game is either a draw or still going
    if moves(board):
        return 0 #more moves exist, game still going
    else:
        return .5 #list empty, game drawn

number_of_games = 0
x_wins = 0
o_wins = 0
draws = 0
number = 0
#need funciton to record results
def record_result(status):
    global number_of_games
    global x_wins
    global o_wins
    global draws
    global number
    number += 1
    if status != 0:
        number_of_games += 1
    if status == 1:
        x_wins += 1
    if status == -1:
        o_wins += 1
    if status == .5:
        draws += 1

#step through games (earliest win can happen after move 5)
for move1 in moves(board):
    board1 = make_move(board,move1)
    for move2 in moves(board1):
        board2 = make_move(board1,move2)
        for move3 in moves(board2):
            board3 = make_move(board2,move3)
            for move4 in moves(board3):
                board4 = make_move(board3,move4)
                for move5 in moves(board4):
                    board5 = make_move(board4,move5)
                    status5 = game_status(board5) #x could win here
                    record_result(status5)
                    if status5 == 0:
                        for move6 in moves(board5):
                            board6 = make_move(board5, move6)
                            status6 = game_status(board6) #o could win here
                            record_result(status6)
                            if status6 == 0:
                                for move7 in moves(board6):
                                    board7 = make_move(board6, move7)
                                    status7 = game_status(board7) #x could win here
                                    record_result(status7)
                                    if status7 == 0:
                                        for move8 in moves(board7):
                                            board8 = make_move(board7, move8)
                                            status8 = game_status(board8)
                                            record_result(status8) #o could win here
                                            if status8 == 0:
                                                for move9 in moves(board8):
                                                    board9 = make_move(board8, move9)
                                                    status9 = game_status(board9)
                                                    record_result(status9) #x could win, or draw here

print('x wins '+str(x_wins)+' times')
print('o wins '+str(o_wins)+' times')
print('draw '+str(draws)+' times')
print('number checked: '+str(number))
print('number of games: '+str(number_of_games))

print('362880 is 9!')