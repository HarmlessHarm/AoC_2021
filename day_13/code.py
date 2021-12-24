import numpy as np
import re
import os

TEST = False

input_file = ("test_" if TEST else "") + "input.txt"

input_path = os.path.join(os.path.dirname(__file__), input_file)

fold_regexp = r"(x|y)=(\d+)"
point_regexp = r"(\d+),(\d+)"


def do_x_fold(paper, line):

    left, fold, right = np.vsplit(paper, np.array([line, line+1]))

    if left.shape != right.shape:
        print("NOT SIMILAR IN SIZE!!!!")

    left += np.flipud(right)
    left = np.array(left > 0, dtype=int)
    return left

def do_y_fold(paper, line):
    # Hsplit as the matrix is y,x not x,y
    top, fold, bottom = np.hsplit(paper, np.array([line, line+1]))
    
    if top.shape != bottom.shape:
        print("NOT SIMILAR IN SIZE!!!!")
    
    top += np.fliplr(bottom)
    top = np.array(top > 0, dtype=int)
    return top

def print_paper(paper):

    print(paper.T)

def count_points(paper):
    return np.sum(paper)

with open(input_path, 'r') as f:
    
    points = list()
    folds = list()
    point_input = True

    for line in f.readlines():
        # points finished
        if line == "\n":
            point_input = False
            continue
        if point_input:
            x, y = map(int, re.findall(point_regexp, line)[0])
            points.append((x,y))
        
        else:
            dir, nr = re.findall(fold_regexp, line)[0]
            folds.append((dir, int(nr)))

points = np.array(points)
max_x = np.max(points[:,0])
max_y = np.max(points[:,1])

paper = np.zeros((max_x+1, max_y+1))

for x, y in points:
    paper[x, y] = 1


for i, (fold, line) in enumerate(folds):
    if fold == 'x':
        paper = do_x_fold(paper, line)
    else:
        paper = do_y_fold(paper, line)
    if i == 0:
        first_fold = paper.copy()


print(f"After first fold, found {count_points(first_fold)} points")

import matplotlib.pyplot as plt
plt.imshow(paper.T)
plt.show()
