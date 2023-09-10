map = []
r = 0
c = 0
count = 0

with open("slopes.txt") as f:
    map = f.readlines()
    map = [line.strip() for line in map]

while r+1 < len(map):
    c += 3
    r += 1

    space = map[r][c%len(map[r])]
    if space == '#':
        count += 1

print(count)

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

total = 1

for slope in slopes:
    tc = 0
    r,c = 0,0

    while r+1 < len(map):
        r += slope[1]
        c += slope[0]
        space = map[r][c%len(map[r])]
        if space == '#':
            tc += 1
    total *= tc

print(total)
