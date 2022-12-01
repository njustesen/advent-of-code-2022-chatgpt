"""
Solves https://adventofcode.com/2022/day/1 without any changes other than those marked by # ***
"""

# Parse the input
input_str = ""  # *** MODIFIED

with open("dec1.txt") as f:   # *** ADDED
    input_str = f.read()    # *** ADDED

# Split the input into blocks
blocks = input_str.strip().split("\n\n")

# Calculate the total calories for each block
calories = [sum(map(int, block.split("\n"))) for block in blocks]

# Find the block with the most calories
max_calories = max(calories)

# Print the result
print(max_calories)