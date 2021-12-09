import re
import numpy as np
from numpy.lib.histograms import histogram_bin_edges


def has_bingo(input_board):

    cols = np.sum(input_board, axis=0)
    rows = np.sum(input_board, axis=1)

    if np.max(rows) >=5 or np.max(cols) >= 5:
        return True
    
    return False

def get_bingo_condition(board):
    global number_sequence
    bingo_board = np.zeros(board.shape)

    for i, n in enumerate(number_sequence):
        bingo_board += board == n
        if has_bingo(bingo_board):
            return bingo_board, i, n


def get_board_score(bingo_board, board, n):
    unmarked = board[bingo_board == 0]
    return np.sum(unmarked) * n

with open("day4/input_4.txt", 'r') as f:

    number_sequence = list(map(int, f.readline().split(',')))
    f.readline()
    boards = list()
    board = list()
    for line in f.readlines():
        if line == "\n":
            boards.append(np.array(board))
            board = list()

        else:
            n_reg = r"(?:(\d+)(?:\s+|\n))"
            nmbrs = list(map(int, re.findall(n_reg, line)))
            board.append(nmbrs)


min_turns = float('inf')
best_score = 0

max_turns = 0
worst_score = 0

for board in boards:

    bingo_board, turns, num = get_bingo_condition(board)

    if turns < min_turns:
        best_score = get_board_score(bingo_board, board, num)
        min_turns = turns

    if turns > max_turns:
        worst_score = get_board_score(bingo_board, board, num)
        max_turns = turns

print(f"Best score is {best_score} in {min_turns}")
print(f"Worst score is {worst_score} in {max_turns}")
    
    
        

