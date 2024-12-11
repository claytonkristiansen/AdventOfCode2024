from pathlib import Path
import re

data = ""

with open(Path(__file__).parent / 'input.txt', 'r') as f:
    data = [int(x) for x in f.read().split(' ')]

num_blinks = 75

def apply_blink(stones):
    new_stones = []
    for stone in stones:
        stone_str = str(abs(stone))
        stone_str_len = len(stone_str)
        if stone == 0:
            new_stones.append(1)
        # If even number of digits
        elif len(stone_str) % 2 == 0:
            
            new_stones.append(int(stone_str[:int(stone_str_len / 2)]))
            new_stones.append(int(stone_str[int(stone_str_len / 2):]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

stones = data
print(f"Num stones: {len(stones)} ={stones}")

for i in range(0, num_blinks):
    stones = apply_blink(stones)
    print(f"({i}) Num stones: {len(stones)}")
