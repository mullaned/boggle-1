from random import choice
from string import ascii_uppercase

def make_grid(width, height):
    return {(x, y): choice(ascii_uppercase)
            for x in range(width)
            for y in range(height)}


def neighbours_of_position(position):
    x, y = position
    return [
             (x-1, y-1), (x, y-1), (x+1, y-1),
             (x-1, y),             (x+1, y),
             (x-1, y+1), (x, y+1), (x+1, y+1)
           ]

def get_neighbours(grid):
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]

    return neighbours


def search(grid):
    neighbours = get_neighbours(grid)
    paths = []

    def do_search(path):
        paths.append(path)
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])

    for position in grid:
        do_search([position])

    words = []
    for path in paths:
        words.append(''.join([grid[p] for p in path]))

    return words


grid = make_grid(2, 2)
words = search(grid)

print words
