"""
Solves https://adventofcode.com/2022/day/2 with minor changes to the code.
Part 1: I had to stitch together the scoring function from two different solutions from ChatGPT but otherwise it got it.
Part 2: I had to prompt ChatGPT with the previous solution to get something that was close. I also had to do several re-runs.
It was never able to compute the 'player_shape' (what to play to achieve the outcome) correctly but it knew that it had to compute it to get the right score.
"""

# Part 1

data = [
    'A Y',
    'B X',
    'C Z'
]

letter_map = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

total_score = 0

for line in open("2.txt").readlines():
    opponent, player = line.strip().split()
    opponent_shape = letter_map[opponent]
    player_shape = letter_map[player]
    if opponent_shape == player_shape:
        # Draw
        score = 3 + player_shape
    elif (opponent_shape - player_shape) % 3 == 1:
        # Opponent wins
        score = player_shape
    else:
        # Player wins
        score = player_shape + 6
    total_score += score

print(total_score)


# Part 2
letter_map = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

total_score = 0

for line in open("2.txt").readlines():
    opponent, outcome = line.strip().split()
    opponent_shape = letter_map[opponent]
    if outcome == "X":
        # Need to lose
        player_shape = opponent_shape-1 if opponent_shape > 1 else 3  # Original: (opponent_shape - 1) % 3
    elif outcome == "Y":
        # Need to draw
        player_shape = opponent_shape
    else:
        # Need to win
        player_shape = opponent_shape+1 if opponent_shape < 3 else 1  # Original: (opponent_shape + 1) % 3

    if opponent_shape == player_shape:
        # Draw
        score = 3 + player_shape
    elif (opponent_shape - player_shape) % 3 == 1:
        # Opponent wins
        score = player_shape
    else:
        # Player wins
        score = player_shape + 6
    total_score += score

print(total_score)
