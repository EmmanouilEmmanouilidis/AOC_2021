with open("plane_seats.txt") as f:
    seatings  = f.readlines()
    seatings = [line.strip() for line in seatings]

seats =[]
for seat in seatings:
    row = int(seat[:7].replace('F','0').replace('B','1'),2)
    col = int(seat[7:].replace('L','0').replace('R','1'),2)
    seat_id = row * 8 + col

    seats.append(seat_id)

print(max(seats))

seats = sorted(seats)

my_seat = set(range(seats[o],seats[-1])) - set(seats)
print(my_seat)

"""
bin_codes =[]
for seat in seatings:
    position = list(seat)
    for i in range(0,10):
        if position[i] == "F":
            position[i] = "0"
        elif position[i] == "B":
            position[i] = "1"
        elif position[i] == "L":
            position[i] = "0"
        elif position[i] == "R":
            position[i] = "1"
    bin_codes.append(''.join(position))

rows = []
columns = []
for code in bin_codes:
    rows.append(int("".join(str(x) for x in code[0:7]), 2))
    columns.append(int("".join(str(x) for x in code[7:10]), 2))

solutions = []

for i in range(len(rows)):
    solutions.append(rows[i]*8+columns[i])

#print(max(solutions))

sorted_list = sorted(solutions)
print(sorted_list)
sol = []
for i  in range(0,len(sorted_list)-1):
    if sorted_list[i]+1 != sorted_list[i+1]:
        sol = sorted_list[i] + 1
print(sol)
"""
