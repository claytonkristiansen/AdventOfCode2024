from collections import Counter

def main():
    with open('/home/kristiansenc/repos/AdventOfCode2024/day1/input.txt', 'r') as file:
        lines = file.readlines()
        column1 = []
        column2 = []
        for line in lines:
            col1, col2 = line.split()
            column1.append(int(col1))
            column2.append(int(col2))
    column1 = sorted(column1)
    column2 = sorted(column2)

    count_column1_in_column2 = Counter(column2)
    occurrences = {num: count_column1_in_column2[num] for num in column1}
    print(occurrences)

    similarity_score = 0
    for num in occurrences:
        similarity_score += occurrences[num] * num
    print(similarity_score)

    total_distance = 0
    for i in range(len(column1)):
        total_distance += abs(column1[i] - column2[i])
    # Your main code goes here
    print(total_distance)

if __name__ == "__main__":
    main()