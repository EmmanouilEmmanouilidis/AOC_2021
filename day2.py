import re

lines = []

with open("passwords.txt") as f:
    lines = f.readlines()

valid = 0
val2 = 0
pattern = '([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)'

for i in lines:
    match = re.search(pattern, i)
    min_amount = int(match.group(1))
    max_amount = int(match.group(2))
    char = match.group(3)
    password = match.group(4)
    count = password.count(char)
    if count >= min_amount and count <= max_amount:
        valid += 1

    if password[min_amount-1] == char and not password[max_amount-1]== char:
        val2 += 1
    elif password[max_amount-1] == char and not password[min_amount-1]== char:
        val2 += 1

print(valid)
print(val2)
