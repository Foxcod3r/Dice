from random import randint
from os import system, name

#developer : Foxcoder
#I hope you enjoy this game

def check(dice: int):
    if dice == 6:
        return True
    else:
        return False

def clear():
    system("cls" if name == "nt" else "clear")

player_1, player_2 = input('''Enter the first player's name : '''), input('''Enter the name of the second player : ''')
clear()

_position1, _position2 = 0, 0
_accepted1, _accepted2 = False, False

save1, save2 = '□'*26, '□'*26
ui = list('□'*26)

while True:
    if _accepted1:
        clear()
        print(f'{player_1} : {save1} : {_position1}\n{player_2} : {save2} : {_position2}\n'+'-'*55)
        input(f'{player_1} : Please Enter [enter] to roll the dice')
        clear()
        _chance = randint(1,6)
        _position1 += _chance
        try:
            ui[_position1] = '■'
            save1 = ''.join([str(i) for i in ui])
            ui[_position1] = '□'
            if _position1 == 25: print(f'{player_1} : {save1} : {_position1}\n{player_2} : {save2} : {_position2}\n'+'-'*55+f'Player {player_2} won');break
        except IndexError:
            _position1 -= _chance
        print(f'{player_1} : {save1} : {_position1}\n{player_2} : {save2} : {_position2}\n'+'-'*55)
    else:
        clear()
        print(f'{player_1} : {save1} : {_position1}\n{player_2} : {save2} : {_position2}\n'+'-'*55)
        input(f'{player_1} : Please Enter [enter] to roll the dice')
        clear()
        _accepted1 = check(randint(1,6))
        
    if _accepted2:
        clear()
        print(f'{player_1} : {save1} : {_position1}\n{player_2} : {save2} : {_position2}\n'+'-'*55)
        input(f'{player_2} : Please Enter [enter] to roll the dice')
        clear()
        _chance = randint(1,6)
        _position2 += _chance
        try:
            ui[_position2] = '■'
            save2 = ''.join([str(i) for i in ui])
            ui[_position2] = '□'
            if _position2 == 25: print(f'{player_1} : {save1} : {_position1}\n{player_2} : {save2} : {_position2}\n'+'-'*55+f'Player {player_2} won');break
        except IndexError:
            _position2 -= _chance
        print(f'{player_1} : {save1} : {_position1}\n{player_2} : {save2} : {_position2}\n'+'-'*55)
    else:
        clear()
        print(f'{player_1} : {save1} : {_position1}\n{player_2} : {save2} : {_position2}\n'+'-'*55)
        input(f'{player_2} : Please Enter [enter] to roll the dice')
        clear()
        _accepted2 = check(randint(1,6))