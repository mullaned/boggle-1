import time
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


def path_to_word(grid, path):
    return ''.join([grid[p] for p in path])


# TODO, Split loading the file, and building the Dictionary, Stems
def get_dictionary(dictionaryFile):
    stems, dictionary = set(), set()

    with open(dictionaryFile) as f:
        for word in f:
            word = word.strip().upper()
            dictionary.add(word)

            for i in range(len(word)):
                stems.add(word[:i + 1])

    return dictionary, stems


def search(grid):
    neighbours = get_neighbours(grid)
    dictionary, stems = get_dictionary('/usr/share/dict/words')

    paths = []

    def do_search(path):
        word = path_to_word(grid, path)
        if word not in stems:
            return
        if word in dictionary:
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


def print_grid(grid):
    s = ''
    for y in range(10):
        for x in range(10):
            s += grid[x, y] + ' '
        s += '\n'
    print s


def time_function(method):
    t1 = time.time()
    res = method()
    print '%2.2f sec' % (time.time() - t1)
    return res


def get_words():
    grid = make_grid(10, 10)
    return search(grid)

# get_words()
