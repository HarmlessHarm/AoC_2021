import numpy as np

def get_neighbors(arr, row, col):
    mask = np.zeros(arr.shape,dtype=bool)

    mask[row, col-1 if col!=0 else col:col+2] = True
    mask[row-1 if row!=0 else row:row+2, col] = True
    mask[row, col] = False
    indexes = np.where(mask == True)
    return arr[mask], list(zip(indexes[0], indexes[1]))

def explore_recursive(arr, i, j, v, d):
    neighbors, indexes = get_neighbors(arr, i, j)
    
    basin_indexes = [f"{i,j}"]
    # print(f"at {i,j}-{d}, found neighbors {indexes}")
    for i, (m, n) in enumerate(indexes):
        # print(f"Exploring {m, n}", end=" ")
        if neighbors[i] < 9 and neighbors[i] > v:
            # print(f"Neighbour is valid -> recursive")
            basin_indexes += explore_recursive(arr, m, n, neighbors[i], d+1)
        # else:
            # print(f"Neighbour is invalid -> return")
            
    return basin_indexes


with open("day9/input_9.txt", 'r') as f:

    height_map_list = list()

    for line in f.readlines():

        line_ints = list(map(int, list(line.strip())))

        height_map_list.append(line_ints)

    height_map = np.array(height_map_list)


risk_level = 0
basins = list()
for i, row in enumerate(height_map):
    for j, v in enumerate(row):
        neighbors, _ = get_neighbors(height_map, i, j)
        if all(v < n for n in neighbors):
            risk_level += v + 1

            basin_nodes = np.unique(explore_recursive(height_map, i, j, v, 0))
            basin_size = len(basin_nodes)
            basins.append(basin_size)

top_basins = sorted(basins, reverse=True)[:3]

print(f"Risk level is: {risk_level}")

print(f"Top 3 Basin product: {np.prod(top_basins)}")
