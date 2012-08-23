from nose.tools import *
from Battleship.battleship import *
from Battleship.ships import *

import random


def test_isFree_human():
    game = board()
    
    #empty board tests for human
    assert_equal(game.isFree(0, 0, True), True)
    assert_equal(game.isFree(game.X_AXIS-1, 0, True), True)
    assert_equal(game.isFree(0, game.Y_AXIS-1, True), True)
    assert_equal(game.isFree(game.X_AXIS-1, game.Y_AXIS-1, True), True)

def test_isFree_computer():
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

def test_placeShip():
    bigShip = fiveSquareShip('horizontal')
    assert_equal(bigShip.LENGTH, 5)
    assert_equal(bigShip.direction, 'horizontal')
    game = board()
    game.placeShip(bigShip)
    assert_equal(game.placeShip, 5)
