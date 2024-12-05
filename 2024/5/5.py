from itertools import permutations
from tqdm import tqdm

def get_ordering_and_updates(s):
    s1, s2 = s.split('\n\n')
    p = [l.split('|') for l in s1.split()]
    u = [l.split(',') for l in s2.split()]
    return p, u

def is_valid_update(u, pairs):
    # first make a dict of number to rank so we dont degenerate to O^2
    rank = {l[0]: l[1] for l in zip(u, range(len(u)))}
    for p in pairs:
        if p[0] in u and p[1] in u and rank[p[0]] > rank[p[1]]:
            return False
    return True

def get_middle_sum_valid(pairs, updates):
    total = 0
    for u in updates:
        # we hope the list has odd number of elements
        if is_valid_update(u, pairs):
            total += int(u[len(u)//2])
    return total

def reorder_update(u, pairs):
    # we assume all can be reordered
    pairs_that_order = [p for p in pairs if p[0] in u and p[1] in u]
    # we're just gonna brute force it LOL
    for permutation in tqdm(permutations(u)):
        if is_valid_update(permutation, pairs):
            return permutation
    raise ValueError('We could not reorder it')

def get_middle_sum_invalid_reorder(pairs, updates):
    total = 0
    for u in updates:
        # we hope the list has odd number of elements
        if not is_valid_update(u, pairs):
            nu = reorder_update(u, pairs)
            total += int(nu[len(nu)//2])
    return total

with open('input.txt', 'r') as f:
    s = f.read()

# pairs, updates = get_ordering_and_updates(s)
# s = get_middle_sum_valid(pairs, updates)
# print(s)


pairs, updates = get_ordering_and_updates(s)
n = get_middle_sum_invalid_reorder(pairs, updates)
print(n)