import re

with open('passports.txt') as f:
    passports_input = f.read().split('\n\n')

def height_check(s):
    height = re.match(r'^(\d{1,})(cm|in)$',s)
    print(height)
    if height:
        if height[2] == "cm" and 150 <= int(height[1]) <= 193:
            return True
        elif height[2] == "in" and 59 <= int(height[1]) <= 76:
            return True
    return False

values = {'byr': lambda s: len(s) == 4 and 1920 <= int(s) <= 2002,
          'iyr': lambda s: len(s) == 4 and 2010 <= int(s) <= 2020,
          'eyr': lambda s: len(s) == 4 and 2010 <= int(s) <= 2020,
          'hgt': height_check,
          'hcl': lambda s: re.match(r'#[a-f0-9]{6}', s),
          'ecl': lambda s: s in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
          'pid': lambda s: len(s) == 9 and s.isdigit()
          }


passports = []
for p in passports_input:
    passports.append(p.replace('\n',' ').split(' '))

counter = 0
counter_sec = 0
for p in passports:
    d = dict(i.split(':') for i in p)
    if all(v in d for v in values):
        counter += 1
        checker = True
        for i in values:
            fun = values[i]
            if not fun(d[i]):
                checker = False
        if checker:
            chounter_sec += 1

print(counter)
print(counter_sec)
