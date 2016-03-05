from random import choice
from string import ascii_uppercase

from profile import time_function


def play_boggle():
    grid = make_grid(20, 20)
    dictionary = get_dictionary('/usr/share/dict/words')

    words = search(grid, dictionary)

    display_grid(grid)
    display_words(words)


def make_grid(width, height):
    return {(x, y): choice(ascii_uppercase)
            for x in range(width)
            for y in range(height)}


def grid_as_text(grid):
    height = max(grid)[0] + 1
    width = max(grid)[1] + 1
    rows = []
    for x in range(height):
        rows.append(' '.join([grid[x, y] for y in range(width)]))
    return rows


def display_grid(grid):
    for line in grid_as_text(grid):
        print line


def path_to_word(grid, path):
    return ''.join([grid[p] for p in path])


def display_words(words):
    print "Found", len(words), "Words"
    print ", ".join(words)


def neighbours_of_position(position):
    x, y = position
    return [
             (x-1, y-1), (x, y-1), (x+1, y-1),
             (x-1, y),             (x+1, y),
             (x-1, y+1), (x, y+1), (x+1, y+1)
           ]


def all_grid_neighbours(grid):
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours


def get_dictionary(dictionary_file):
    dictionary, stems = set(), set()

    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            dictionary.add(word)

            for i in range(len(word)):
                stems.add(word[:i + 1])

    return dictionary, stems


def search(grid, dictionary):
    word_list, stems = dictionary
    neighbours = all_grid_neighbours(grid)

    paths = []

    def do_search(path):
        word = path_to_word(grid, path)
        if word not in stems:
            return
        if word in word_list:
            paths.append(path)
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])

    for position in grid:
        do_search([position])

    words = []
    for path in paths:
        words.append(path_to_word(grid, path))

    return set(words)


time_function(play_boggle)
