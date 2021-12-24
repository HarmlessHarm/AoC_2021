import os

TEST = False

input_file = ("test_" if TEST else "") + "input.txt"

input_path = os.path.join(os.path.dirname(__file__), input_file)

opening = ['(', '[', '{', '<']
closing = [')', ']', '}', '>']
score = {')':3, ']':57, '}':1197, '>':25137}
auto_score = {')':1, ']':2, '}':3, '>':4}


def get_closing(o):
    return closing[opening.index(o)]

def get_opening(c):
    return opening[closing.index(c)]







with open(input_path, 'r') as f:
    
    syntax_score = 0
    all_complete_scores = []
    
    for line in f.readlines():

        queue = []

        for i, c in enumerate(line):
            if c in opening:
                queue.append(c)
            if c in closing:
                if opening.index(queue[-1]) == closing.index(c):
                    queue.pop()
                else:
                    print(f"Expected: {get_closing(queue[-1])}, Found: {c} instead")
                    syntax_score += score[c]
                    break

        if i == len(line) - 1:
            complete_score = 0
            while len(queue) > 0:
                op_br = queue.pop()
                cl_br = get_closing(op_br)
                # print(cl_br, end=' ')

                complete_score *= 5
                complete_score += auto_score[cl_br]

            all_complete_scores.append(complete_score)

all_complete_scores = sorted(all_complete_scores)

print(f"Syntax Error Highscore is {syntax_score}")
print(f"Auto Complete (Median)Highscore is {all_complete_scores[len(all_complete_scores)//2]}")