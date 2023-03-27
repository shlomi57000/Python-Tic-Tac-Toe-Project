# פונקציה להצגת הלוח בכל זמן נתון
def Show_Tic(tic):
    if len(tic) == 3 :
        for i in range(len(tic)):
            print(' \n ---+---+--- ')
            for x in range(len(tic[i])):
                print(f'| {tic[i][x]} ', end='')
            print('|', end='')
        print(' \n ---+---+--- ')
    if len(tic) == 4 :
        for i in range(len(tic)):
            print(' \n ---+---+---+--- ')
            for x in range(len(tic[i])):
                print(f'| {tic[i][x]} ', end='')
            print('|', end='')
        print(' \n ---+---+---+--- ')


# פונקציה לקבלת ערכי שורה ועמודה מהמשתמש ועדכון העמודה בבורד
def Enter(tic,symbol):
    print(f'player with symbol {symbol} , it is your turn,')
    row = input('please enter row number : ')
    while not row.isdigit() or (int(row) < 0 or int(row) > len(tic)-1)  :
        row = input('wrong input ,please enter row number again: ')
    row = int(row)

    column = input('please enter column number : ')
    while not column.isdigit() or (int(column) < 0 or int(column) > len(tic)-1)  :
        column = input('wrong number,please enter column number again: ')
    column = int(column)

    if tic[row][column] != "_" :
        print(f'\noops , this cell ({[row,column]}) is taken please choose another one')
        Enter(tic,symbol)
    else:
        tic[row][column] = symbol

# פונקציית מהלך משחק של מחשב
def Enter_Comp(tic,symbol):
    print(f'player with symbol {symbol} , it is your turn,')
    row = random.choice(range(len(tic)))
    column = random.choice(range(len(tic)))
    if tic[row][column] != "_" :
        print(f'oops , this cell ({[row,column]}) is taken please choose another one')
        Enter_Comp(tic,symbol)
    else:
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
def check_win (tic,symbol) :
    # check rows
    for i in tic:
        if i.count(symbol) == len(tic):
            return 1

    # check columns
    for x in range(len(tic)):
        check_col = []
        for y in range(len(tic[x])):
             check_col.append(tic[y][x])
        if check_col.count(symbol) == len((tic[x]))  :
            return 1

    # check diagonal
    diag = []
    for i in range(len(tic)) :
        diag.append(tic[i][i])
    if diag.count(symbol) == len(tic) :
        return 1

    #check other diagonal
    diag =[]
    for i in range(len(tic)) :
        diag.append(tic[i][len(tic)-1-i])
    if diag.count(symbol) == len(tic) :
        return 1

    return 0
def Check_tie (tic) :
    for i in tic:
        if '_' in i:
            return 0
    return 1

def Check_Winning_Move (tic,symbol):
    # check rows for wining move
    counter = 0
    empty_position = 0
    for i in tic:
        if i.count(symbol) == len(tic)-1 and i.count('_') == 1 :
            empty_position = i.index('_')
            return [counter,empty_position]
        counter += 1

    # check columns for wining move
    for x in range(len(tic)):
        check_col = []
        for y in range(len(tic[x])):
             check_col.append(tic[y][x])
        if check_col.count(symbol) == len((tic[x]))-1 and check_col.count('_') == 1 :
            empty_position = check_col.index('_')
            return [ empty_position, x]

    # check diagonal for wining move
    diag = []
    for i in range(len(tic)):
        diag.append(tic[i][i])
    if diag.count(symbol) == len(tic)-1 and diag.count('_') == 1:
        empty_position = diag.index('_')
        return [empty_position, empty_position]

    # check other diagonal for wining move
    diag = []
    for i in range(len(tic)):
        diag.append(tic[i][len(tic) - 1 - i])
    if diag.count(symbol) == len(tic)-1 and diag.count("_") == 1:
        empty_position = diag.index('_')
        return [empty_position, len(tic) - 1 - empty_position]
    return []

# game 1V1 Flow
def play_game (player1,player2,tic) :
    w = 0
    win = []
    # loop for winning
    while w != 1:
        win = Check_Winning_Move(tic,player1)
        if win != []:
            print(f'Next Player , Notice There is a winning move : {win}')
        Enter(tic,player1)
        w = check_win(tic,player1)
        t = Check_tie(tic)
        Show_Tic(tic)
        if w == 1 :
            print(f'the winner is {player1} player')
            break
        elif t == 1 :
            print(f'There is a tie ! ')
            break
        win = Check_Winning_Move(tic, player2)
        if win != []:
            print(f'Notice There is a winning move : {win}')
        Enter(tic,player2)
        w = check_win(tic,player2)
        t = Check_tie(tic)
        Show_Tic(tic)
        if w == 1:
            print(f'the winner is {player2} player')
            break
        elif t == 1 :
            print(f'There is a tie ! ')
            break

# Game 1Vcomp
def play_game_with_comp (player1,player2,tic) :
    w = 0
    win = []
    # loop for winning
    while w != 1:
        win = Check_Winning_Move(tic, player1)
        if win != []:
            print(f'Next Player , Notice There is a winning move : {win}')
        Enter(tic,player1)
        w = check_win(tic,player1)
        t = Check_tie(tic)
        Show_Tic(tic)
        if w == 1 :
            print(f'the winner is {player1} player')
            break
        elif t == 1 :
            print(f'There is a tie ! ')
            break
        win = Check_Winning_Move(tic, player2)
        if win != []:
            print(f'Next Player , Notice There is a winning move : {win}')
        Enter_Comp(tic,player2)
        w = check_win(tic,player2)
        t = Check_tie(tic)
        Show_Tic(tic)
        if w == 1:
            print(f'the winner is {player2} player')
            break
        elif t == 1 :
            print(f'There is a tie ! ')
            break

def play_game_comp_with_comp (player1,player2,tic) :
    w = 0
    # loop for winning
    while w != 1:
        win = Check_Winning_Move(tic, player1)
        if win != []:
            print(f'Next Player , Notice There is a winning move : {win}')
        Enter_Comp(tic, player1)
        w = check_win(tic,player1)
        t = Check_tie(tic)
        Show_Tic(tic)
        if w == 1:
            print(f'the winner is {player1} player')
            break
        elif t == 1 :
            print(f'There is a tie ! ')
            break
        win = Check_Winning_Move(tic, player2)
        if win != []:
            print(f'Next Player , Notice There is a winning move : {win}')
        Enter_Comp(tic, player2)
        w = check_win(tic,player2)
        t = Check_tie(tic)
        Show_Tic(tic)
        if w == 1:
            print(f'the winner is {player2} player')
            break
        elif t == 1 :
            print(f'There is a tie ! ')
            break

# function for decide if i want to plat again
def play_again (v):
    answer = 0
    while answer != 'y' and answer != 'Y' and answer != 'n' and answer != 'N':
        print('want to play Again ? [Y/N]')
        answer = input()
    if answer == 'Y' or answer == 'y':
        return - 1
    else:
        return v

#Flow

import random
v = -1
answer = '_'
while v < 0 or v > 5:
    print(f'welcome ! , please select game mode : \n 1). 1V1 \n 2). 1Vcomp \n 3). compVcomp \n 4). play 4X4 board \n 5). exit game')
    v = int(input())
    # 4 X 4 Board Game
    if v == 4:
        tic = [['_', '_', '_', '_'], ['_', '_', '_', '_'], ['_', '_', '_', '_'],['_', '_', '_', '_']]
        print('wow you choose 4X4 board , have fun !')
        print(f'Choose game mode : \n 1). 1V1 \n 2). 1Vcomp \n 3). compVcomp \n 4). exit game')
        v = int(input())
    else :
        tic = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    # 1 V 1 game
    if v == 1:
        print('player1 : ')
        player1 = choose_symbol()
        if player1 == None:
            print('player2 : ')
            player2 = choose_symbol()
            if player2 == None:
                player2 = random.choice(['X', 'O'])
                player1 = check_symbol(player2)
            else:
                player1 = check_symbol(player2)
        else:
            player2 = check_symbol(player1)
        print(f'player 1 your symbol  is {player1}')
        print(f'player 2 your symbol  is {player2}')
        play_game(player1, player2, tic)
        v = play_again (v)
    # 1 V Comp game
    elif v == 2:
        print('player : ')
        player1 = choose_symbol()
        if player1 == None:
            print('computer player : ')
            player2 = random.choice(['X', 'O'])
            player1 = check_symbol(player2)
        else:
            player2 = check_symbol(player1)
        print(f'player 1 your symbol  is {player1}')
        print(f'computer player your symbol  is {player2}')
        play_game_with_comp (player1,player2,tic)
        v = play_again (v)
    # comp V comp Game
    elif v == 3:
        player1 = random.choice(['X', 'O'])
        player2 = check_symbol(player1)
        print(f'computer player 1 your symbol  is {player1}')
        print(f'computer player 2 your symbol  is {player2}')
        play_game_comp_with_comp(player1, player2, tic)
        v = play_again (v)
    # Exit game
    elif v == 5 or v == 4:
        print('exiting game.....')
        break




