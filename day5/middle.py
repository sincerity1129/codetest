from itertools import combinations

number = [-2, 3, 0, 2, -5]
comb = list(combinations(number, 3))

sums = sum(1 for combination in comb if sum(combination) == 0)
print(sums)