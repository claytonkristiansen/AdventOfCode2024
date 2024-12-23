# Advent of Code 2024 day 5

from pathlib import Path
from functools import cmp_to_key
import re

def CheckRule(update, rule):
    second_found = False
    for i in range(0, len(update)):
        if update[i] == rule[1]:
            second_found = True
        elif update[i] == rule[0] and second_found:
            return False
    return True

def InOrder(item1, item2, rules):
    for rule in rules:
        if rule[0] == item1 and rule[1] == item2:
            return -1
        if rule[1] == item1 and rule[0] == item2:
            return 1
    return 0


data = ""

with open(Path(__file__).parent / 'input.txt', 'r') as f:
    data = f.read().split('\n\n')

# Fun parsing
rules = [[int(num) for num in line.split('|')] for line in data[0].split('\n')]
updates = [[int(num) for num in line.split(',')] for line in data[1].split('\n')]

good_updates = []
bad_updates = []
sum_of_middle = 0

for update in updates:
    is_good = True
    for rule in rules:
        if not CheckRule(update, rule):
            is_good = False
    if is_good:
        good_updates.append(update)
        sum_of_middle += update[int(len(update) / 2)]
    else:
        bad_updates.append(update)

# print(good_updates)
print(sum_of_middle)

print(bad_updates[0])
sorted_updates = []
sorted_middle_sum = 0

for update in bad_updates:
    sorted_update = sorted(update, key=cmp_to_key(lambda item1, item2: InOrder(item1, item2, rules)))
    sorted_middle_sum += sorted_update[int(len(update) / 2)]
    sorted_updates.append(sorted_update)


print(sorted_updates[0])

for update in sorted_updates:
    is_good = True
    for rule in rules:
        if not CheckRule(update, rule):
            is_good = False
    if not is_good:
        print("FAILED")

print(sorted_middle_sum)