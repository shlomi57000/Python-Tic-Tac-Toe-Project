
# פונקציה להצגת הלוח בכל זמן נתון
def Show_Tic():
    for i in range(len(tic)):
        print(' \n ---+---+--- ')
        for x in range(len(tic[i])):
            print(f'| {tic[i][x]} ',end='')
        print('|', end='')
    print(' \n ---+---+--- ')

# פונקציה לקבלת ערכי שורה ועמודה מהמשתמש

def Enter(symbol):
    print('player:')
    row = input('please enter row number : ')
    while row != 0 and row != 1 and row != 2 :
        row = input('wrong input ,please enter row number again: ')


    column = int(input('please enter column number : '))
    while column != 0 and column != 1 and column != 2 :
        column = int(input('wrong number,please enter column number again: '))
    tic[row][column] = symbol


# פונקציה לבחירת סמל המשחק
def choose_symbol ():
    choose = ''
    while choose !=  'y' and choose != 'Y' and choose != 'n' and choose != 'N':
        print('Want to manually choose your player symbol ? [y/n]')
        choose = input()
        symbol = ''
        if choose == 'y' or choose == 'Y':
            while symbol != 'X' and symbol != 'x' and symbol != 'O' and symbol != 'o' :
                print('choose your player symbol --> [X\O]')
                symbol = input()
            return symbol.upper()

# פונקציה לבדיקת מה הסמל שהתקבל ומחזירה את השני
def check_symbol (symbol) :
    if symbol == 'X' or symbol == 'x':
        return 'O'
    else:
        return 'X'
#פונקציה לבדיקת ניצחון באיקס עיגול
def check_win (tic) :
    for i in tic:
        print(i)
        if i.count('X') == len(tic):
            return 1
        elif i.count('O') == len(tic):
            return 1
        else:
            return 0

    for x in range(len(tic)):
        for i in range(len(tic[x])-1):
             if tic[i][x] != tic[i+1][x] :
                 continue
             if tic[i][x] == tic[i + 1][x] and i+1 == len(tic)-1 :
                 return 1


def play_game (player1,player2,tic) :
    w = 0
    while w != 1:
        Enter(player1)
        w = check_win(tic)
        print(f'{w}')
        Show_Tic()
        if w == 1 :
            break
        Enter(player2)
        w = check_win(tic)
        print(f'{w}')
        Show_Tic()

#Flow

tic = [['_','_','_'],['_','_','_'],['_','_','_']]
import random
v = -1
while v < 0 or v > 4 :
    print(f'welcome ! , please select game mode : \n 1). 1V1 \n 2). 1Vcomp \n 3). compVcomp \n 4). exit game')
    v = int(input())
if v == 1 :
    print('player1 : ')
    player1 = choose_symbol()

    if player1 == None :
        print('player2 : ')
        player2 = choose_symbol()

        if player2 == None :
            player2 = random.choice(['X','O'])
            player1 = check_symbol(player2)
        else:
            player1 = check_symbol(player2)
    else:
        player2 = check_symbol(player1)
    print(f'player 1 your symbol  is {player1}')
    print(f'player 2 your symbol  is {player2}')
    play_game(player1, player2, tic)

elif v == 2:
    print()
elif v == 3 :
    print()
elif v == 4 :
    print('exiting game.....')

# print(tic[1][1])
