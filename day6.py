from functools import reduce

with open('customs.txt') as f:
    groups = f.read().split('\n\n')


counter_union = 0
counter_intersect = 0
for group in groups:
    union_set = reduce(set.union,map(set,group.split()))
    intersect_set = reduce(set.intersection,map(set,group.split()))
    counter_union += len(union_set)
    counter_intersect += len(intersect_set)

print(counter_union)
print(counter_intersect)
