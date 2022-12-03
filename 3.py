"""
Part 1: First two attempts came close - both required two lines to be changed. Third attempt worked without any changes.
Part 2: First two attempts were not good - third attempt worked without changes.
"""

# Part 1

priority = 0
for line in open("3.txt").readlines():
    comp1 = set(line[:len(line) // 2])
    comp2 = set(line[len(line) // 2:])
    common = comp1.intersection(comp2)
    for letter in common:
        if letter.isalpha():
            if letter.islower():
                priority += ord(letter) - ord('a') + 1
            else:
                priority += ord(letter) - ord('A') + 27

print(priority)


# Part 2

priority = 0
lines = open("3.txt").readlines()
for i in range(0, len(lines), 3):
    comp1 = set(lines[i])
    comp2 = set(lines[i + 1])
    comp3 = set(lines[i + 2])
    common = comp1.intersection(comp2, comp3)
    for letter in common:
        if letter.isalpha():
            if letter.islower():
                priority += ord(letter) - ord('a') + 1
            else:
                priority += ord(letter) - ord('A') + 27
            break

print(priority)




