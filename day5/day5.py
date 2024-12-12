# Advent of Code 2024 day 4

from pathlib import Path
import re

def CheckRule(update, rule):
    second_found = False
    for i in range(0, len(update)):
        if update[i] == rule[1]:
            second_found = True
        elif update[i] == rule[0] and second_found:
            return False
    return True

data = ""

with open(Path(__file__).parent / 'input.txt', 'r') as f:
    data = f.read().split('\n\n')

# Fun parsing
rules = [[int(num) for num in line.split('|')] for line in data[0].split('\n')]
updates = [[int(num) for num in line.split(',')] for line in data[1].split('\n')]

good_updates = []
sum_of_middle = 0

for update in updates:
    is_good = True
    for rule in rules:
        if not CheckRule(update, rule):
            is_good = False
    if is_good:
        good_updates.append(update)
        sum_of_middle += update[int(len(update) / 2)]

# print(good_updates)
print(sum_of_middle)
