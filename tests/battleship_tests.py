from nose.tools import *
from Battleship.battleship import *
from Battleship.ships import *
from Battleship.playgame import *
from Battleship.ai import *

import random


def test_isFree_empty_human():
    game = board()
    
    #empty board tests for human
    assert_equal(game.isFree(0, 0, True), True)
    assert_equal(game.isFree(game.X_AXIS-1, 0, True), True)
    assert_equal(game.isFree(0, game.Y_AXIS-1, True), True)
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS-1, True), True)

def test_isFree_empty_computer():
    game = board()
    
    #empty board tests for computer
    assert_equal(game.isFree(0, 0, False), True)
    assert_equal(game.isFree(game.X_AXIS-1, 0, False), True)
    assert_equal(game.isFree(0, game.Y_AXIS-1, False), True)
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS-1, False), True)
    

def test_isFree_Human():
    
    #player board tests with ships in extreme positions
    #corners
    game = board()
    game.p_map[0][0] = 1
    game.p_map[game.X_AXIS-1][0] = 1
    game.p_map[0][game.Y_AXIS-1] = 1
    game.p_map[game.X_AXIS-1][game.Y_AXIS-1] = 1
    #extreme rows and columns
    game.p_map[game.X_AXIS/2][0] = 1
    game.p_map[game.X_AXIS/2][game.Y_AXIS-1] = 1
    game.p_map[0][game.Y_AXIS/2] = 1
    game.p_map[game.X_AXIS-1][game.Y_AXIS/2] = 1


    #top left corner, 4 squares should be false
    assert_equal(game.isFree(0, 0, True), False)
    assert_equal(game.isFree(0, 1, True), False)
    assert_equal(game.isFree(1, 0, True), False)
    assert_equal(game.isFree(1, 1, True), False)

    #top right corner, 4 squares should be false
    assert_equal(game.isFree(game.X_AXIS-1, 0, True), False)
    assert_equal(game.isFree(game.X_AXIS-1, 1, True), False)
    assert_equal(game.isFree(game.X_AXIS-2, 0, True), False)
    assert_equal(game.isFree(game.X_AXIS-2, 1, True), False)
    #bottom left corner, 4 squares should be false
    assert_equal(game.isFree(0, game.Y_AXIS-1, True), False)
    assert_equal(game.isFree(0, game.Y_AXIS-2, True), False)
    assert_equal(game.isFree(1, game.Y_AXIS-1, True), False)
    assert_equal(game.isFree(1, game.Y_AXIS-2, True), False)
    #bottom right corner, 4 squares should be false
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS-1, True), False)
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS-2, True), False)
    assert_equal(game.isFree(game.X_AXIS-2, game.Y_AXIS-1, True), False)
    assert_equal(game.isFree(game.X_AXIS-2, game.Y_AXIS-2, True), False)


    #tests top row, 6 squares
    assert_equal(game.isFree(game.X_AXIS/2, 0, True), False)
    assert_equal(game.isFree(game.X_AXIS/2-1, 0, True), False)
    assert_equal(game.isFree(game.X_AXIS/2+1, 0, True), False)
    assert_equal(game.isFree(game.X_AXIS/2-1, 1, True), False)
    assert_equal(game.isFree(game.X_AXIS/2, 1, True), False)
    assert_equal(game.isFree(game.X_AXIS/2+1, 1, True), False)
    #tests bottom row, 6 squares
    assert_equal(game.isFree(game.X_AXIS/2, game.Y_AXIS-1, True), False)
    assert_equal(game.isFree(game.X_AXIS/2-1, game.Y_AXIS-1, True), False)
    assert_equal(game.isFree(game.X_AXIS/2+1, game.Y_AXIS-1, True), False)
    assert_equal(game.isFree(game.X_AXIS/2-1, game.Y_AXIS-2, True), False)
    assert_equal(game.isFree(game.X_AXIS/2, game.Y_AXIS-2, True), False)
    assert_equal(game.isFree(game.X_AXIS/2+1, game.Y_AXIS-2, True), False)
    #leftmost column, 6 squares
    assert_equal(game.isFree(0, game.Y_AXIS/2, True), False)
    assert_equal(game.isFree(0, game.Y_AXIS/2+1, True), False)
    assert_equal(game.isFree(0, game.Y_AXIS/2-1, True), False)
    assert_equal(game.isFree(1, game.Y_AXIS/2, True), False)
    assert_equal(game.isFree(1, game.Y_AXIS/2+1, True), False)
    assert_equal(game.isFree(1, game.Y_AXIS/2-1, True), False)
    #rightmost column, 6 squares
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS/2, True), False)
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS/2+1, True), False)
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS/2-1, True), False)
    assert_equal(game.isFree(game.X_AXIS-2, game.Y_AXIS/2, True), False)
    assert_equal(game.isFree(game.X_AXIS-2, game.Y_AXIS/2+1, True), False)
    assert_equal(game.isFree(game.X_AXIS-2, game.Y_AXIS/2-1, True), False)

    #this tests out the squar board left when ships are places in extrema
    #it ommits a few coordinates though
    for i in range(2, game.Y_AXIS-2):
        for j in range(2, game.X_AXIS-2):
            assert_equal(game.isFree(j, i, True), True)


    # random case is last
    #test random case which is at least 1 square from boarders
    ran_x = random.randint(1, 23)
    ran_y = random.randint(1, 13)
    game.p_map[ran_x][ran_y] = 1

    #test around the random ship, 9 squares
    assert_equal(game.isFree(ran_x-1, ran_y-1, True), False)
    assert_equal(game.isFree(ran_x, ran_y-1, True), False)
    assert_equal(game.isFree(ran_x+1, ran_y-1, True), False)
    assert_equal(game.isFree(ran_x-1, ran_y, True), False)
    assert_equal(game.isFree(ran_x, ran_y, True), False)
    assert_equal(game.isFree(ran_x+1, ran_y, True), False)
    assert_equal(game.isFree(ran_x-1, ran_y+1, True), False)
    assert_equal(game.isFree(ran_x, ran_y+1, True), False)
    assert_equal(game.isFree(ran_x+1, ran_y+1, True), False)

def test_isFree_Computer():
    
    #player board tests with ships in extreme positions
    #corners
    game = board()
    game.c_map[0][0] = 1
    game.c_map[game.X_AXIS-1][0] = 1
    game.c_map[0][game.Y_AXIS-1] = 1
    game.c_map[game.X_AXIS-1][game.Y_AXIS-1] = 1
    #extreme rows and columns
    game.c_map[game.X_AXIS/2][0] = 1
    game.c_map[game.X_AXIS/2][game.Y_AXIS-1] = 1
    game.c_map[0][game.Y_AXIS/2] = 1
    game.c_map[game.X_AXIS-1][game.Y_AXIS/2] = 1


    #top left corner, 4 squares should be false
    assert_equal(game.isFree(0, 0, False), False)
    assert_equal(game.isFree(0, 1, False), False)
    assert_equal(game.isFree(1, 0, False), False)
    assert_equal(game.isFree(1, 1, False), False)

    #top right corner, 4 squares should be false
    assert_equal(game.isFree(game.X_AXIS-1, 0, False), False)
    assert_equal(game.isFree(game.X_AXIS-1, 1, False), False)
    assert_equal(game.isFree(game.X_AXIS-2, 0, False), False)
    assert_equal(game.isFree(game.X_AXIS-2, 1, False), False)
    #bottom left corner, 4 squares should be false
    assert_equal(game.isFree(0, game.Y_AXIS-1, False), False)
    assert_equal(game.isFree(0, game.Y_AXIS-2, False), False)
    assert_equal(game.isFree(1, game.Y_AXIS-1, False), False)
    assert_equal(game.isFree(1, game.Y_AXIS-2, False), False)
    #bottom right corner, 4 squares should be false
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS-1, False), False)
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS-2, False), False)
    assert_equal(game.isFree(game.X_AXIS-2, game.Y_AXIS-1, False), False)
    assert_equal(game.isFree(game.X_AXIS-2, game.Y_AXIS-2, False), False)


    #tests top row, 6 squares
    assert_equal(game.isFree(game.X_AXIS/2, 0, False), False)
    assert_equal(game.isFree(game.X_AXIS/2-1, 0, False), False)
    assert_equal(game.isFree(game.X_AXIS/2+1, 0, False), False)
    assert_equal(game.isFree(game.X_AXIS/2-1, 1, False), False)
    assert_equal(game.isFree(game.X_AXIS/2, 1, False), False)
    assert_equal(game.isFree(game.X_AXIS/2+1, 1, False), False)
    #tests bottom row, 6 squares
    assert_equal(game.isFree(game.X_AXIS/2, game.Y_AXIS-1, False), False)
    assert_equal(game.isFree(game.X_AXIS/2-1, game.Y_AXIS-1, False), False)
    assert_equal(game.isFree(game.X_AXIS/2+1, game.Y_AXIS-1, False), False)
    assert_equal(game.isFree(game.X_AXIS/2-1, game.Y_AXIS-2, False), False)
    assert_equal(game.isFree(game.X_AXIS/2, game.Y_AXIS-2, False), False)
    assert_equal(game.isFree(game.X_AXIS/2+1, game.Y_AXIS-2, False), False)
    #leftmost column, 6 squares
    assert_equal(game.isFree(0, game.Y_AXIS/2, False), False)
    assert_equal(game.isFree(0, game.Y_AXIS/2+1, False), False)
    assert_equal(game.isFree(0, game.Y_AXIS/2-1, False), False)
    assert_equal(game.isFree(1, game.Y_AXIS/2, False), False)
    assert_equal(game.isFree(1, game.Y_AXIS/2+1, False), False)
    assert_equal(game.isFree(1, game.Y_AXIS/2-1, False), False)
    #rightmost column, 6 squares
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS/2, False), False)
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS/2+1, False), False)
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS/2-1, False), False)
    assert_equal(game.isFree(game.X_AXIS-2, game.Y_AXIS/2, False), False)
    assert_equal(game.isFree(game.X_AXIS-2, game.Y_AXIS/2+1, False), False)
    assert_equal(game.isFree(game.X_AXIS-2, game.Y_AXIS/2-1, False), False)

    #this tests out the squar board left when ships are places in extrema
    #it ommits a few coordinates though
    for i in range(2, game.Y_AXIS-2):
        for j in range(2, game.X_AXIS-2):
            assert_equal(game.isFree(j, i, False), True)


    # random case is last
    #test random case which is at least 1 square from boarders
    ran_x = random.randint(1, 23)
    ran_y = random.randint(1, 13)
    game.c_map[ran_x][ran_y] = 1

    #test around the random ship, 9 squares
    assert_equal(game.isFree(ran_x-1, ran_y-1, False), False)
    assert_equal(game.isFree(ran_x, ran_y-1, False), False)
    assert_equal(game.isFree(ran_x+1, ran_y-1, False), False)
    assert_equal(game.isFree(ran_x-1, ran_y, False), False)
    assert_equal(game.isFree(ran_x, ran_y, False), False)
    assert_equal(game.isFree(ran_x+1, ran_y, False), False)
    assert_equal(game.isFree(ran_x-1, ran_y+1, False), False)
    assert_equal(game.isFree(ran_x, ran_y+1, False), False)
    assert_equal(game.isFree(ran_x+1, ran_y+1, False), False)

def test_placeShip_Big_Horizontal():
    game = board()
    game.placeShip(fiveSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'horizontal'), True)

    for i in range(5):
        assert_equal(game.p_map[game.X_AXIS/2+i][game.Y_AXIS/2], 1)

def test_placeShip_Big_Verticle():
    game = board()
    game.placeShip(fiveSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'verticle'), True)

    for i in range(5):
        assert_equal(game.p_map[game.X_AXIS/2][game.Y_AXIS/2+i], 1)

def test_placeShip_Big_Horizontal_computer():
    game = board()
    game.placeShip(fiveSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'horizontal'), False)

    for i in range(5):
        assert_equal(game.c_map[game.X_AXIS/2+i][game.Y_AXIS/2], 1)

def test_placeShip_Big_Verticle_computer():
    game = board()
    game.placeShip(fiveSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'verticle'), False)

    for i in range(5):
        assert_equal(game.c_map[game.X_AXIS/2][game.Y_AXIS/2+i], 1)



def test_placeShip_Medium_Horizontal():
    game = board()
    game.placeShip(fourSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'horizontal'), True)

    for i in range(4):
        assert_equal(game.p_map[game.X_AXIS/2+i][game.Y_AXIS/2], 1)

def test_placeShip_Medium_Verticle():
    game = board()
    game.placeShip(fourSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'verticle'), True)

    for i in range(4):
        assert_equal(game.p_map[game.X_AXIS/2][game.Y_AXIS/2+i], 1)

def test_placeShip_Medium_Horizontal_computer():
    game = board()
    game.placeShip(fourSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'horizontal'), False)

    for i in range(4):
        assert_equal(game.c_map[game.X_AXIS/2+i][game.Y_AXIS/2], 1)

def test_placeShip_Medium_Verticle_computer():
    game = board()
    game.placeShip(fourSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'verticle'), False)

    for i in range(4):
        assert_equal(game.c_map[game.X_AXIS/2][game.Y_AXIS/2+i], 1)     

def test_placeShip_Small_Verticle():
    game = board()
    game.placeShip(threeSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'verticle'), True)

    for i in range(3):
        assert_equal(game.p_map[game.X_AXIS/2][game.Y_AXIS/2+i], 1)

def test_placeShip_Small_Horizontal():
    game = board()
    game.placeShip(threeSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'horizontal'), True)

    for i in range(3):
        assert_equal(game.p_map[game.X_AXIS/2+i][game.Y_AXIS/2], 1)  

def test_placeShip_Small_Horizontal_computer():
    game = board()
    game.placeShip(threeSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'horizontal'), False)

    for i in range(3):
        assert_equal(game.c_map[game.X_AXIS/2+i][game.Y_AXIS/2], 1)

def test_placeShip_Small_Verticle_computer():



    game = board()
    game.placeShip(threeSquareShip(game.X_AXIS/2, game.Y_AXIS/2, 'verticle'), False)

    for i in range(3):
        assert_equal(game.c_map[game.X_AXIS/2][game.Y_AXIS/2+i], 1)       


def test_playgame_input_verify():
    game = board()
    computer = ai()
    play = playgame(game, computer)
    #input too short
    assert_equal(play.verify_input('13, 13'), False)
    #check if it handles correct input correctly. Note:, function subtracts 1 from user input.
    assert_equal(play.verify_input('10, 10, v'), [9, 9, 'v'])
    #input not in right format ie no number in first place
    assert_equal(play.verify_input('v, 13, 13'), False)
    assert_equal(play.verify_input('13, v, 13'), False)
    #wrong char for verticle/horizontal
    assert_equal(play.verify_input('13, 13, b'), False)
    #input too large or negative
    assert_equal(play.verify_input('%d, 1, v' % (game.X_AXIS+1)), False)
    assert_equal(play.verify_input('1, %d, v' % (game.Y_AXIS+1)), False)
    assert_equal(play.verify_input('0, 0, v'), False)
    assert_equal(play.verify_input('-1, -5, v'), False)

#def test_playgame_putship():

def test_battleship_battle_horizontal():
    #!this test can be nicely optimized with loops!
    #write same test except for verticle ship
    #also check if other squares dont become hit or sunk.
    game = board()
    computer = ai()
    play = playgame(game, computer)
    ships = []
    #this test places a horizontal ship at 0, 0 and creates and object 
    #quite manually
    ships.append(fourSquareShip(0, 0, 'horizontal'))
    #adds one horizontal ship and 1 verticle object
    ships.append(fourSquareShip(15, 7, 'horizontal'))
    ships.append(threeSquareShip(2, 5, 'verticle'))
    #adds above ships to map, manually
    for i in range(5, 8):
        game.p_map[2][i] = 1
    for i in range(15, 19):
        game.p_map[i][7] = 1
    for i in range(0, 4):
        game.p_map[i][0] = 1

    #this quickly checks if there's a ship at 0, 0
    assert_equal(game.p_map[0][0], 1)
    assert_equal(ships[0].getHealth(), 4)
    #this hits the 4 square ship with 3 hits and checks it's health
    ships = game.battle(0, 0, True, ships)
    #health check
    assert_equal(ships[0].getHealth(), 3)
    #hit, etc.
    ships = game.battle(1, 0, True, ships)
    assert_equal(ships[0].getHealth(), 2)
    ships = game.battle(2, 0, True, ships)
    assert_equal(ships[0].getHealth(), 1)
    #this checks if hit squares turned from 1 (ship) to 3 (hit)
    for i in [0, 1, 2]:
        assert_equal(game.p_map[i][0], 3)

    #hits ship 4th time, sinks it
    ships = game.battle(3, 0, True, ships)
   # assert_equal(game.p_map[3][0], 4)
    #ship hp should be 0
    assert_equal(ships[0].getHealth(), 0)
    #next code checks if battle sub functions marked ship as sunk
    for i in range(0, 4):        
        assert_equal(game.p_map[i][0], 4)
    #check 2nd 4square ship
    for i in range(15, 19):
        assert_equal(game.p_map[i][7], 1)
    #check 1st 3square ship
    for i in range(5, 8):
        assert_equal(game.p_map[2][i], 1)
    
    #Now we will sink the verticle ship
    ships = game.battle(2, 5, True, ships)
    assert_equal(game.p_map[2][5], 3)
    assert_equal(ships[2].getHealth(), 2)
    ships = game.battle(2, 6, True, ships)
    assert_equal(game.p_map[2][6], 3)
    assert_equal(ships[2].getHealth(), 1)    
    ships = game.battle(2, 7, True, ships)
    assert_equal(game.p_map[2][5], 4)

    #now we sink the other horizontal ship
    ships = game.battle(15, 7, True, ships)
    ships = game.battle(16, 7, True, ships)
    assert_equal(game.p_map[15][7], 3)
    assert_equal(game.p_map[16][7], 3)
    assert_equal(ships[1].getHealth(), 2)
    ships = game.battle(17, 7, True, ships)
    ships = game.battle(18, 7, True, ships)
    assert_equal(ships[1].getHealth(), 0)
    for i in range(15, 19):
        assert_equal(game.p_map[i][7], 4)

