import collections

with open("jolts.txt") as f:
    lines = f.read().splitlines()
    input = [0] + sorted([int(i) for i in lines])
    input = input + [max(input)+3]

diffs = [b-a for a,b in zip(input, input[1:]) ]
differences = collections.Counter(diffs)
print(differences[1]*differences[3])

poss = [1] + [0]*input[-1]
for i in input[1:]:
    poss[i] = poss[i-1]+poss[i-2]+poss[i-3]
print(poss[-1])
