# Takes a 2D map, converts given characters to walls, poles, and open space respectively, and returns it
# as a 1D vector in a file, with each line being one character


import pathlib

# ~~~~~~~ CONSTANTS ~~~~~~~
WALL_CHAR = "2"
POLE_CHAR = "1"
OPEN_SPACE_CHAR = "0"


# Returns all characters in a given file in a list, with all '\n' removed
def getMapFrom(map_file):
    map_chars = []

    path = pathlib.Path(map_file)
    # Get all characters in the given map_file
    while not path.is_file():
        map_file = input("Invalid map_file, try again: ")
        path = pathlib.Path(map_file)

    with open(map_file) as f:
        while True:
            c = f.read(1)
            map_chars.append(c)
            if not c:
                break

    # Remove all '\n'
    map_chars = [x for x in map_chars if (x != '\n')]
    return map_chars


def writeMap(map, file):
    f = open(file, 'w+')
    for char in map:
        f.write(char + '\n')
    f.close()


# Get info from user
map_file = input("Please enter the name of the map file: ")
# Get the map from the given file
map_chars = getMapFrom(map_file)

raw_pole_chars = input("Please enter which characters represent poles in a comma separated list: ")
raw_wall_chars = input("Please enter which characters represent walls in a comma separated list: ")
raw_open_space_chars = input("Please enter which characters represent open space in a comma separated list: ")

new_map_file = input("Please enter the name of the file you wish to write the converted map to: ")

# Convert raw chars representing walls, poles, and open space to lists
pole_chars = [x.strip() for x in raw_pole_chars.split(',')]
wall_chars = [x.strip() for x in raw_wall_chars.split(',')]
open_space_chars = [x.strip() for x in raw_open_space_chars.split(',')]



# Convert all characters to wall, pole, or open space characters
# Checks if character matches any of the given characters, converts appropriately if it does
def checkChar(char_to_check, pole_chars, wall_chars, open_space_chars):

    for char in pole_chars:
        if char == char_to_check:
            return POLE_CHAR
    for char in wall_chars:
        if char == char_to_check:
            return WALL_CHAR
    for char in open_space_chars:
        if char == char_to_check:
            return OPEN_SPACE_CHAR

    # If the char to check wasn't found in any of the lists, return it unmodified
    return char_to_check

map = [checkChar(c, pole_chars, wall_chars, open_space_chars) for c in map_chars]

writeMap(map, new_map_file)
#Write map to file
###########################################################################