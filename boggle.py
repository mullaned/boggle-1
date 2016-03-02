from random import choice
from string import ascii_uppercase

def make_grid(width, height):
    return {(x, y): choice(ascii_uppercase)
            for x in range(width)
            for y in range(height)}


def neighbours_of_position(x, y):
    return [
             (x-1, y-1), (x, y-1), (x+1, y-1),
             (x-1, y),             (x+1, y),
             (x-1, y+1), (x, y+1), (x+1, y+1)
           ]

def get_neighbours(grid):
    neighbours = {}

    for position in grid:
        x, y = position

        position_neighbours = neighbours_of_position(x, y)

        neighbours[position] = [p
                                for p in position_neighbours
                                if  0 <= p[0] < x
                                and 0 <= p[1] < y]

    return neighbours