import os

TEST = True

input_file = ("test_" if TEST else "") + "input.txt"

input_path = os.path.join(os.path.dirname(__file__), input_file)

with open(input_path, 'r') as f:
    pass