from pathlib import Path
import re

data = ""

with open(Path(__file__).parent / 'input.txt', 'r') as f:
    data = f.read()

sum_of_products_1 = 0
sum_of_products_2 = 0


mul_pattern = r"mul\(\d{1,3},\d{1,3}\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_instructions = re.finditer(mul_pattern, data)

for mul_instr in mul_instructions:
    num_pattern = r"\d{1,3}"
    operands = re.finditer(num_pattern, mul_instr.group())
    product = 1
    for operand in operands:
        product *= int(operand.group())
    sum_of_products_1 += product

mul_instructions = re.finditer(mul_pattern, data)
do_instructions = re.finditer(do_pattern, data)
dont_instructions = re.finditer(dont_pattern, data)
instructions = []
instructions.extend(mul_instructions)
instructions.extend(do_instructions)
instructions.extend(dont_instructions)
instructions = sorted(instructions, key=lambda i: i.start())

do = True
for instr in instructions:
    if instr.group() == "do()":
        do = True
    elif instr.group() == "don't()":
        do = False
    elif do and instr.group()[:3] == "mul":
        num_pattern = r"\d{1,3}"
        operands = re.finditer(num_pattern, instr.group())
        product = 1
        for operand in operands:
            product *= int(operand.group())
        sum_of_products_2 += product



print(f"Sum of Products (part 1) is: {sum_of_products_1}")
print(f"Sum of Products (part 2) is: {sum_of_products_2}")
