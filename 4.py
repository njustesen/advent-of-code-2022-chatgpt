"""
Part 1: Solved it in first attempt.
Part 2: Solved it in first attempt.
"""

# Part 1

counter = 0
for line in open("4.txt").readlines():
    range1, range2 = line.strip().split(",")
    start1, end1 = map(int, range1.split("-"))
    start2, end2 = map(int, range2.split("-"))
    range1 = set(range(start1, end1 + 1))
    range2 = set(range(start2, end2 + 1))
    if range1.issubset(range2) or range2.issubset(range1):
        counter += 1

print(counter)

# Part 2

counter = 0
for line in open("4.txt").readlines():
    range1, range2 = line.strip().split(",")
    start1, end1 = map(int, range1.split("-"))
    start2, end2 = map(int, range2.split("-"))
    range1 = set(range(start1, end1 + 1))
    range2 = set(range(start2, end2 + 1))
    if range1.intersection(range2):
        counter += 1

print(counter)
