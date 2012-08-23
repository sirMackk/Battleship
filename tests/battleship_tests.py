from nose.tools import *
from Battleship.battleship import *

import random


def test_isFree_human():
    game = board()
    
    #empty board tests for human
    assert_equal(game.isFree(0, 0, True), True)
    assert_equal(game.isFree(game.x_axis-1, 0, True), True)
    assert_equal(game.isFree(0, game.y_axis-1, True), True)
    assert_equal(game.isFree(game.x_axis-1, game.y_axis-1, True), True)

def test_isFree_computer():
    game = board()
    
    #empty board tests for computer
    assert_equal(game.isFree(0, 0, False), True)
    assert_equal(game.isFree(game.x_axis-1, 0, False), True)
    assert_equal(game.isFree(0, game.y_axis-1, False), True)
    assert_equal(game.isFree(game.x_axis-1, game.y_axis-1, False), True)
    
def test_isFree_human_wShips():
    #player board tests with ships in extreme positions
    #corners
    game = board()
    game.p_map[0][0] = 1
    game.p_map[game.x_axis-1][0] = 1
    game.p_map[0][game.y_axis-1] = 1
    game.p_map[game.x_axis-1][game.y_axis-1] = 1
    #extreme rows and columns
    game.p_map[game.x_axis/2][0] = 1
    game.p_map[game.x_axis/2][game.y_axis-1] = 1
    game.p_map[0][game.y_axis/2] = 1
    game.p_map[game.x_axis-1][game.y_axis/2] = 1


    #top left corner, 4 squares should be false
    assert_equal(game.isFree(0, 0, True), False)
    assert_equal(game.isFree(0, 1, True), False)
    assert_equal(game.isFree(1, 0, True), False)
    assert_equal(game.isFree(1, 1, True), False)

    #top right corner, 4 squares should be false
    assert_equal(game.isFree(game.x_axis-1, 0, True), False)
    assert_equal(game.isFree(game.x_axis-1, 1, True), False)
    assert_equal(game.isFree(game.x_axis-2, 0, True), False)
    assert_equal(game.isFree(game.x_axis-2, 1, True), False)
    #bottom left corner, 4 squares should be false
    assert_equal(game.isFree(0, game.y_axis-1, True), False)
    assert_equal(game.isFree(0, game.y_axis-2, True), False)
    assert_equal(game.isFree(1, game.y_axis-1, True), False)
    assert_equal(game.isFree(1, game.y_axis-2, True), False)
    #bottom right corner, 4 squares should be false
    assert_equal(game.isFree(game.x_axis-1, game.y_axis-1, True), False)
    assert_equal(game.isFree(game.x_axis-1, game.y_axis-2, True), False)
    assert_equal(game.isFree(game.x_axis-2, game.y_axis-1, True), False)
    assert_equal(game.isFree(game.x_axis-2, game.y_axis-2, True), False)


    #tests top row, 6 squares
    assert_equal(game.isFree(game.x_axis/2, 0, True), False)
    assert_equal(game.isFree(game.x_axis/2-1, 0, True), False)
    assert_equal(game.isFree(game.x_axis/2+1, 0, True), False)
    assert_equal(game.isFree(game.x_axis/2-1, 1, True), False)
    assert_equal(game.isFree(game.x_axis/2, 1, True), False)
    assert_equal(game.isFree(game.x_axis/2+1, 1, True), False)




    # random case is last
    #test random case which is at least 1 square from boarders
    #game.p_map[random.randint(1, 23)][random.randint(1, 13)] = 1


    #this tests out the squar board left when ships are places in extrema
    #it ommits a few coordinates though
    for i in range(2, game.y_axis-2):
        for j in range(2, game.x_axis-2):
            assert_equal(game.isFree(j, i, True), True)
