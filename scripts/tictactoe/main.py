from __future__ import print_function
from sys import stdout
import random
import time
global board
board = ['z', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
global unit
global comp_unit
unit = str(input("Choose Your Symbol( 1 or 0 ) : "))
if unit == '1':
    comp_unit = '0'
else:
    comp_unit = '1'

print("Places are corresponding to your KeyPad")
"""unit= random.choice('X 0'.split())
if unit =='X':
    comp_unit='0'
else:
    comp_unit= 'X'"""


def board_print():

    bo = '''
 %s | %s | %s
 ---------
 %s | %s | %s
 ---------
 %s | %s | %s
 ---------''' % (board[7], board[8], board[9], board[4], board[5], board[6], board[1], board[2], board[3])

    print(bo)


def victory(var):
    bo = board
    end = False
    if (bo[1] == var and bo[2] == var and bo[3] == var):
        end = True
    elif (bo[4] == var and bo[5] == var and bo[6] == var):
        end = True
    elif (bo[7] == var and bo[8] == var and bo[9] == var):
        end = True
    elif (bo[1] == var and bo[4] == var and bo[7] == var):
        end = True
    elif (bo[2] == var and bo[5] == var and bo[8] == var):
        end = True
    elif (bo[3] == var and bo[6] == var and bo[9] == var):
        end = True
    elif (bo[1] == var and bo[5] == var and bo[9] == var):
        end = True
    elif (bo[3] == var and bo[5] == var and bo[7] == var):
        end = True
    return end


def enter(a, pos):
    board[pos] = a
    board_print()


def comp_enter():
    cvic = 0
    for i in range(1, 10):
        if board[i] == ' ':
            board[i] = comp_unit
            if victory(comp_unit):
                cvic = 1
                break
            else:
                board[i] = ' '
            board[i] = unit
            if victory(unit):
                board[i] = comp_unit
                cvic = 1
                break
            else:
                board[i] = ' '

    if cvic != 1:
        if board[5] == ' ':
            board[5] = comp_unit
        else:
            if (board[1] == ' ' or board[3] == ' ' or board[7] == ' ' or board[9] == ' ') and ((board[1] != unit and board[9] != unit)and(board[3] != unit and board[7] != unit)):
                ran1 = int(random.sample([1, 3, 7, 9], 1)[0])
                while board[ran1] != ' ':
                    ran1 = int(random.sample([1, 3, 7, 9], 1)[0])
                board[ran1] = comp_unit
            else:
                ran1 = int(random.sample([2, 4, 5, 6, 8], 1)[0])
                while board[ran1] != ' ':
                    ran1 = int(random.sample([2, 4, 5, 8], 1)[0])
                board[ran1] = comp_unit


while ' ' in board:
    pos = int(input('Enter where to place your %s : ' % (unit)))
    while board[pos] != ' ':
        print('This place already has a value')
        pos = int(input('Enter where to place your %s : ' % (unit)))
    enter(unit, pos)
    end = victory(unit)
    if end == True:
        print("Player wins")
        break
    if ' ' in board:
        comp_enter()
        print("Computer's move.....")
        t = 3
        while t > 0:
            stdout.write("\r%d" % t)
            stdout.flush()
            time.sleep(1)
            t -= 1
        print('\n')
        board_print()
        if victory(comp_unit):
            print("Computer wins")
            break

else:
    print('Game Over , Its a draw')
