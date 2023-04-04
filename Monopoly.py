import time
import random

game_winner = 0
landmarks = {1: 'Start', 2: 'Old Kent Road', 3: 'Community Chest', 4: 'Whitechapel Road', 5: 'Income Tax',
             6: 'Kings Cross Station', 7: 'The Angel Islington', 8: 'Chance', 9: 'Euston Road', 10: 'Pentonville Road',
             11: 'Jail', 12: 'Pall Mall', 13: 'Electric Company', 14: 'Whitehall', 15: 'Northumberland Avenue',
             16: 'Marylebone Station', 17: 'Bow Street', 18: 'Community Chest', 19: 'Marlborough Street',
             20: 'Vine Street', 21: 'Free Parking', 22: 'Strand', 23: 'Chance', 24: 'Fleet Street',
             25: 'Trafalgar Square', 26: 'Fenchurch Street Station', 27: 'Leicester Square', 28: 'Coventry Street',
             29: 'Water Works', 30: 'Piccadilly', 31: 'Go To Jail', 32: 'Regent Street', 33: 'Oxford Street',
             34: 'Community Chest', 35: 'Bond Street', 36: 'Liverpool Street Station', 37: 'Chance', 38: 'Park Lane',
             39: 'Super Tax', 40: 'Mayfair'}
cost = {2: 60, 3: 0, 4: 60, 5: 200, 6: 200, 7: 100, 8: 0, 9: 100, 10: 120, 11: 0, 12: 140, 13: 150, 14: 140, 15: 160,
        16: 200, 17: 180, 18: 0, 19: 180, 20: 200, 21: 0, 22: 220, 23: 0, 24: 220, 25: 240, 26: 200, 27: 260, 28: 260,
        29: 150, 30: 280, 31: 0, 32: 300, 33: 300, 34: 0, 35: 320, 36: 200, 37: 0, 38: 350, 39: 350, 40: 400}
purchasable = [2, 4, 7, 9, 10, 12, 14, 15, 17, 19, 20, 22, 24, 25, 26, 27, 28, 30, 32, 33, 35, 36, 38, 40]
traps = [5, 39, 31]
owned = []
p1 = [1500, 1]
p1_property = []
p2 = [1500, 1]
p2_property = []


def dice():
    return random.randint(1, 6)


def cpu():
    if p2[0] <= 60:
        global game_winner
        game_winner = 1
        return 'CPU has gone bankrupt, You win'
    print('CPU is rolling the dice...')
    time.sleep(1)
    x = dice()
    p2[1] += x
    print(f'CPU rolled a {x}')
    if p2[1] > 40:
        p2[1] -= 40
        p2[0] += 200
    if p2[1] in traps:
        if p2[1] == 5:
            p2[0] -= 200
            return 'CPU has been hit by the Income Tax'
        elif p2[1] == 39:
            p2[0] -= 400
            return 'CPU has been hit by the Super Tax'
        elif p2[1] == 31:
            p2[1] = 11
            return 'CPU has been sent to Jail'
    elif p2[1] in purchasable:
        print(f'CPU has landed on {landmarks[p2[1]]} and it costs ${cost[p2[1]]}')
        if p2[0] >= cost[p2[1]]:
            print('CPU is contemplating on getting the property')
            contem = random.randint(1, 2)
            if contem == 1:
                print('CPU has decided to buy the property')
                p2[0] -= cost[p2[1]]
                p2_property.append(p2[1])
                purchasable.remove(p2[1])
                owned.append(p2[1])
                return f'CPU now has ${p2[0]}'
            else:
                return 'CPU has decided not to buy the property'
        else:
            return 'CPU does not have enough money to buy the property'
    elif p2[1] in owned:
        if p2[1] in p1_property:
            print(f'CPU has landed on {landmarks[p2[1]]} which is owned by you')
            print('CPU is paying rent')
            p2[0] -= cost[p2[1]]
            p1[0] += cost[p2[1]]
            return f'CPU now has ${p2[0]}'
    else:
        print(f'CPU has landed on {landmarks[p2[1]]}')
        return 'CPU has done nothing'


def player1():
    if p1[0] <= 60:
        global game_winner
        game_winner = 1
        return 'You have gone bankrupt, Opponent wins'
    print('You are rolling the dice...')
    time.sleep(1)
    x = dice()
    p1[1] += x
    print(f'You rolled a {x}')
    if p1[1] > 40:
        p1[1] -= 40
        p1[0] += 200
    if p1[1] in traps:
        if p1[1] == 5:
            p1[0] -= 200
            return 'You have been hit by the Income Tax'
        elif p1[1] == 39:
            p1[0] -= 400
            return 'You have been hit by the Super Tax'
        elif p1[1] == 31:
            p1[1] = 11
            return 'You have been sent to Jail'
    elif p1[1] in purchasable:
        print(f'You have landed on {landmarks[p1[1]]} and it costs ${cost[p1[1]]}')
        if p1[0] >= cost[p1[1]]:
            print('You are contemplating on getting the property')
            contem = int(input('Do you want to buy the property? (1)Yes (2)No: '))
            if contem == 1:
                print('You have decided to buy the property')
                p1[0] -= cost[p1[1]]
                p1_property.append(p1[1])
                purchasable.remove(p1[1])
                owned.append(p1[1])
                return f'You now have ${p1[0]}'
            else:
                return 'You have decided not to buy the property'
        else:
            return 'You do not have enough money to buy the property'
    elif p1[1] in owned:
        if p1[1] in p2_property:
            print(f'You have landed on {landmarks[p1[1]]} which is owned by your opponent')
            print('You are paying rent')
            p1[0] -= cost[p1[1]]
            p2[0] += cost[p1[1]]
            return f'You now have ${p1[0]}'
    else:
        print(f'You have landed on {landmarks[p1[1]]}')
        return 'You have done nothing'


def player2():
    if p2[0] <= 60:
        global game_winner
        game_winner = 1
        return 'Player 2 has gone bankrupt, Player 1 wins'
    print('Player 2 is rolling the dice...')
    time.sleep(1)
    x = dice()
    p2[1] += x
    print(f'Player 2 rolled a {x}')
    if p2[1] > 40:
        p2[1] -= 40
        p2[0] += 200
    if p2[1] in traps:
        if p2[1] == 5:
            p2[0] -= 200
            return 'Player 2 has been hit by the Income Tax'
        elif p2[1] == 39:
            p2[0] -= 400
            return 'Player 2 has been hit by the Super Tax'
        elif p2[1] == 31:
            p2[1] = 11
            return 'Player 2 has been sent to Jail'
    elif p2[1] in purchasable:
        print(f'Player 2 has landed on {landmarks[p2[1]]} and it costs ${cost[p2[1]]}')
        if p2[0] >= cost[p2[1]]:
            print('Player 2 is contemplating on getting the property')
            contem = int(input('Do you want to buy the property? (1)Yes (2)No: '))
            if contem == 1:
                print('Player 2 has decided to buy the property')
                p2[0] -= cost[p2[1]]
                p2_property.append(p2[1])
                purchasable.remove(p2[1])
                owned.append(p2[1])
                return f'Player 2 now has ${p2[0]}'
            else:
                return 'Player 2 has decided not to buy the property'
        else:
            return 'Player 2 does not have enough money to buy the property'
    elif p2[1] in owned:
        if p2[1] in p1_property:
            print(f'Player 2 has landed on {landmarks[p2[1]]} which is owned by Player 1')
            print('Player 2 is paying rent')
            p2[0] -= cost[p2[1]]
            p1[0] += cost[p2[1]]
            return f'Player 2 now has ${p2[0]}'
    else:
        print(f'Player 2 has landed on {landmarks[p2[1]]}')
        return 'Player 2 has done nothing'


def choiice(x):
    if x == 1:
        print('You have chosen to play against the CPU')
        turns = int(
            input('How many turns do you want to play for? [If you want an infinite number of turns Enter 0]: '))
        if turns == 0:
            while game_winner == 0:
                print(player1())
                time.sleep(2)
                print(cpu())
        else:
            for i in range(turns):
                if game_winner == 1:
                    break
                print(player1())
                time.sleep(2)
                print(cpu())
            if p2[0] > p1[0]:
                print('CPU wins')
            else:
                print('You win')
    elif x == 2:
        print('You have chosen to play against another player')
        turns = int(
            input('How many turns do you want to play for? [If you want an infinite number of turns Enter 0]: '))
        if turns == 0:
            while game_winner == 0:
                print(player1())
                time.sleep(2)
                print(player2())
        else:
            for i in range(turns):
                if game_winner == 1:
                    break
                print(player1())
                time.sleep(2)
                print(player2())
            if p2[0] > p1[0]:
                print('Player 2 wins')
            else:
                print('Player 1 wins')


print('Welcome to Monopoly [2P]')
print('Do you want to play against the (1)CPU or (2)Another player?')
choice = int(input('Enter your choice: '))
if choice == 1:
    choiice(1)
elif choice == 2:
    choiice(2)
