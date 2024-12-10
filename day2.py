data = []

with open('/home/a0500846/AdventOfCode2024/day2/input.txt', 'r') as f:
    for line in f.readlines():
        row = [int(x) for x in line.strip().split()]
        data.append(row)

num_safe_reports = 0

for levels in data:
    safe = True
    increasing = True
    have_removed = False
    if levels[0] - levels[1] > 0:
        increasing = False
    prev_level = levels[0]
    for i in range(1, len(levels)):
        if levels[i - 1] == levels[i] \
           or (increasing and (levels[i - 1] - levels[i] > 0)) \
           or ((not increasing) and (levels[i - 1] - levels[i] < 0)) \
           or (abs(levels[i - 1] - levels[i]) > 3):
            if not have_removed:
                if i == (len(levels) - 1):
                    
                if levels[i - 1] == levels[i] \
                   or (increasing and (levels[i - 1] - levels[i] > 0)) \
                   or ((not increasing) and (levels[i - 1] - levels[i] < 0)) \
                   or (abs(levels[i - 1] - levels[i]) > 3):
            else:
                safe = False
                break
    if safe:
        num_safe_reports += 1

print(f"The number of safe reports is {num_safe_reports}")
