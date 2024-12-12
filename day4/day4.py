# Advent of Code 2024 day 4
# I totall brute forced the heck out of this one :)

from pathlib import Path
import re

data = ""

with open(Path(__file__).parent / 'input.txt', 'r') as f:
    data = f.readlines()

num_xmas = 0
num_x_mas = 0

for i in range(0, len(data)):
    x_pattern = r"X"
    x_locations = re.finditer(x_pattern, data[i])
    for x_loc in x_locations:
        j = x_loc.start()
        if i > 2:
            # \
            if j > 2:
                if data[i - 1][j - 1] == 'M' \
                   and data[i - 2][j - 2] == 'A' \
                   and data[i - 3][j - 3] == 'S':
                    num_xmas += 1
            # |
            if data[i - 1][j] == 'M' \
               and data[i - 2][j] == 'A' \
               and data[i - 3][j] == 'S':
                num_xmas += 1
            # /
            if j < (len(data[i]) - 3):
                if data[i - 1][j + 1] == 'M' \
                   and data[i - 2][j + 2] == 'A' \
                   and data[i - 3][j + 3] == 'S':
                    num_xmas += 1
        if j < (len(data[i]) - 3):
            # --
            if data[i][j + 1] == 'M' \
               and data[i][j + 2] == 'A' \
               and data[i][j + 3] == 'S':
                num_xmas += 1
        if i < len(data) - 3:
            # \
            if j > 2:
                if data[i + 1][j - 1] == 'M' \
                   and data[i + 2][j - 2] == 'A' \
                   and data[i + 3][j - 3] == 'S':
                    num_xmas += 1
            # |
            if data[i + 1][j] == 'M' \
               and data[i + 2][j] == 'A' \
               and data[i + 3][j] == 'S':
                num_xmas += 1
            # /
            if j < (len(data[i]) - 3):
                if data[i + 1][j + 1] == 'M' \
                   and data[i + 2][j + 2] == 'A' \
                   and data[i + 3][j + 3] == 'S':
                    num_xmas += 1
        if j > 2:
            # --
            if data[i][j - 1] == 'M' \
               and data[i][j - 2] == 'A' \
               and data[i][j - 3] == 'S':
                num_xmas += 1

for i in range(0, len(data)):
    a_pattern = r"A"
    a_locations = re.finditer(a_pattern, data[i])
    for a_loc in a_locations:
        j = a_loc.start()
        if i > 0 and i < (len(data) - 1) and j > 0 and j < (len(data[i]) - 1):
            #M.M
            #.A.
            #S.S
            if data[i - 1][j - 1] == 'M' \
               and data[i - 1][j + 1] == 'M' \
               and data[i + 1][j - 1] == 'S' \
               and data[i + 1][j + 1] == 'S':
                num_x_mas += 1

            #S.S
            #.A.
            #M.M
            if data[i - 1][j - 1] == 'S' \
               and data[i - 1][j + 1] == 'S' \
               and data[i + 1][j - 1] == 'M' \
               and data[i + 1][j + 1] == 'M':
                num_x_mas += 1

            #M.S
            #.A.
            #M.S
            if data[i - 1][j - 1] == 'M' \
               and data[i - 1][j + 1] == 'S' \
               and data[i + 1][j - 1] == 'M' \
               and data[i + 1][j + 1] == 'S':
                num_x_mas += 1

            #S.M
            #.A.
            #S.M
            if data[i - 1][j - 1] == 'S' \
               and data[i - 1][j + 1] == 'M' \
               and data[i + 1][j - 1] == 'S' \
               and data[i + 1][j + 1] == 'M':
                num_x_mas += 1


print(f"Num XMAS: {num_xmas}")
print(f"Num X-MAS: {num_x_mas}")
