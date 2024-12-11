from pathlib import Path

data = []

with open(Path(__file__).parent / 'input.txt', 'r') as f:
    for line in f.readlines():
        row = [int(x) for x in line.strip().split()]
        data.append(row)

num_safe_reports = 0


# Currently setup for day 2, allows removing one element to still be safe
for levels in data:
    for skip_index in range(0, len(levels)):
        mod_level = levels[:skip_index] + levels[skip_index + 1:]
        safe = True
        increasing = True
        if mod_level[0] - mod_level[1] > 0:
            increasing = False
        prev_level = mod_level[0]
        for i in range(1, len(mod_level)):
            if mod_level[i - 1] == mod_level[i] \
            or (increasing and (mod_level[i - 1] - mod_level[i] > 0)) \
            or ((not increasing) and (mod_level[i - 1] - mod_level[i] < 0)) \
            or (abs(mod_level[i - 1] - mod_level[i]) > 3):
                safe = False
                break
        if safe:
            num_safe_reports += 1
            break

print(f"The number of safe reports is {num_safe_reports}")
