"""
Solves https://adventofcode.com/2022/day/1 without any changes to the code.
Part 1: First attempt - not changes to the code.
Part 2: ChatGPT first responded with a C# solution. I then asked, "What about in python?" and that worked. No changes made other than calling the function in the end.
"""

# Read the input
input_str = ""

with open("1.txt") as f:
    input_str = f.read()

# --- Part 1 ---

# Split the input into blocks
blocks = input_str.strip().split("\n\n")

# Calculate the total calories for each block
calories = [sum(map(int, block.split("\n"))) for block in blocks]

# Find the block with the most calories
max_calories = max(calories)

# Print the result
print(max_calories)

elves = []
current_elf = []
total = 0
top = []

# --- PART 2 ---

from typing import List, Tuple

def find_top_elves(input: List[str]) -> int:
    elves = []
    current_elf = []
    total = 0
    top = []

    for line in input:
        if line.isdigit():
            # Add the calorie count to the current Elf's items
            current_elf.append(int(line))
            total += int(line)
        else:
            # End of the current Elf's items
            # Add the current Elf and their total Calories to the list of top Elves
            top.append((total, current_elf))
            current_elf = []
            total = 0

    # Check the last Elf's items
    top.append((total, current_elf))

    # Sort the list of top Elves by total Calories
    top.sort(key=lambda x: x[0], reverse=True)

    # Find the total Calories carried by the top three Elves
    max = 0
    for i in range(3):
        if i >= len(top):
            break
        for item in top[i][1]:
            max += item

    return max

# Call the function - I had to add this
print(find_top_elves(input_str.split("\n")))
