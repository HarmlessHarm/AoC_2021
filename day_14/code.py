import os, re
from collections import Counter, defaultdict

TEST = False

input_file = ("test_" if TEST else "") + "input.txt"

input_path = os.path.join(os.path.dirname(__file__), input_file)


pair_reg = r"([A-Z]{2})\W{4}([A-Z])"


with open(input_path, 'r') as f:
    
    template = list(f.readline().strip())
    pairs = dict()
    
    for line in f.readlines():
        if line == "\n":
            continue
        
        pair, insert = re.findall(pair_reg, line)[0]
        pair = tuple(pair)

        pairs[pair] = insert

original_template = template.copy()
# old_template = template.copy()
STEPS = 10
for s in range(STEPS):
    new_template = template.copy()
    N = 1
    for i in range(len(template) - 1):
        P = tuple(template[i:i+2])
        if P in pairs:
            new_template.insert(i + N, pairs[P])
            N += 1

    template = new_template.copy()

counts = Counter(template)

max_occ = max(counts.values())
min_occ = min(counts.values())

print(f'Max - Min occurences = {max_occ - min_occ}')

pair2pair = dict()

for pair, inserted in pairs.items():
    pair2pair[pair] = [(pair[0], inserted), (inserted, pair[1])]

template_pairs = dict()
for i in range(len(original_template)-1):
    p = tuple(original_template[i:i+2])
    if p not in template_pairs:
        template_pairs[p] = 1
    else:
        template_pairs[p] += 1

# print(pair2pair[('N','N')])
# print(template_pairs)

STEPS = 40
for N in range(STEPS):
    new_temp_pairs = template_pairs.copy()
    for tpair, c in template_pairs.items():
        # print(tpair)
        # print(pair2pair[tpair])
        exp1, exp2 = pair2pair[tpair]
        if exp1 not in new_temp_pairs:
            new_temp_pairs[exp1] = c
        else:
            new_temp_pairs[exp1] += c
        
        if exp2 not in new_temp_pairs:
            new_temp_pairs[exp2] = c
        else:
            new_temp_pairs[exp2] += c
        new_temp_pairs[tpair] -= c

        # print(new_temp_pairs)

    template_pairs = new_temp_pairs.copy()


counter = [(s, e, c) for (s, e), c in template_pairs.items()]

starts = defaultdict(int)
ends = defaultdict(int)

for s, e, c in counter:
    starts[s] += c
    ends[e] += c

counts = {}

for letter in starts:
    counts[letter] = max(starts[letter], ends[letter])

print(f'Max - Min occurences = {max(counts.values()) - min(counts.values())}')