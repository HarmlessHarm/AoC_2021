import numpy as np
import os
import re

TEST = True

input_file = ("test_" if TEST else "") + "input.txt"

input_path = os.path.join(os.path.dirname(__file__), input_file)


line_map = np.zeros((1000, 1000))
line_map_diag = np.zeros((1000, 1000))

with open(input_path, 'r') as f:
    
    coord_reg = r"(?:(\d+),(\d+))\s->\s(?:(\d+),(\d+))"

    for line in f.readlines():
        x1, y1, x2, y2 = map(int, re.findall(coord_reg, line)[0])
        
        dx = x2 - x1
        sx = dx/abs(dx) if dx != 0 else 1
        dy = y2 - y1
        sy = dy/abs(dy) if dy != 0 else 1

        range_x = np.linspace(x1, x2 + sx, abs(dx), dtype=int)
        range_y = np.linspace(y1, y2 + sy, abs(dy), dtype=int)

        print(range_x)
        break
        for x, y in zip(range_x, range_y):
            if x1 == x2 or y1 == y2:
                line_map[y, x] += 1
                line_map_diag[y, x] += 1
            else:
                line_map_diag[y, x] += 1

print(line_map[:10, :10])

overlap = np.sum(line_map >= 2)
print(f"Min 2 overlap (hori | vert): {overlap}")
                
overlap_diag = np.sum(line_map_diag >= 2)
print(f"Min 2 overlap (hori | vert | diag): {overlap_diag}")
                
            
