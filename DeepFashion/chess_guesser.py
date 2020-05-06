#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the knightlOnAChessboard function below.
def make_Gameboard(n):
    gameboard = []
    for row in range(0,n):
        this_row = []
        for column in range(0,n):
            this_row.append(0)
        gameboard.append(this_row)
    return gameboard

def get_a_b_pairs(n):
    a_b_pair_list = []
    for a in range(1,n):
        for b in range(1,n):
            a_b_pair_list.append([a,b])
    return a_b_pair_list

def get_possible_locations(n,pair):
    possible_locations = []
    for x in range(0,n):
            for y in range(0,n):
                if (x+y)%2==0:
                    if (x*pair[0])<=n:
                        if (y*pair[1])<=n:
                            location = [x*pair[0],y*pair[1]]
                            if location in possible_locations:
                                continue
                            else:
                                possible_locations.append(location)
    return possible_locations

def show_solved_Gameboards(n):
    gameboard = make_Gameboard(n)
    a_b_pair_list = get_a_b_pairs(n)
    print(len(a_b_pair_list))
    for pair in a_b_pair_list:
        new_gameboard = make_Gameboard(n)
        possible_locations = get_possible_locations(n,pair)
        for location in possible_locations:
            new_gameboard[location[0]][location[1]] = 1
            new_gameboard[location[1]][location[0]] = 1
        print_Gameboard(new_gameboard, pair)

def print_Gameboard(board, pair):
    print("Board for the pair ", pair)
    for row in board:
            print(row)
    print('--------------------------')

def crawl_board(n,pair):
    crawled_board = make_Gameboard(n)
    position=[0,0]
    all_positions = []
    target_reached = False
    iterations = 0
    vectors = possible_vectors_from_pair(pair)
    WASTED_LOOPS = 0
    counted = False
    while target_reached == False and iterations<1000:
        #append position to list of all positions  visited
        if not position in all_positions:
            all_positions.append(position)
        else:
            counted = True
            WASTED_LOOPS += 1
        #choose random vector
        rand_vector = vectors[random.randint(0,len(vectors)-1)]
        proposed_position = [position[0] + rand_vector[0],position[1] + rand_vector[1]]
        if 0 <= proposed_position[0] < n and 0 <= proposed_position[1] < n:
            position=proposed_position
        else:
            if not counted:
                WASTED_LOOPS+=1
        #terminate if target position is reached
        if position == [n-1,n-1]:
            target_reached = False
        iterations += 1
    #update gameboard with 1's for positions visited
    for position in all_positions:
        crawled_board[position[0]][position[1]] = 1
    print("Wasted Loops: ", WASTED_LOOPS)
    return crawled_board

def possible_vectors_from_pair(pair):
    a = pair[0]
    b = pair[1]
    vectors_possible=[
        [a,b],
        [-a,b],
        [a,-b],
        [-a,-b],
        [b,a],
        [b,-a],
        [-b,a],
        [-b,-a],
    ]
    return vectors_possible

def check_possible_Moves(position,n,pair,previous):
    possible_moves = 0
    for vector in possible_vectors_from_pair(pair):
        new_Position = [position[0]+vector[0],position[1]+vector[1]]
        if 0<=new_Position[0]<n and 0<=new_Position[1]<n:
            if not new_Position in previous:
                possible_moves += 1
                previous.append(new_Position)
        # if new_Position[0]==(n-1) and new_Position[1]==(n-1):
        #     print("winner")
    return [previous, possible_moves]

def recursive(previous_moves,n,pair):
    local_count = 0
    for move in range(0,previous_moves[1]):
        this_position = previous_moves[0][len(previous_moves[0])-move-1]
        new_previous_moves = check_possible_Moves(this_position,n,pair,previous_moves[0])
        local_count = new_previous_moves[1]+1
    new_previous_moves[1]=local_count
    new_previous_moves.append(previous_moves[2]+1)
    return new_previous_moves

def check_for_winner(previous_moves,n):
    if [n-1,n-1] in previous_moves[0]:
        return True
    else:
        return False

def knightlOnAChessboard(n):
    pairs = get_a_b_pairs(n)
    for pair in pairs:
        previous_moves = [[[0,0]],1,0]
        winner = False
        while winner==False:
            previous_moves = recursive(previous_moves,n,pair)
            winner = check_for_winner(previous_moves,n)
            if previous_moves[1]==0:
                winner = True
                previous_moves[2] = -1
        print(pair, previous_moves[2])

knightlOnAChessboard(5)
